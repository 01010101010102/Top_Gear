from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import urllib

from .models import Servicos
from clientes.models import Veiculo

def testepg(request):
  return render(request, "servicos/servico-PI-camionete.html")

def servicos(request):
  
  global placa_req
  global tipo_veiculo

  if request.method == "GET":
    placa_req = request.GET.get('text') 
    # Verifica se o usuário está logado antes de prosseguir
    if placa_req:
      try:
        cliente = get_object_or_404(Veiculo, placa=placa_req)
        tipo_veiculo = cliente.tipo_veiculo
      except Veiculo.DoesNotExist:
        return HttpResponse("Placa inválida")
      else:
        # Mapeamento de tipos de veículo para templates correspondentes
        tipo_template = {
          "CRP": "servicos/servico-Página-Inicial.html",
          "CMT": "servicos/servico-PI-camionete.html",
          "MT": "servicos/servico-PI-moto.html",
        }
        template = tipo_template.get(tipo_veiculo, "servicos/servico-Login.html")
        return render(request, template, {})
    
    return render(request, "servicos/servico-Login.html", {})
     
  elif request.method == "POST": 
    veiculo = get_object_or_404(Veiculo, placa=placa_req)
    data = timezone.localtime(timezone.now())
    aviso = request.POST.get('textarea')
    servicos = request.POST.getlist('checkbox[]')
    valor_total = calcula_valor(servicos, tipo_veiculo)
    
    separador = ", "
    serv = separador.join(servicos)
    
    servico = Servicos(escolha_servico=serv, aviso=aviso, data_inicio=data, veiculo=veiculo, valor_total=valor_total)
    servico.save() 
     
    return HttpResponseRedirect("confirmacao/", status=303)

  else:
    return HttpResponse("método inválido")
  
def confirmacao(request):
  if request.method == "GET":
    try:
      veiculo_cliente = Veiculo.objects.get(placa=placa_req)
      nome_cliente = veiculo_cliente.cliente.nome
      rua_cliente = veiculo_cliente.cliente.rua
      casa_cliente = veiculo_cliente.cliente.numero      
      ultimo_servico = Servicos.objects.filter(veiculo=veiculo_cliente).latest('data_inicio')
      ultimo_aviso = ultimo_servico.aviso
      escolha = ultimo_servico.escolha_servico
      
      if "DKB" in escolha.strip():
        mensagem = enviar_msg_com_DKB(placa_req, nome_cliente, escolha, ultimo_aviso, rua_cliente, casa_cliente)
      else:
        mensagem = enviar_msg(placa_req, nome_cliente, escolha, ultimo_aviso)
    except (Veiculo.DoesNotExist and Servicos.DoesNotExist):
      return HttpResponse("BO")

    return render(request, "servicos/servico-confirmação.html", {'zap': mensagem} )
  
def enviar_msg(placa, nome, servicos, aviso):
  tipo_servico = {
    "LG": "Lavagem Geral",
    "ML": "Meia Sola",
    "PTR": "Pintura",
    "MTR": "Motor",
    "APR": "Aspiração"
  }
  servicos_completos = ', '.join([tipo_servico[servico] for servico in servicos.split(', ')])
  texto = f"-------\nplaca:{placa}.\nnome:{nome}.\nservico:{servicos_completos}.\naviso:{aviso}.\n----------\n"  
  msg = urllib.parse.quote(texto)  
  mensagem_zap = f"https://wa.me/559992010132?text={msg}"
  
  return mensagem_zap

def enviar_msg_com_DKB(placa, nome, servicos, aviso, rua, numero):
  tipo_servico = {
    "LG": "Lavagem Geral",
    "ML": "Meia Sola",
    "PTR": "Pintura",
    "MTR": "Motor",
    "APR": "Aspiração",
    "DKB": "Disk Busca"
  }
  servicos_completos = ', '.join([tipo_servico[servico] for servico in servicos.split(', ')])
  texto = f"-------\nplaca:{placa}.\nnome:{nome}.\nservico:{servicos_completos}.\naviso:{aviso}.\n\n\nVou querer o Disck Busca\nRua:{rua}.\n Número da residência:{numero}\n\n----------\n"  
  msg = urllib.parse.quote(texto)  
  mensagem_zap = f"https://wa.me/559992010132?text={msg}"
  
  return mensagem_zap

def calcula_valor(servicos, tipo_veic):
  preco_total = 0.0
  Carro = {'LG': 50.0, 'ML': 40.0, 'MTR': 20.0, 'APR': 20.0}
  Camionete = {'LG': 60.0, 'ML': 50.0, 'MTR': 20.0, 'APR': 20.0}
  Moto = {'LG': 20.0}
  
  if tipo_veic == "CRP":
    for servico in servicos:
      preco_total += Carro.get(servico, 0.0)
  elif tipo_veic == "CMT":
    for servico in servicos:
      preco_total += Camionete.get(servico, 0.0)
  elif tipo_veic == "MT":
    for servico in servicos:
      preco_total += Moto.get(servico, 0.0)
  
  return preco_total