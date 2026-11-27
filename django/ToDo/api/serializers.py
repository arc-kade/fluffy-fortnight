from rest_framework import serializers
from todoapp.models import Todos

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = "__all__"
        