from django.shortcuts import render, redirect
from .models import Veiculo, Cliente
from django.http import HttpResponseBadRequest

def index(request):
   return render(request, "Página-Inicial.html", {})

def cadastro(request):
   if request.method == "GET":
      return render(request, "cadastro.html", {})

   if request.method == "POST":
      nome = request.POST.get('nome')
      telefone = request.POST.get('telefone')
      tipo_veiculo = request.POST.get('select')
      placa = request.POST.get('placa')
      rua = request.POST.get('street')
      numero = request.POST.get('text')
      cidade = request.POST.get('city')
      veiculo = Veiculo.objects.filter(placa=placa)

      if veiculo.exists():
         return HttpResponseBadRequest("este veiculo já esta cadastrado. Consulte o admin para mudanças.")
      else:
         cliente = Cliente.objects.create(
            nome=nome,
            telefone=telefone,
            rua=rua,
            numero=numero,
            cidade=cidade
         )
         
         veiculo = Veiculo.objects.create(
            tipo_veiculo=tipo_veiculo,
            placa=placa,
            cliente=cliente
         )
         
         return redirect('servicos:servicos')