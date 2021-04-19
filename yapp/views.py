from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, FeedBackModel, FeedBackReply, Note
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm, FeedbackCreateForm, ReplyForm, NoteCreate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(ListView):
    model = Post
    template_name = 'yapp/index.html'
    ordering = ['-id']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'yapp/detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'yapp/create.html'
    success_url = reverse_lazy('index')

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    #fields = '__all__'
    template_name = 'yapp/update.html'
    success_url = reverse_lazy('index')

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'yapp/delete.html'
    success_url = reverse_lazy('index')

class BlogUserListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'yapp/list.html'
    ordering = ['-id']

class BlogCommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    #fields = '__all__'
    template_name = 'yapp/addcomment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    
    success_url = reverse_lazy('index')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        form = Post.objects.filter(title__contains=searched)
        ordering = ['-id']
        return render(request, 'yapp/search.html', {'searched':searched, 'form':form})
        
    else:
        return render(request, 'yapp/search.html', {})

def search_user(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        form = Post.objects.filter(title__contains=searched)
        return render(request, 'yapp/user_search.html', {'searched':searched, 'form':form})
    else:
        return redirect(request, 'yapp/user_search.html', {})

def search_feedback(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        form = FeedBackModel.objects.filter(title__contains=searched)
        return render(request, 'yapp/comment/feed_search.html', {'searched':searched, 'form':form})
    else:
         return render(request, 'yapp/comment/feed_search.html', {})
'''
def BlogUserLoginView(request):
    model = User
    form = LoginForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is not Correct!!')

    return render(request, 'user/login.html', {'form':form})
'''

class FeedBackCreate(LoginRequiredMixin, CreateView):
    model = FeedBackModel
    #fields = '__all__'
    form_class = FeedbackCreateForm
    template_name = 'yapp/comment/create.html'
    success_url = reverse_lazy('feedbacklist')
   

class FeedBackList(ListView):
    model = FeedBackModel
    template_name = 'yapp/comment/list.html'
    ordering = ['-id']

class FeedBackUserList(LoginRequiredMixin, ListView):
    model = FeedBackModel
    template_name = 'yapp/comment/userfeed.html'
    ordering = ['-id']

class BlogReplyCreateView(CreateView):
    model = FeedBackReply
    form_class = ReplyForm
    #fields = '__all__'
    template_name = 'yapp/comment/addreply.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('feedbacklist')

def BlogParticularUserFeed(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        form = FeedBackModel.objects.filter(title__contains=searched)
        return render(request, 'yapp/comment/specific.html', {'searched':searched, 'form':form})
    else:
        return render(request, 'yapp/comment/specific.html', {})

'''
class BlogReplyListView(DetailView):
    model = FeedBackReply
    template_name = 'yapp/comment/viewreply.html'
'''
class BlogReply(DetailView):
    model = FeedBackModel
    template_name = 'yapp/comment/viewreply.html'
    
    
class NoteUserCreate(LoginRequiredMixin, CreateView):
    model = Note
    #fields = '__all__'
    form_class = NoteCreate
    template_name = 'yapp/notes/create.html'
    success_url = reverse_lazy('note_list')

class NoteUserList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'yapp/notes/list.html'
    ordering = ['-id']

class NoteUserDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'yapp/notes/detail.html'

class NoteUserDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'yapp/notes/delete.html'

class NoteUserUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteCreate
    template_name = 'yapp/notes/update.html'
    success_url = reverse_lazy('note_list')

def NoteSearchListView(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        form = Note.objects.filter(title__contains=searched)
        return render(request, 'yapp/notes/search.html', {'searched':searched, 'form':form})
    else:
        return render(request, 'yapp/notes/search.html', {})


