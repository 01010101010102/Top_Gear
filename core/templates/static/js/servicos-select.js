function atualizarValorServico(caixaSelecao) {
    const elementoValorServico = document.getElementById('valor-servico-input');
    let valorTotal = 0;
    let servicosSelecionados = [];
    
    const caixasSelecao = document.querySelectorAll('input[name="checkbox[]"]:checked');
    caixasSelecao.forEach(function(caixaSelecao) {
      const valor = parseFloat(caixaSelecao.getAttribute('data-value'));
      valorTotal += valor;
      servicosSelecionados.push(caixaSelecao.getAttribute('data-calc'));
    });
    
    // Verificar combinações inválidas
    const servicoGeral = servicosSelecionados.includes('LG');
    const servicoMeiaSola = servicosSelecionados.includes('ML');
    const servicoPintura = servicosSelecionados.includes('PTR');
    const servicoAspiracao = servicosSelecionados.includes('APR');
    
    if ((servicoGeral && servicoMeiaSola) || (servicoGeral && servicoAspiracao) || (servicoGeral && servicoPintura) || (servicoMeiaSola && servicoPintura)) {
      alert('Você não pode selecionar Geral, Meia Sola e Pintura juntos. A aspiração e o enceramento é gratis quando voçê escolhe a Geral!');
      caixaSelecao.checked = false;
      return;
    }

    // Se a opção 'Motor' estiver selecionada, adicione um valor adicional
    const caixaSelecaoMotor = document.querySelector('input[data-calc="MTR"]:checked');
    if (caixaSelecaoMotor) {
      valorTotal += 20; // Adicione o valor desejado aqui
    }

    elementoValorServico.value = valorTotal.toFixed(2); // Exibir o valor total

    
  }