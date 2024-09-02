from django.db import models
# from django.db.models import JSONField

# Create your models here.


class Marcador(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    nome = models.CharField(max_length=50, help_text='Digite o nomme do marcador ou trait. Estar informação será mult empresa e projeto')  # Texto tamanho 50

    def __str__(self):
        return self.nome

class Status(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    nome = models.CharField(max_length=50, help_text='Digite o nomme do Status. Exemplo: ativo / inativo')

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    nome = models.CharField(max_length=50, help_text='Digite o nomme da atividade. Ex. Extrair, Centrifugar, ')  # Texto tamanho 50

    def __str__(self):
        return self.nome

class TipoResultado(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    nome = models.CharField(max_length=50, help_text='Digite o nomme do resultado. Ex. Positivo, Negativo, ')  # Texto tamanho 50

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    nro_empresa = models.PositiveIntegerField()  # Inteiro positivo 
    nome = models.CharField(max_length=50, blank=True, help_text='Digite o nome da nova empresa' )   # Texto tamanho 50

    def __str__(self):
        return f"Id: {self.id} - Empresa número : {self.nro_empresa} - Empresa nome: {self.nome}"

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  # Chave estrangeira para Empresa
    nro_projeto = models.PositiveIntegerField()  # Inteiro positivo
    qt_amostras = models.PositiveIntegerField(blank=True, null=True,)  # Inteiro positivo (opcional)
    amostras_geradas = models.BooleanField( default=True) # Inteiro
    ativo = models.BooleanField(default=True) # boolean

    def __str__(self):
        return f" Id: {self.id} - Projeto número: {self.nro_projeto}  |  total de {self.qt_amostras} amostras"

class Placa(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    tamanho_placa = models.CharField(max_length=20, choices=[('96','96'),('384','384'),('1536','1536')])
    placa_numero = models.PositiveIntegerField(default=0)
    processada = models.BooleanField(default=False)

    def __str__(self):
        return f"Id: {self.id} - Placa número: {self.placa_numero} - Tamanho da placa: {self.tamanho_placa}"

class Amostra(models.Model):
    id = models.AutoField(primary_key = True)
    amostra_numero = models.PositiveIntegerField(default=0)
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Id:  {self.id} - Amostra número: {self.amostra_numero}"

class Analise(models.Model):
    id = models.AutoField(primary_key=True)  # Índice automático
    id_placa = models.ForeignKey(Placa, on_delete=models.CASCADE)
    id_marcador = models.ForeignKey(Marcador, on_delete=models.CASCADE)
    id_resultado = models.ForeignKey(TipoResultado, on_delete=models.CASCADE)
    processada = models.BooleanField(default=False)

    def __str__(self):
        return f"Id: {self.id} - Placa número {self.id_placa.placa_numero} - Marcador {self.id_marcador} | Resultado {self.id_resultado.nome}"
    
class Posicao(models.Model):
    id = models.AutoField(primary_key=True)  # ��ndice automático
    id_amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE)
    id_placa = models.ForeignKey(Placa, on_delete=models.CASCADE)
    coordenada_x = models.FloatField()
    coordenada_y = models.FloatField()
    
    def __str__(self):
        return f"Id : {self.id} - Posição: X={self.coordenada_x} Y={self.coordenada_y}"

class Transferencia(models.Model):
    id = models.AutoField(primary_key=True)  # ��ndice automático
    id_placa_origem = models.ForeignKey(Placa, on_delete=models.CASCADE, related_name="Origem") #
    id_placa_destino = models.ForeignKey(Placa, on_delete=models.CASCADE, related_name="Destino")

    def __str__(self):
        return f" Empresa {self.id_placa_origem.id_projeto.id_empresa.nome} | Projeto {self.id_placa_origem.id_projeto.id} | Placa origem {self.id_placa_origem.id} | Placa Destino {self.id_placa_destino.id}"