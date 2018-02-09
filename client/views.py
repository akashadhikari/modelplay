from rest_framework import generics

from .models import (
	Client,
	)
from .serializers import (
	ClientSerializer,
	)


class ClientViewSet(generics.ListCreateAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

	def perform_create(self, serializer):
			serializer.save() # Adding owner=self.request.user


class ClientDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer
