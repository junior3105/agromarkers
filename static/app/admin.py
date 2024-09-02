from django.contrib import admin
from .models import Empresa, Projeto, Marcador, Status, Atividade, TipoResultado, Placa, Analise, Amostra, Posicao, Transferencia
from unfold.admin import ModelAdmin

# Registre seus modelos aqui

@admin.register(Empresa)
class CustomAdminClass(ModelAdmin):
    pass


# class EmpresaAdmin(admin.ModelAdmin):
#     fields = ('nro_empresa', 'nome')

# admin.site.register(Empresa, EmpresaAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    fields = ('id_empresa', 'nro_projeto', 'qt_amostras', 'amostras_geradas','ativo')
    list_display = ('id_empresa', 'nro_projeto', 'qt_amostras', 'amostras_geradas','ativo')
    list_filter = ('id_empresa', 'amostras_geradas', 'ativo')
    readonly_fields = ('amostras_geradas', 'ativo')
    

admin.site.register(Projeto, ProjetoAdmin)

admin.site.register(Marcador)
admin.site.register(Status)
admin.site.register(Atividade)
admin.site.register(TipoResultado)


class PlacaAdmin(admin.ModelAdmin):
    fields = ('id_projeto', 'tamanho_placa', 'processada')
    list_display = ('id_projeto', 'tamanho_placa','placa_numero', 'processada')
    list_filter = ('id_projeto', 'tamanho_placa', 'processada')


admin.site.register(Placa, PlacaAdmin)

admin.site.register(Analise)

class AmostraAdmin(admin.ModelAdmin):
    fields = ('id_projeto','amostra_numero')
    list_display = ('id_projeto','amostra_numero','id')
    list_filter = ('id_projeto',)
    readonly_fields = ('id_projeto','amostra_numero','id')

    
admin.site.register(Amostra, AmostraAdmin)

class PosicaoAdmin(admin.ModelAdmin):
    fields = ('id_amostra', 'id_placa', 'coordenada_x', 'coordenada_y')
    list_display = ('id_placa__id_projeto__id_empresa','id_placa__id_projeto','id_placa' ,'id_amostra', 'coordenada_x', 'coordenada_y')
    # list_filter = ('id_amostra')
    readonly_fields = ('id_amostra', 'id_placa', 'coordenada_x', 'coordenada_y')

    
admin.site.register(Posicao, PosicaoAdmin)
admin.site.register(Transferencia)
