from rest_framework import generics, mixins
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import newUserModel
from .serializers import newUserModelSerializers

from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly

from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.

class newUserModelList(mixins.ListModelMixin,generics.DestroyAPIView,mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView ):
    queryset = newUserModel.objects.all()
    serializer_class = newUserModelSerializers
    #authentication
    authentication_classes = [TokenAuthentication]
    #permission
    permission_classes = [DjangoModelPermissions, IsAuthenticatedOrReadOnly]
    
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:  
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({"message": "No user found"})

mixinView = newUserModelList.as_view()    

#detail user
