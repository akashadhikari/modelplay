from rest_framework import serializers

from .models import (
    Client,
    )


class ClientSerializer(serializers.ModelSerializer):

    #client_listofproduct = ListOfProductSerializer

    class Meta:
        model = Client
        fields = '__all__'