# import math

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Projeto, Amostra, Placa

# @receiver(post_save, sender=Projeto)
# def gerar_placas_e_amostras(sender, instance, created, **kwargs):
#     if created and instance.qt_amostras:
#         # 1. Calcular a quantidade de placas necessárias
#         qt_placas = math.ceil(instance.qt_amostras / 96)

#         # 2. Criar as placas
#         Placa.objects.bulk_create([
#             Placa(id_projeto=instance, tamanho_placa='96') for _ in range(qt_placas)
#         ])

#         # 3. Criar as amostras (sem associar às placas)
#         Amostra.objects.bulk_create([
#             Amostra(id_projeto=instance, numero=i+1) for i in range(instance.qt_amostras)
#         ])

#         instance.amostras_geradas = True
#         instance.save()


#         # 4. Criar as posições para cada amostra, distribuindo em formato de matriz
#         posicoes = []
#         for i, amostra in enumerate(qt.amostra):
#             placa = placas[i // 96]  # Encontra a placa correspondente
#             linha = (i % 96) // 8 + 1  # Calcula a linha (1 a 12)
#             coluna = (i % 96) % 8 + 1   # Calcula a coluna (1 a 8)
#             posicoes.append(Posicao(id_amostra=amostra, id_placa=placa, coordenada_x=linha, coordenada_y=coluna))

#         Posicao.objects.bulk_create(posicoes)

#         instance.amostras_geradas = True
#         instance.save()

import math

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Projeto, Amostra, Placa, Posicao

@receiver(post_save, sender=Projeto)
def gerar_placas_amostras_e_posicoes(sender, instance, created, **kwargs):
    if created and instance.qt_amostras:
        # 1. Calcular a quantidade de placas necessárias
        qt_placas = math.ceil(instance.qt_amostras / 96)

        # 2. Criar as placas
        placas = Placa.objects.bulk_create([
            Placa(id_projeto=instance, tamanho_placa='96', placa_numero=i + 1) for i in range(qt_placas)
        ])

        # 3. Criar as amostras com nro_amostra sequencial
        amostras = Amostra.objects.bulk_create([
            Amostra(id_projeto=instance, amostra_numero=i + 1) for i in range(instance.qt_amostras)
        ])

        # 4. Criar as posições para cada amostra, distribuindo em formato de matriz
        posicoes = []
        for i, amostra in enumerate(amostras):
            placa = placas[i // 96]  # Encontra a placa correspondente
            linha = (i % 96) // 8 + 1  # Calcula a linha (1 a 12)
            coluna = (i % 96) % 8 + 1   # Calcula a coluna (1 a 8)
            posicoes.append(Posicao(id_amostra=amostra, id_placa=placa, coordenada_x=linha, coordenada_y=coluna))

        Posicao.objects.bulk_create(posicoes)

        instance.amostras_geradas = True
        instance.save()

