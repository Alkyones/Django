from django.shortcuts import get_object_or_404
from rest_framework import generics , mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin

class ProductDetailAPIView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'

class ProductListCreateAPIView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'   # this is not needed because we are using the primary key of the model

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        print(serializer)
        serializer.save(user= self.request.user ,content = content)

    # def get_queryset(self,*args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     print(self.request.user)
    #     return qs.filter(user=self.request.user)

class ProductDeleteAPIView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance.delete()
        super().perform_destroy(instance)   

class ProductUpdateAPIView(StaffEditorPermissionMixin,UserQuerySetMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return Response({"message": "You must provide an ID"})
        else:
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            return Response({"message": "You must provide an ID"})
        else:
            return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content = content)

@api_view(['GET', 'POST'])
def product_alt_view(request,pk = None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # #detail of product
            # product = Product.objects.filter(pk=pk)
            # if not product.exists():
            #     return Response({'error': 'Product does not exist'})
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data 
            return Response(data)    
        #list of products
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == 'POST':
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data, status=201)