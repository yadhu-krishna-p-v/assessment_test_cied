from django.urls import path
from apps.users.views import UserCrudAPIView, UserListView
urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list_api'),
    path('users/<int:pk>/', UserCrudAPIView.as_view(), name='user_crud_api_with_pk'),
]