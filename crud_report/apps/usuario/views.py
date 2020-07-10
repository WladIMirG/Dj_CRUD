import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView, View
from apps.usuario.models import Usuario
from apps.usuario.forms import FormularioLogin, FormularioUsuario
from apps.usuario.mixins import LoginYSuperStaffMixin, ValidarPermisosRequeridosUsuariosMixin
from apps.book.models import Book
from apps.comment.models import Comment
from apps.book.views import ListBook

import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


_HOME = 'home.html'
_INDEX = 'index.html'

class SalePDF(View):
    Book = Book
    Comment = Comment
    def get_context_data(self):
        context = {}
        context['book'] = Book.objects.filter(state = True)
        context['comment'] = Comment.objects.filter()
        return context



    def get(self, request, pk, *args, **kwargs):
        #try:
        if pk == 1:
            template_path = 'pdf/genpdf.html'
        else:
            template_path = 'pdf/comment_genpdf.html'
#        context = {
#            'title':'Este es mi primer pdf',
#            'book': Book.objects.filter(state = True),}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        
        template = get_template(template_path)
        html = template.render(self.get_context_data())

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
        #except:
        #    pass
        #return HttpResponseRedirect(reverse_lazy('book:list_book'))
        #return HttpResponse("Hola")




class Inicio(LoginRequiredMixin,TemplateView):
    """Clase que renderiza el index del sistema"""
    template_name = _INDEX


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class InicioUsuarios(
    LoginYSuperStaffMixin,
    ValidarPermisosRequeridosUsuariosMixin,
    TemplateView):
    template_name='usuarios/inicio.html'


class ListadoUsuario(LoginYSuperStaffMixin, ValidarPermisosRequeridosUsuariosMixin,ListView):
    model = Usuario

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('usuarios:inicio_usuarios')


class RegistrarUsuario(LoginYSuperStaffMixin, ValidarPermisosRequeridosUsuariosMixin, CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    nombres=form.cleaned_data.get('nombres'),
                    apellidos=form.cleaned_data.get('apellidos')
                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios:inicio_usuarios')


class EditarUsuario(LoginYSuperStaffMixin, ValidarPermisosRequeridosUsuariosMixin, UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios:inicio_usuarios')


class EliminarUsuario(LoginYSuperStaffMixin, ValidarPermisosRequeridosUsuariosMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar.html'

    def delete(self,request,*args,**kwargs):
        if request.is_ajax():
            usuario = self.get_object()
            usuario.usuario_activo = False
            usuario.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('usuarios:inicio_usuarios')
