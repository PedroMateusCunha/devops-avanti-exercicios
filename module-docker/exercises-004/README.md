# Exercícios 4

---
**Requisitos**

- Baseado no exercício de programação do repositório de Craig Richards com exemplos Python (https://github.com/geekcomputers/Python ) retorne ao exemplo que você usou e pense como você criaria um Dockerfile para ele.
- Se tiver dificuldade com o código que você escolheu, pode escolher outro. O importante aqui é fazer um Dockerfile desafiador, de um código que você conhece pouco.
- Teste cada uma das condições, salve prints, arquive.
---

### Considerações:

Esse código foi primeiramente desenvolvido por Craig Richards. Onde fiz alterações no código para solucionar o exercício proposto.

### Descrição da Abordagem:

Neste exercício foi construído um Dockerfile para o código binary_search.py.

### Preparação do ambiente:

Primeiramente teremos que buildar a imagem que terá os requisitos necessários para que os códigos rodem com sucesso. Abra um novo terminal e navega até o diretório raiz desse exercício e execute:

```bash
docker build -t binary_search .
```

### Execução da aplicação:

Para executar essa aplicação, basta executar em seu terminal preferido, no diretório raiz da aplicação:

```bash
docker run -it binary_search
```
E seguir as instruções para realizar a busca binária em uma lista.
