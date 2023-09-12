from rest_framework import serializers
from .models import Box
from .filters import MyBoxFilter, ListBoxFilter


class AdminBoxSerializer(serializers.ModelSerializer):
    area = serializers.ReadOnlyField()
    volume = serializers.ReadOnlyField()

    class Meta:
        model = Box
        fields = "__all__"


class GuestBoxSerializer(serializers.ModelSerializer):
    area = serializers.ReadOnlyField()
    volume = serializers.ReadOnlyField()

    class Meta:
        model = Box
        fields = (
            "id",
            "length",
            "breadth",
            "height",
            "area",
            "volume",
        )


