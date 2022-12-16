from rest_framework import serializers
from miApp.models import Inscritos, Institucion

class Inscritos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'
        
class Institucion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'