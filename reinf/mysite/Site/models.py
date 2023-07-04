from django.contrib.auth.models import User

from django.db import models

# Create your models here.
    
    
class Empresa(models.Model):
    cod_empresa = models.AutoField(primary_key=True)
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

class GrpEmpresa(models.Model):
    grp_empresa = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'grp_empresa'
        
def __str__(self):
    return self.Grp_empresa

class Enderecos(models.Model):
    cod_empresa = models.IntegerField(primary_key=True) 
    seq = models.IntegerField()
    endereco = models.CharField(max_length=70, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cod_municipio = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='cod_municipio', blank=True, null=True)    
    uf = models.ForeignKey('Uf', models.DO_NOTHING, db_column='uf', blank=True, null=True)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    ie = models.CharField(max_length=18, blank=True, null=True)
    im = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enderecos'
        unique_together = (('cod_empresa', 'seq'),)





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

class usuario(models.Model): 
    cod_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Id_Usuario', null=False, blank=False)
    cod_empresa = models.OneToOneField(Empresa, models.DO_NOTHING, db_column='cod_empresa', primary_key=True, related_name='Id_Empresa') 
    nome        = models.CharField(max_length=60, blank=True, null=True)
    email       = models.CharField(max_length=60, blank=True, null=True)
    telefone    = models.CharField(max_length=13, blank=True, null=True)
    celular     = models.CharField(max_length=13, blank=True, null=True)

    
    #senha = models.CharField(max_length=8, null=False, blank=False)
    
    class Meta:
        managed = True  
        db_table = 'usuario'
        unique_together = (('cod_empresa', 'cod_usuario'),)

    def __str__(self):
        return self.usuario
    
    class imagem(models.Model):
        imagem = models.ImageField(upload_to='img/')