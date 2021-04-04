from django.urls import path
from .views import (
    SignUpView, 
    UserListView, 
    UserListUpdate, 
    UserListDelete,
    PostList,
    PostDetail,
)

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('api/', PostList.as_view()),
    path('api/<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/edit/', UserListUpdate.as_view(), name='user_edit'),
    path('<int:pk>/delete/', UserListDelete.as_view(), name='user_delete'),
    path('signup/', SignUpView.as_view(), name='signup'), 
]
