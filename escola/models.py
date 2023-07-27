from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class TableAlunos(models.Model):
    name = models.CharField(max_length=55, blank=False, null=False)
    date_birth = models.DateField()
    cpf = models.CharField(max_length=11, blank=False, null=False)
    rg = models.CharField(max_length=9, blank=False, null=False)

    def __str__(self):
        return self.name

class TableCursos(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    cod_curso = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    nivel = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL, default='B')

    def __str__(self):
        return self.description

class TableMatriculas(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespentino'),
        ('N', 'Noturno')
    )

    aluno = models.ForeignKey(TableAlunos, on_delete=models.CASCADE)
    curso = models.ForeignKey(TableCursos, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')