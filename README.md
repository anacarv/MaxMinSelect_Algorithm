# Algorítmo MaxMinSelect

## Sobre o Projeto

Este projeto implementa o **Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select)**, utilizando a abordagem de 
divisão e conquista. O objetivo é reduzir o número de comparações em relação a abordagens mais ingênuas e analisar a sua complexidade 
computacional.

## Como funciona o algoritmo?

O algoritmo **MaxMin Select** divide a lista em duas partes e resolve cada uma recursivamente, retornando os valores mínimo e máximo. Em seguida, combina os resultados para obter os elementos mínimo e máximo da lista original.

### Passos do Algoritmo:

1. **Caso base:** Se houver apenas um elemento, ele é tanto o menor quanto o maior.

2. **Caso de dois elementos:** Comparação direta para determinar o menor e o maior.

3. **Divisão e Conquista:**
   - Divide o array ao meio.
   - Resolve recursivamente para cada metade.
   - Combina os resultados retornando o menor dos mínimos e o maior dos máximos.

## Como executar o projeto

### Pré-requisitos

Este projeto requer **Python 3.x** e **Git** instalados, e ele **não exige a instalação de nenhuma dependência adicional**

### Rodando o código

1. Clone este repositório:
   ```sh
   git clone https://github.com/anacarv/MaxMinSelect_Algorithm
   cd maxmin_select
   ```
2. Execute o script:
   ```sh
   python main.py
   ```
3. Digite uma lista de números inteiros quando solicitado e dê enter para ver o resultado.

## Análise da Complexidade

### Complexidade Assintótica

#### Método de Contagem de Operações

O algoritmo **MaxMin Select** reduz o número de comparações em relação à abordagem ingênua. Para calcular a quantidade de comparações feitas em cada etapa, analisamos a estrutura do algoritmo:

- A cada passo, o problema é dividido em dois subproblemas de tamanho `n/2`.
- Cada subproblema encontra os valores mínimo e máximo separadamente.
- Após resolver as duas metades, fazemos apenas **duas comparações** para obter o mínimo e o máximo globais.

##### Contagem das Comparações

1. **Caso base:** Se `n = 1`, não há comparações, pois há apenas um elemento.
2. **Caso com dois elementos (`n = 2`)**: Apenas **uma comparação** é necessária.
3. **Caso geral (`n > 2`)**:
   - O array é dividido em duas partes de tamanho `n/2`.
   - Cada subproblema executa a mesma operação recursivamente.
   - Após obter os mínimos e máximos das duas metades, realizamos **duas comparações** adicionais.

Seja `C(n)` o número total de comparações:
```
C(n) = C(n/2) + C(n/2) + 2
```
Expandindo a recorrência:
```
C(n) = 2C(n/2) + 2
C(n/2) = 2C(n/4) + 2
C(n/4) = 2C(n/8) + 2
...
```
Após `log_2(n)` divisões, atingimos `n = 1` e paramos a recursão. Somando todas as comparações:
```
C(n) ≈ 3n/2 - 2
```
Portanto, a complexidade total de comparações é **O(n)**, pois a função cresce linearmente com `n`.

Essa abordagem é mais eficiente que a comparação ingênua, que precisaria de `2(n-1)` comparações.

#### Aplicação do Teorema Mestre

A recorrência do problema é definida como:
```math
T(n) = 2T(n/2) + O(1)
```
Para resolver essa recorrência, identificamos os valores:
- `a = 2` (duas chamadas recursivas),
- `b = 2` (divisão do problema pela metade a cada passo),
- `f(n) = O(1)` (operações constantes para cada divisão e combinação).

Agora aplicamos o **Teorema Mestre**, que se baseia na fórmula geral:
```math
T(n) = aT(n/b) + f(n)
```
Para determinar a complexidade, calculamos:
- `log_b(a) = log_2(2) = 1`.
- `f(n) = O(1)` é menor que `O(n^p)` para `p = 1`.
- Pelo **caso 2 do Teorema Mestre**, concluímos que:
  ```math
  T(n) = O(n)
  ```

## Exemplo de Entrada e Saída

```
Digite uma lista de números inteiros separados por espaço: 3 1 7 9 2 8 4 6
Lista de entrada: [3, 1, 7, 9, 2, 8, 4, 6]
Menor elemento: 1, Maior elemento: 9
```