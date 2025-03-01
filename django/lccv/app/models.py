from django.db import models

# Create your models here.
class Colaboradores(models.Model):
    id_colaborador = models.IntegerField(primary_key=True, verbose_name='ID do Colaborador')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    nome = models.CharField(max_length=100,verbose_name='Nome')
    dt_nascimento = models.DateField(verbose_name='Data de Nascimento')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

class Financiador(models.Model):
    id_financiador = models.IntegerField(primary_key=True, verbose_name='ID do Financiador')
    financiador = models.CharField(max_length=100, verbose_name='Financiador')

    def __str__(self):
        return self.financiador
    
    class Meta:
        verbose_name = 'Financiador'
        verbose_name_plural = 'Financiadores'

class AreasTecnologicas(models.Model):
    id_area_tecnologica = models.IntegerField(primary_key=True, verbose_name='ID da Área Tecnológica')
    area_tecnologica = models.CharField(max_length=100, verbose_name='Área Tecnológica')

    def __str__(self):
        return self.area_tecnologica
    
    class Meta:
        verbose_name = 'Área Tecnológica'
        verbose_name_plural = 'Áreas Tecnológicas'


class Projetos(models.Model):
    id_projeto = models.IntegerField(primary_key=True, verbose_name='ID do Projeto')
    projeto = models.CharField(max_length=100, verbose_name='Projeto')
    id_financiador = models.ForeignKey(Financiador, on_delete=models.CASCADE, verbose_name='Financiador')
    id_area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.CASCADE, verbose_name='Área Tecnológica')
    coordenador = models.CharField(max_length=100, verbose_name='Coordenador')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    inicio_vigencia = models.DateField(verbose_name='Início da Vigência')
    fim_vigencia = models.DateField(null=True, blank=True, verbose_name='Fim da Vigência')
    valor = models.DecimalField(max_digits= 20, decimal_places=2, verbose_name='Valor')
    equipe = models.ManyToManyField(Colaboradores, verbose_name='Equipe')

    def __str__(self):
        return self.projeto
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'











    