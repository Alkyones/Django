from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import registeredUserModel
from .serializers import registeredUserSerializer

#create or view
class registeredUserList(generics.ListCreateAPIView):
    queryset = registeredUserModel.objects.all()
    serializer_class = registeredUserSerializer

    def perform_create(self, serializer):
        serializer.save()
#detail
class registeredUserDetail(generics.RetrieveAPIView):
    queryset = registeredUserModel.objects.all()
    serializer_class = registeredUserSerializer
    lookup_field = 'pk'
    def get_object(self):
        return get_object_or_404(registeredUserModel, pk=self.kwargs.get('pk'))

# delete
class registeredUserDelete(generics.DestroyAPIView):
    queryset = registeredUserModel.objects.all()
    serializer_class = registeredUserSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "User deleted successfully"})

class registeredUserUpdate(generics.UpdateAPIView):
    queryset = registeredUserModel.objects.all()
    serializer_class = registeredUserSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()
        return Response({"message": "User updated successfully"})





#/users/create/
create_view = registeredUserList.as_view()
#/users/delete/<pk>/
delete_view = registeredUserDelete.as_view()
#/users/detail/<pk>/
detail_view = registeredUserDetail.as_view()
#/users/update/<pk>/
update_view = registeredUserUpdate.as_view()