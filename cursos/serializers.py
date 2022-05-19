from rest_framework import serializer 
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializer.ModelSerializer):
    
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao', 
            'ativo',
        )
        
        

class CursoSerializer(serializer.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )