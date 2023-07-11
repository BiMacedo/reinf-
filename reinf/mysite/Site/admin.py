from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import usuarios, Empresa, GrpEmpresa

# Register your models here.cl
class GrpEmpresaadmin(admin.ModelAdmin):
  list_display = ('grp_empresa',)
  search_fields = ['grp_empresa']
  
admin.site.register(GrpEmpresa, GrpEmpresaadmin)


class UsuarioAdmin(admin.ModelAdmin):
  list_display = ('nome',)
  search_fields = ['nome']
  
 # def get_queryset(self, request):
  # return super().get_queryset(request).filter()
  
admin.site.register(usuarios, UsuarioAdmin)


class EmpresaAdmin(admin.ModelAdmin):
  list_display = ('razao',)
  search_fields = ['razao']
  
admin.site.register(Empresa,EmpresaAdmin)





    