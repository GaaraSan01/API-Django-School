from django.contrib import admin
from escola.models import TableAlunos, TableCursos, TableMatriculas
# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_birth', 'cpf', 'rg')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(TableAlunos, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'cod_curso', 'description')
    list_display_links = ('id', 'cod_curso')
    search_fields = ('cod_curso',)
    list_per_page = 20

admin.site.register(TableCursos, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(TableMatriculas, Matriculas)