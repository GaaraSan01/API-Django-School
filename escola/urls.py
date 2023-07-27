from django.urls import path, include
from escola.views import AlunosViewsSet, CursosViewsSet, MatriculasViewsSet, ListMatriculasAlunoViewsSet, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewsSet, basename='alunos')
router.register('cursos', CursosViewsSet, basename='cursos')
router.register('matriculas', MatriculasViewsSet, basename='matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListMatriculasAlunoViewsSet.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]