from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
          "id": instance.id,
          "name": instance.name
        }
