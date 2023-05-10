# Exercícios 3

---
**Requisitos**

- Verifique o conteúdo do repositório de Craig Richards com exemplos Python (https://github.com/geekcomputers/Python ) e escolha um dos exemplos para:
    1. verificar com PyLint,
    1. resolver os problemas de estilo ou justificar a não alteração,
    1. escreva testes com PyTest.
- Recomendações: Binary_search.py, rock_paper_scissor_game.py, stack.py ou escolha outro ao seu gosto.
- Realize os testes necessários, execute as principais condições, salve prints, arquive.

---

### Considerações:

Esse código foi primeiramente desenvolvido por Craig Richards. Onde fiz alterações no código para solucionar o exercício proposto.

### Descrição da Abordagem:

Neste exercício foram desenvolvidos dois testes para o microsserviço search_csv. Onde o primeiro realiza um teste ao pesquisar um cep já existente na base de dados e o outro realiza o teste de um cep vazio.

### Preparação do ambiente:

Primeiramente teremos que buildar a imagem que terá os requisitos necessários para que os códigos rodem com sucesso. Abra um novo terminal e navega até o diretório raiz desse exercício e execute:

```bash
docker build -t binary_search .
```

### Execução da aplicação:

Para executar essa aplicação, basta executar em seu terminal preferido, no diretório raiz da aplicação:

```bash
docker run -it binary_search binary_search.py
```
ou
```bash
docker run -it binary_search Binary_search.py
```
E seguir as instruções para realizar a busca binária em uma lista.

### Verificando o estilo de código com pylint:

Para realizar essa verificação, utilizaremos o comando docker run no arquivo original, nomeado como `Binary_search.py`. Então, execute em um terminal:

```bash
docker run -it --entrypoint="" binary_search pylint Binary_search.py
```
A saída deverá mostrar uma nota de 0 à 10 para o estilo do código. Exemplo:

```bash
************* Module Binary_search
Binary_search.py:39:0: C0304: Final newline missing (missing-final-newline)
Binary_search.py:1:0: C0114: Missing module docstring (missing-module-docstring)
Binary_search.py:1:0: C0103: Module name "Binary_search" doesn't conform to snake_case naming style (invalid-name)
Binary_search.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
Binary_search.py:3:23: C0103: Argument name "l" doesn't conform to snake_case naming style (invalid-name)
Binary_search.py:3:26: C0103: Argument name "r" doesn't conform to snake_case naming style (invalid-name)
Binary_search.py:3:29: C0103: Argument name "x" doesn't conform to snake_case naming style (invalid-name)
Binary_search.py:3:18: W0621: Redefining name 'arr' from outer scope (line 27) (redefined-outer-name)
Binary_search.py:3:29: W0621: Redefining name 'x' from outer scope (line 30) (redefined-outer-name)
Binary_search.py:12:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
Binary_search.py:37:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

-----------------------------------
Your code has been rated at 3.12/10
```

Dessa forma, podemos agora executar no código com o estilo refatorado, nomeado como `binary_search.py`:

```bash
docker run -it --entrypoint="" binary_search pylint binary_search.py
```
A saída esperado é algo parecido com:

```bash
************* Module binary_search
binary_search.py:45:0: C0301: Line too long (127/100) (line-too-long)

-----------------------------------
Your code has been rated at 9.38/10
```

### Realizando testes:

Foram realizados sete testes. O primeiro testa se o elemento está presente no array, o segundo testa se o elemento não está presente, o terceiro testa um array com apenas um elemento, o quarto testa um array vazio, o quinto testa um array com múltiplos elementos em que o elemento a ser procurado não está presente, o sexto testa um array grande e o sétimo testa um array com números negativos. Todos os testes são realizados usando a função "binary_search" e um ou mais casos de entrada e saída esperados são fornecidos para validar a função.

```bash
docker run -it --entrypoint="" binary_search pytest -v
```

A saída deverá mostrar uma lista com os resultados dos testes.