from rest_framework.serializers import ModelSerializer

from .models import newUserModel


class newUserModelSerializers(ModelSerializer):
    class Meta:
        model = newUserModel
        fields = '__all__'  # '__all__' is a special keyword that returns all the fields of the model

        