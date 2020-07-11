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
    su = Usuario
    

    def link_callback(self, uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

    def get_context_data(self):
        context = {}
        context['book'] = Book.objects.filter(state = True)
        context['comment'] = Comment.objects.filter()
        context['usuario'] = Usuario.objects.filter(is_active=True)
        context['comp'] = {'nombre': 'Intelli next', 'direccion': 'Carrera 11 # 94 - 02, oficina 109, Bogotá - Colombia.', 'telefono':'(1) 695 6100', 'mail':'info@intelli-next.com', 'web':'https://www.intelli-next.com/'}
        context['icon'] = '{}{}'.format(settings.STATIC_URL, 'images/logo45.png')
        return context

    def get(self, request, pk, *args, **kwargs):
        #try:
        if pk == 1:
            template_path = 'pdf/user_genpdf.html'
            filename = "user_report.pdf"
        elif pk == 2:
            template_path = 'pdf/genpdf.html'
            filename = "book_report.pdf"
        else:
            template_path = 'pdf/comment_genpdf.html'
            filename = "comment_report.pdf"

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename='+filename
        
        template = get_template(template_path)
        html = template.render(self.get_context_data())

        pisa_status = pisa.CreatePDF(html, dest=response, link_callback=self.link_callback)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
        

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


class InicioUsuarios(LoginYSuperStaffMixin,ValidarPermisosRequeridosUsuariosMixin,TemplateView):
    template_name='usuarios/inicio.html'


class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/listar.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)
    
class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear.html'
    # success_url = reverse_lazy('usuarios:listar_usuarios')

    def post(self, request, *args, **kwargs):
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
            return redirect('usuarios:listar_usuarios')
        else:
            return render(request,self.template_name,{'form',form})

class EditarUsuario(UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar.html'
    # success_url = reverse_lazy('usuarios:listar_usuarios')

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,instance = self.get_object())
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_usuarios')
        else:
            return render(request,self.template_name,{'form',form})

class EliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')
