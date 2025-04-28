from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.authentication.models import User
from apps.authentication.serializers import RegisterSerializer
from apps.authentication.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated


class UserListView(generics.ListCreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class UserCrudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    authentication_classes = []
    
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)
    
    