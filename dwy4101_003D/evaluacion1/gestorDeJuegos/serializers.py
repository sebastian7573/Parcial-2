from rest_framework import serializers 
from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):     
    class Meta:         
        model = Reserva    
        fields = ('nombre','categoria','plataforma')