from rest_framework import serializers
from .models import Projetos, Colaboradores

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'

class ColaboradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaboradores
        fields = '__all__'
