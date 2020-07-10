from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm
from apps.book.models import Book

class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/create_comment.html'
    success_url = reverse_lazy('book:list_book')

 #   def post(self,request,*args,**kwargs):
 #       object = Comment.objects.filter()
 #       object.save()
 #       return redirect('comment:list_comment')


class ListComment(View):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/list_comment.html'


    def get_queryset(self):
       return self.model.objects.filter()

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['comment'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

class UpdateComment(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/edit_comment.html'
    success_url = reverse_lazy('comment:list_comment')

class DeleteComment(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment:list_comment')
