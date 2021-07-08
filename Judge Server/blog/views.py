from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from froala_editor.fields import FroalaField
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def savecomment(request):
    temp=Post.objects.get(id=request.POST['objID'])
    temp.comment_set.create(usr=request.user,text=request.POST['comment'])
    temp.save()
    return HttpResponse("")





def home(request):
        

    context = {
        'posts': Post.objects.all(),
    }   
    return render(request, 'blog/home.html',context)

def comment(request):
    temp=Post.objects.get(id=request.POST['objID'])
    temp.comment_set.create(usr=request.user,text=request.POST['comment'])
    temp.save()
    next = request.POST.get('next', '/')
    messages.success(request, f'Comment successful')
    return HttpResponseRedirect(next)

@csrf_exempt
def upvote(request):
    temp=Comment.objects.get(id=request.POST['comment_id'])
    if request.user not in temp.user_reaction.all():
        temp.vote+=1
        temp.user_reaction.add(request.user)
        temp.save()
    return HttpResponse('')
@csrf_exempt
def downvote(request):
    temp=Comment.objects.get(id=request.POST['comment_id'])
    if request.user not in temp.user_reaction.all():
        temp.vote-=1
        temp.user_reaction.add(request.user)
        temp.save()
    return HttpResponse('')

def deleteComment(request,comment):
    temp=Comment.objects.get(id=comment)
    val='/discuss/post/'+str(temp.post.id)
    temp.delete()
    return HttpResponseRedirect(val)

class PostListView(ListView):
    model=Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model=Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

        

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post

    success_url = '/discuss'
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False


    