from rest_framework import generics
from .serializers import PostSerializer

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import CustomUserCreationForm
from .models import CustomUser

class PostList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserListView(ListView):
    model = CustomUser
    template_name = 'users.html'
    context_object_name = 'object_list'

class UserListUpdate(UpdateView):
    model = CustomUser
    fields = ('username', 'phone', 'email', 'password',)
    template_name = 'user_edit.html'
    success_url = reverse_lazy('users')

class UserListDelete(DeleteView):
    model = CustomUser
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users')