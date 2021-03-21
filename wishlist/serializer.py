from rest_framework import serializers
from wishlist.models import WishListModel

class WishListSerializer(serializers.ModelSerializer):
        def to_representation(self,instance):
        representation = super(CreditCardSerializer, self).to_representation(instance)
        return representation