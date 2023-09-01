from django.db import models
    
class Cliente(models.Model):
    nome = models.CharField(max_length=30, db_column="nome")
    telefone = models.CharField(max_length=15, db_column="telefone")
    rua = models.CharField(max_length=50, db_column="rua", null=True)
    numero = models.PositiveSmallIntegerField(db_column="numero", null=True)
    cidade = models.CharField(max_length=20, db_column="cidade", default="Imperatriz")
    
    
    
    def __str__(self):
        return "(%s, %s)" % (self.nome, self.telefone)
    
class Veiculo(models.Model):
    
    tipos_de_veiculos = [
        ("CRP", "Carro de passeio"),
        ("CMT", "Camionete"),
        ("MT", "Moto"),
    ]
    tipo_veiculo = models.CharField(max_length=3, default="CRP", choices=tipos_de_veiculos, db_column="tipo_veiculo")
    placa = models.CharField(max_length=8, db_column="placa")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return "(%s, %s)" % (self.placa, self.tipo_veiculo)