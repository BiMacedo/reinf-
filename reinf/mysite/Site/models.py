from django.contrib.auth.models import User

from django.db import models

# Create your models here.
    
class Empresa(models.Model):
    cod_empresa = models.CharField(primary_key=True, max_length=10)
    cnpj = models.CharField(max_length=14)
    razao = models.CharField(max_length=120, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    ie = models.CharField(max_length=13, blank=True, null=True)
    im = models.CharField(max_length=13, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    matriz = models.BooleanField(blank=True, null=True)
    crt = models.CharField(max_length=1, blank=True, null=True)
    cnae = models.CharField(max_length=7, blank=True, null=True)
    iest = models.CharField(max_length=18, blank=True, null=True)
    suframa = models.CharField(max_length=10, blank=True, null=True)
    grp_empresa = models.ForeignKey('GrpEmpresa', models.DO_NOTHING, db_column='grp_empresa', blank=True, null=True)
    chave_acesso = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'
      
    def __str__(self):
        return self.razao


class Enderecos(models.Model):
    cod_empresa = models.IntegerField(blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=70, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cod_municipio = models.IntegerField(blank=True, null=True)
    uf = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    ie = models.CharField(max_length=18, blank=True, null=True)
    im = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enderecos'


class GrpEmpresa(models.Model):
    grp_empresa = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'grp_empresa'
        
    def __str__(self):
        return self.grp_empresa


class Municipios(models.Model):
    cod_municipio = models.CharField(primary_key=True, max_length=7)
    municipio = models.CharField(max_length=35, blank=True, null=True)
    uf = models.ForeignKey('Uf', models.DO_NOTHING, db_column='uf', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipios'


class Uf(models.Model):
    uf = models.CharField(primary_key=True, max_length=2)
    cod_ibge = models.CharField(max_length=2, blank=True, null=True)
    nome = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uf'


class usuarios(models.Model):
    cod_usuario = models.IntegerField(primary_key=True)
    cod_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='cod_empresa',blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    celular = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
    
    def __str__(self):
        return self.nome
    
    class imagem(models.Model):
        imagem = models.ImageField(upload_to='img/')
        