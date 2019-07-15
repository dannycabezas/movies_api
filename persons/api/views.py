from persons.models import Person
from persons.api.serializers import PersonCreateSerializer
from persons.api.serializers import PersonSerializer
from persons.api.serializers import PersonUpdateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class PersonListAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonCreateAPIView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonCreateSerializer
    permission_classes = [IsAuthenticated]


class PersonUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PersonDeleteAPIView(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsOwnerOrReadOnly]
