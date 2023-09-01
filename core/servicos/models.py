from django.db import models
from clientes.models import Veiculo


class Servicos(models.Model):
    

    escolha_servico = models.CharField(max_length=25, db_column="escolha_servico")
    aviso = models.CharField(max_length=60, db_column="aviso", null=True)
    data_inicio = models.DateTimeField()
    valor_total = models.FloatField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "(%s, %s, %s)" % (self.escolha_servico, self.aviso, self.data_inicio)
    
