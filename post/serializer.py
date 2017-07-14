from rest_framework import serializers

from post.models import LostPost


class LostSerializer(serializers.ModelSerializer):
    ownerID = serializers.ReadOnlyField(source='owner.id')
    ownerUsername = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LostPost
        fields = ('id', 'name', 'text', 'ownerID', 'ownerUsername')
