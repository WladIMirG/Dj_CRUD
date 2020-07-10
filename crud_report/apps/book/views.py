from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_url = reverse_lazy('book:list_book')

class ListBook(View):
    model = Book
    form_class = BookForm
    template_name = 'book/list_book.html'
    queryset = Book.objects.filter(state = True)

    def get_queryset(self):
        return self.model.objects.filter(state = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['book'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())


class UpdateBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/edit_book.html'
    success_url = reverse_lazy('book:list_book')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['book_form'] = Book.objects.filter(state = True)
        return context

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy('book:list_book')

#    def post(self,request,pk,*args,**kwargs):
#        object = Book.objects.get(id_book = pk)
#        object.state = False
#        object.save()
#        return redirect('book:list_book')