from django.db import models

# Create your models here.
class Colaboradores(models.Model):
    id_colaborador = models.IntegerField(primary_key=True)
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome

class Financiador(models.Model):
    id_financiador = models.IntegerField(primary_key=True)
    financiador = models.CharField(max_length=100)

    def __str__(self):
        return self.financiador

class AreasTecnologicas(models.Model):
    id_area_tecnologica = models.IntegerField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100)

    def __str__(self):
        return self.area_tecnologica


class Projetos(models.Model):
    id_projeto = models.IntegerField(primary_key=True)
    projeto = models.CharField(max_length=100)
    id_financiador = models.ForeignKey(Financiador, on_delete=models.CASCADE)
    id_area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.CASCADE)
    coordenador = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits= 20, decimal_places=2)
    equipe = models.ManyToManyField(Colaboradores)

    def __str__(self):
        return self.projeto











    