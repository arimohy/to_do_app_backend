from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from bson import ObjectId

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = '_id'

    def get_object(self):
        _id = self.kwargs['_id']
        return Task.objects.filter(_id=ObjectId(_id)).first()
