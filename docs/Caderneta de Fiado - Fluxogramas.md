---
tipo: fluxograma
projeto: "[[Caderneta de Fiado]]"
criado: 2026-11-26
tags: [projeto, fluxograma]
---
# Fluxogramas

Ligado a: [[Trilha - Caderneta de Fiado]] · [[Caderneta de Fiado - Requisitos]]

> Fluxograma = desenho do passo a passo de um processo. Retângulo é uma ação, losango é uma decisão (com saída "sim" e "não"), seta que volta é uma repetição.

## 1. Fechamento de sábado

Sugerido pelo Mentor e aprovado por mim em 26/11/2026.

```mermaid
flowchart TD
    A[Recolher as fichas no balcão] --> B[Pegar a próxima ficha]
    B --> C[Buscar o cliente pelo número]
    C --> D{A data é de semana já fechada?}
    D -- sim --> F[Lançar ajuste do tipo fora do período]
    D -- não --> E[Lançar compra ou pagamento]
    E --> G{Ainda há linhas ou fichas?}
    F --> G
    G -- sim --> B
    G -- não --> H[Fazer o fechamento da semana]
    H --> I[Imprimir todas as fichas]
    I --> J[Fechar o sistema: backup automático]
    J --> K[Devolver as fichas na segunda]
```

**De onde veio cada passo**
- Buscar o cliente pelo número: RF38
- Ajuste do tipo fora do período: RF28 e RN13
- Fechamento da semana: RF27
- Imprimir todas as fichas: RF25
- Backup automático ao fechar: RNF02

## 2. Situação do cliente: bloqueado ou liberado

Sugerido pelo Mentor em 26/11/2026, a partir da RN07, RN08 e RN10. Aprovado por mim em 26/11/2026.

```mermaid
flowchart TD
    A{"Tem condição manual?"}
    A -- "bloqueio manual" --> X["Bloqueado"]
    A -- "liberação manual" --> Y["Liberado"]
    A -- "não" --> C{"Já estava bloqueado?"}
    C -- "não" --> D{"Saldo acima do limite?"}
    D -- "sim" --> X
    D -- "não" --> Y
    C -- "sim" --> E{"O pagamento cobre 70% da dívida e o saldo que sobra fica dentro do limite?"}
    E -- "sim" --> Y
    E -- "não" --> X
```

## 3. Lançar um pagamento

Sugerido pelo Mentor em 26/11/2026, a partir do RF10, RF14, RN04 e RN09. Aprovado por mim em 26/11/2026.

```mermaid
flowchart TD
    A["Buscar o cliente"] --> B{"Cliente inativado?"}
    B -- "sim" --> C["Reativar o cliente"]
    C --> D["Informar data e valor"]
    B -- "não" --> D
    D --> E{"Valor maior que a dívida?"}
    E -- "não" --> G["Registrar o pagamento"]
    E -- "sim" --> F{"Crédito em conta ou erro de digitação?"}
    F -- "erro" --> D
    F -- "crédito" --> H["Registrar o pagamento: a sobra vira crédito em conta"]
    G --> I["Verificar a situação do cliente (fluxograma 2)"]
    H --> I
```

## 4. Corrigir um lançamento

Vale para compra, pagamento e ajuste. Sugerido pelo Mentor em 26/11/2026, a partir da RN05, RNF01, RF39 e RF40. Aprovado por mim em 26/11/2026.

```mermaid
flowchart TD
    A["Escolher o lançamento"] --> B{"É de semana fechada?"}
    B -- "sim" --> C["Não mexer: lançar um ajuste do tipo correção na semana aberta"]
    B -- "não" --> D["Pedir a senha master"]
    D --> E{"Senha correta?"}
    E -- "não" --> Z["Cancelar"]
    E -- "sim" --> F{"Editar ou excluir?"}
    F -- "excluir" --> G["Pedir o motivo"]
    G --> H["Aplicar a mudança e guardar o registro"]
    F -- "editar" --> H
```

## 5. Fazer o fechamento da semana

Sugerido pelo Mentor em 26/11/2026, a partir do RF27, RN06, RN11 e RN12. Aprovado por mim em 26/11/2026. Decidi em 26/11/2026 que, se a conta não bater, o sistema não deixa fechar (RN14).

```mermaid
flowchart TD
    A{"A semana anterior está fechada?"}
    A -- "não" --> B["Fechar a semana anterior primeiro"]
    A -- "sim" --> C["Somar vendido, recebido, ajustes e novos cadastros"]
    C --> D{"Início + vendido - recebido ± ajustes = fim?"}
    D -- "não" --> E["Avisar a diferença e não fechar"]
    D -- "sim" --> F["Guardar o retrato da semana"]
    F --> G["Travar os lançamentos da semana"]
```
