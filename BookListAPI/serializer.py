from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from .models import MenuItem, Category, Rating

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory','category','category_id']

class RatingSerializer (serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
            default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Rating
        fields = ['user', 'menuitem_id', 'rating']

        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['user', 'menuitem_id']
            )
        ]

        extra_kwargs = {
            'rating': {'min_value': 0, 'max_value':5},
        }

# Method 1 Serializer:
# from rest_framework import serializers
# from decimal import Decimal
# from .models import MenuItem, Category 
# class CategorySerializer (serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id','slug','title']
#  
# class MenuItemSerializer(serializers.ModelSerializer):
#     stock =  serializers.IntegerField(source='inventory')
#     price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
#     category = CategorySerializer()
#     class Meta:
#         model = MenuItem
#         fields = ['id','title','price','stock', 'price_after_tax','category']
#     
#     def calculate_tax(self, product:MenuItem):
#         return product.price * Decimal(1.1)

# Method 2 Serializer:
# class MenuItemSerializer(serializers.ModelSerializer):
#     stock =  serializers.IntegerField(source='inventory')
#     price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
#     # category = CategorySerializer()
#     class Meta:
#         model = MenuItem
#         fields = ['id','title','price','stock', 'price_after_tax','category']
#         depth = 1
#     
#     def calculate_tax(self, product:MenuItem):
#         return product.price * Decimal(1.1)
