from rest_framework import serializers
from escola.models import TableAlunos, TableCursos, TableMatriculas

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableAlunos
        fields = ['id', 'name', 'date_birth', 'cpf', 'rg']


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableCursos
        fields = '__all__'

class MatriculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableMatriculas
        exclude = []

class ListMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.description')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = TableMatriculas
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_name = serializers.ReadOnlyField(source='aluno.name')
    class Meta:
        model = TableMatriculas
        fields = ['aluno_name']