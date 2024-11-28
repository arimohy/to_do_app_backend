from rest_framework import serializers
from .models import Task
from bson import ObjectId

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['_id', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Manejo de ObjectId para asegurar que se actualiza correctamente
        if '_id' in validated_data:
            validated_data['_id'] = ObjectId(validated_data['_id'])
        return super().update(instance, validated_data)
