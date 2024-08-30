from rest_framework import serializers
from .models import DishModel

class DishSerializer(serializers.ModelSerializer):
    categoryId_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = DishModel
        fields = ['id','dishName','price','categoryId_id']
        read_only_fields = ['id']


class DishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishModel
        fields = DishSerializer.Meta.fields+['dishImage']
        read_only_fields = ['id']

class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishModel
        fields = ['id','dishImage']
        read_only_fields = ['id']
        extra_kwargs = {'image' : {'required' : True}}