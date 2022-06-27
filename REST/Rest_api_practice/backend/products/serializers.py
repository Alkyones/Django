from rest_framework import serializers, reverse

from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field='pk',
    )
    class Meta:
        model = Product
        fields = [
        "pk",
        'url',
        'edit_url',
        "title",
        "content",
        "price",
        "sale_price",
        "my_discount"]
    
    def url(self, obj):
        request = self.context.get('request')
        if request is None :
            return None

        return reverse("product-detail", kwargs={"pk": obj.pk},request=request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj,'id'):
            return None
        return obj.get_discount()
