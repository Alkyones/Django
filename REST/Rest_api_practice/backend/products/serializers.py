from asyncore import read, write
from ipykernel import write_connection_file
from rest_framework import serializers, reverse

from .models import Product
from . import validators

from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(read_only = True, source='user')
    my_user_data = serializers.SerializerMethodField(read_only = True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    # name = serializers.CharField(source = 'title', read_only= True)

    class Meta:
        model = Product
        fields = [
        "owner",
        "pk",
        'url',
        # 'edit_url',
        "title",
        # 'name',
        "content",
        "price",
        "sale_price",
        "my_discount",
        "my_user_data"]
    
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }


    # def create(self, validated_data):
    #     #email = validated_data.pop('email')
    #     product = super().create(validated_data)
        
    #     return product
    

    #custom_validation
    # def validate_title(self,value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exists")
        
    #     return value

    def url(self, obj):
        request = self.context.get('request')
        if request is None :
            return None

        return reverse("product-detail", kwargs={"pk": obj.pk},request=request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj,'id'):
            return None
        return obj.get_discount()
