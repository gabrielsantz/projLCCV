from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Projetos, Colaboradores
from .serializers import ProjetosSerializer, ColaboradoresSerializer

# /projetos/listar/
@api_view(['GET'])
def listar_projetos(request):
    projetos = Projetos.objects.all()
    serializer = ProjetosSerializer(projetos, many=True)
    return Response(serializer.data)

# /projetos/cadastrar/
@api_view(['POST'])
def cadastrar_projeto(request):
    serializer = ProjetosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /colaboradores/listar/
@api_view(['GET'])
def listar_colaboradores(request):
    colaboradores = Colaboradores.objects.all()
    serializer = ColaboradoresSerializer(colaboradores, many=True)
    return Response(serializer.data)

# /colaboradores/cadastrar/
@api_view(['POST'])
def cadastrar_colaborador(request):
    serializer = ColaboradoresSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



