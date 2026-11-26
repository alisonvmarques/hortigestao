---
tipo: requisitos
projeto: "[[Caderneta de Fiado]]"
criado: 2026-11-25
versao: 2
tags: [projeto, requisitos]
---
# Requisitos

Ligado a: [[Trilha - Caderneta de Fiado]] · [[Caderneta de Fiado - Visão]] · [[Caderneta de Fiado - Lacunas]]

> Um requisito por linha, cada um verificável, numerados em sequência. RF = requisito funcional (o que o sistema faz). RN = regra de negócio (o que ele obedece). RNF = requisito não funcional (como ele deve ser).

## Organização do sistema
| Área | Para que serve |
|---|---|
| Cadastro | Cadastrar e encontrar os clientes |
| Bloqueio | Bloquear e desbloquear clientes manualmente |
| Compras | Lançar as compras de cada cliente |
| Pagamentos | Lançar os pagamentos, totais ou parciais |
| Saldo | Verificar quanto cada um deve, com o detalhamento das movimentações |
| Ficha | Imprimir as fichas, uma ou todas de uma vez |
| Fechamento | Fazer o fechamento da semana, guardando o retrato dos números |
| Sistema | Cuidar dos dados: backup e senha master |

## Cadastro
- **RF01** O sistema permite cadastrar um cliente com nome e limite de crédito (obrigatórios) e, opcionais, apelido, CPF, endereço e telefone.
- **RF02** O sistema permite editar as informações do cadastro de um cliente.
- **RF03** O sistema guarda um registro de cada edição do cadastro, com o que mudou e quando.
- **RF04** O sistema permite inativar um cliente, sem apagar o cadastro nem as movimentações.
- **RF05** O sistema permite reativar um cliente inativado.
- **RF37** O sistema dá a cada cliente um número único, gerado automaticamente e nunca reaproveitado.
- **RF38** O sistema permite encontrar um cliente pelo número, pelo nome ou pelo apelido.

## Bloqueio
- **RF33** O sistema permite bloquear um cliente manualmente, com motivo obrigatório.
- **RF34** O sistema permite desbloquear um cliente manualmente, com motivo obrigatório.
- **RF35** O sistema permite retirar a condição manual de um cliente, que volta a seguir as regras automáticas.

## Compras
- **RF06** O sistema permite lançar uma compra para um cliente, com data e valor.
- **RF07** O sistema permite editar uma compra já lançada.
- **RF08** O sistema permite excluir uma compra lançada, exigindo um motivo.
- **RF09** O sistema guarda um registro de cada edição e exclusão de compra, com o que mudou, quando e, na exclusão, o motivo.

## Pagamentos
- **RF10** O sistema permite lançar um pagamento para um cliente, com data e valor.
- **RF11** O sistema permite editar um pagamento já lançado.
- **RF12** O sistema permite excluir um pagamento lançado, exigindo um motivo.
- **RF13** O sistema guarda um registro de cada edição e exclusão de pagamento, com o que mudou, quando e, na exclusão, o motivo.
- **RF14** Quando o pagamento é maior que a dívida, o sistema mostra um aviso perguntando se a diferença fica como crédito em conta ou se foi erro de digitação.

## Saldo
- **RF15** O sistema mostra a lista de clientes, com o nome e o saldo de cada um.
- **RF16** Ao selecionar um cliente, o sistema mostra os dados do cadastro, o limite, o saldo e todas as movimentações, cada uma com data e valor.
- **RF17** O sistema mostra o total a receber, que é a soma do que todos os clientes devem.
- **RF18** O sistema mostra a exposição, que é a soma dos limites de crédito de todos os clientes.
- **RF19** O sistema mostra quantos clientes estão acima do limite de crédito.
- **RF20** O sistema mostra o total de créditos em conta, que é a soma do que os clientes pagaram a mais.
- **RF31** O sistema mostra o total de perdas, que é a soma do saldo devedor dos clientes inativados.
- **RF32** O sistema mostra quantos clientes estão bloqueados.

## Ficha
- **RF21** A ficha impressa traz linhas em branco para anotar à mão as compras e os pagamentos da semana, com data e valor.
- **RF22** A ficha impressa traz o número, o nome e o apelido do cliente, o saldo atual e o limite de crédito.
- **RF23** A ficha impressa traz as 10 últimas movimentações, cada uma com data e valor.
- **RF24** O sistema permite imprimir a ficha de um cliente.
- **RF25** O sistema permite imprimir de uma vez as fichas de todos os clientes ativos.
- **RF26** A ficha do cliente bloqueado sai com um aviso grande em vermelho, em estilo marca d'água.

## Fechamento
- **RF27** O sistema permite fazer o fechamento da semana, guardando um retrato com: total vendido, total recebido, novos cadastros, a receber no início e a receber no fim da semana.
- **RF28** O sistema permite lançar um ajuste para um cliente, com tipo (correção ou fora do período), data, valor (para mais ou para menos) e motivo obrigatório. No tipo fora do período, a data de referência é obrigatória.
- **RF39** O sistema permite editar ou excluir um ajuste de semana aberta, exigindo um motivo na exclusão.
- **RF40** O sistema guarda um registro de cada edição e exclusão de ajuste, com o que mudou, quando e, na exclusão, o motivo.

## Sistema
- **RF29** O sistema permite fazer um backup manualmente.
- **RF30** O sistema permite restaurar os dados a partir de um backup, escolhendo qual das cópias usar.
- **RF36** Ao criar a senha master, o sistema gera um código de recuperação e o mostra uma única vez. Com o código, o usuário cria uma senha nova e o sistema gera outro código.

## Regras de negócio
- **RN01** O saldo do cliente é a soma das compras, menos os pagamentos, mais ou menos os ajustes.
- **RN02** Compra acima do limite de crédito é registrada normalmente.
- **RN03** Cliente inativado com saldo devedor conta como perda.
- **RN04** Cliente inativado não recebe lançamento; para receber dele, primeiro é reativado.
- **RN05** Compra, pagamento ou ajuste de semana fechada não pode ser editado nem excluído; a correção entra como novo ajuste na semana aberta.
- **RN06** No fechamento, a receber no início, mais o vendido, menos o recebido, mais ou menos os ajustes, é igual ao a receber no fim.
- **RN07** O cliente que passa do limite de crédito fica bloqueado. O sistema não trava a venda: o bloqueio aparece na ficha e quem deixa de vender é o balcão.
- **RN08** O cliente bloqueado é liberado quando um pagamento cobre no mínimo 70% da dívida daquele momento e o saldo que sobra fica dentro do limite.
- **RN09** Pagamento maior que a dívida, quando confirmado, deixa o cliente com crédito em conta. Na lista e na ficha, o crédito aparece por extenso ("Crédito: R$ 20,00"), nunca como saldo com sinal de menos.
- **RN10** Bloqueio ou desbloqueio manual prevalece sobre as regras automáticas até ser retirado pelo usuário.
- **RN11** A semana começa no domingo e termina no sábado. Cada lançamento pertence à semana da sua data.
- **RN12** Os fechamentos são feitos em ordem: não se fecha uma semana enquanto a anterior estiver aberta.
- **RN13** Compra ou pagamento descoberto depois do fechamento da sua semana entra como ajuste do tipo fora do período, na semana aberta. Semana fechada não se reabre.
- **RN14** O fechamento só é concluído se a conta da RN06 bater. Havendo diferença, o sistema avisa o valor e não fecha a semana.

## Requisitos de qualidade (ISO/IEC 25010)
Características da norma: adequação funcional · desempenho · compatibilidade · capacidade de interação · confiabilidade · segurança · manutenibilidade · flexibilidade · proteção (safety).

| Código | Característica | Requisito |
|---|---|---|
| RNF01 | Segurança | O sistema exige a senha master para editar ou excluir um lançamento (compra, pagamento ou ajuste), editar o cadastro (inclusive o limite), inativar um cliente, bloquear ou desbloquear manualmente e restaurar um backup. |
| RNF02 | Confiabilidade | O sistema faz um backup automático toda vez que é fechado e mantém as 7 cópias mais recentes, apagando a mais antiga. |
| RNF03 | Confiabilidade | Os backups ficam numa pasta sincronizada com a nuvem, fora do computador. |
| RNF04 | Capacidade de interação | Dá para digitar as movimentações de uma semana dos 60 clientes em até uma hora. |

## Fora do escopo
- Frente de caixa (PDV) e gestão completa da loja (ERP).
- Parte financeira do Pilão.
- Uso no balcão e aplicativo Android.
- Relatórios de evolução semana a semana (o retrato de cada semana já fica guardado para isso).
- Relatório completo de perdas, com a lista de clientes.
- Mais campos na compra, além de data e valor.
- Mais de um usuário.
- Recuperação da senha master por e-mail.
