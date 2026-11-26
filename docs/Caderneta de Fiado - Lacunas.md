---
tipo: lacunas
projeto: "[[Caderneta de Fiado]]"
criado: 2026-11-26
tags: [projeto, lacunas]
---
# Lacunas

Ligado a: [[Trilha - Caderneta de Fiado]] · [[Caderneta de Fiado - Requisitos]]

> Perguntas que ainda não têm resposta e que afetam o sistema. Quando respondida, a lacuna vai para "Respondidas", com a resposta e a nota onde foi aplicada.

**Gravidade**
- **Alta:** precisa de resposta antes de desenhar as telas.
- **Média:** precisa de resposta antes de escrever o código daquela parte.
- **Baixa:** precisa de resposta antes de publicar.

## Abertas
| # | Pergunta | Gravidade | Por que importa |
|---|---|---|---|
| | Nenhuma em aberto em 26/11/2026. | | |

## Respondidas
| Pergunta | Resposta | Onde foi aplicada |
|---|---|---|
| L01. Compra descoberta depois do fechamento entra como compra com data antiga ou como ajuste? | Ajuste na semana aberta, do tipo "fora do período", com a data real no campo data de referência. Semana fechada não se reabre: faz-se da forma menos danosa para o conjunto. | Requisitos: RF28, RN13 |
| L02. Um ajuste pode ser editado ou excluído? | Pode, porque quem anota e quem digita erra. Pede senha master, e a exclusão exige motivo. Ajuste de semana fechada não se mexe: corrige-se com novo ajuste. | Requisitos: RF39, RF40, RN05, RNF01 |
| L03. O RF19 conta os clientes acima do limite ou os bloqueados? | Os dois, em números separados: acima do limite mostra o risco, bloqueados mostra para quem o balcão não vende. | Requisitos: RF19, RF32 |
| L04. Os 70% para liberar o bloqueado são calculados sobre o quê? | Sobre a dívida no momento do pagamento, não sobre o passado. E o saldo que sobra precisa ficar dentro do limite. | Requisitos: RN08 |
| L05. Dá para bloquear ou desbloquear um cliente na mão? | Sim, analisando caso a caso, sempre com motivo, para saber por que se tomou a decisão. | Requisitos: RF33, RF34, RNF01 |
| L06. Depois de um desbloqueio manual, o sistema volta a bloquear sozinho? | Não. A condição manual vale até eu retirar: o sistema entende como condição especial daquele cliente. | Requisitos: RN10, RF35 |
| L07. O que acontece se eu esquecer a senha master? | Código de recuperação, gerado ao criar a senha e guardado fora do computador. Recuperação por e-mail fica fora do escopo. | Requisitos: RF36, Fora do escopo |
| L08. O que é uma semana para o sistema? | Começa no domingo e termina no sábado. Se eu pular um sábado, são dois fechamentos, feitos em ordem. | Requisitos: RN11, RN12 |
| L09. Como encontro o cliente certo quando há nomes iguais? | Pelo número, pelo nome ou pelo apelido. Cada cliente ganha um número único, impresso na ficha. | Requisitos: RF37, RF38, RF22 |
| L10. Se a conta da semana não bater, o sistema fecha mesmo assim? | Não deixa fechar: avisa a diferença e a semana continua aberta. | Requisitos: RN14 · Fluxogramas: 5 |
