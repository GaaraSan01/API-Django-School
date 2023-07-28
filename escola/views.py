from rest_framework import viewsets, generics
from escola.models import TableAlunos, TableCursos, TableMatriculas
from escola.serializer import AlunoSerializer, CursosSerializer, MatriculasSerializer, ListMatriculasAlunoSerializer, ListAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(a)"""
    queryset = TableAlunos.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewsSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = TableCursos.objects.all()
    serializer_class = CursosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewsSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = TableMatriculas.objects.all()
    serializer_class = MatriculasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListMatriculasAlunoViewsSet(generics.ListAPIView):
    """Listando as matriculas do aluno"""
    def get_queryset(self):
        queryset = TableMatriculas.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = TableMatriculas.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]