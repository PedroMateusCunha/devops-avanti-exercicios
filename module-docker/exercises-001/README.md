# Exercícios 1

---
**Requisitos**

- Crie os Dockerfiles das aplicações usadas no estudo de Python. No caso, crie dos 5 microsserviços.
- Execute os testes baseados nos containers.
- Crie um script para rodar automaticamente todos os builds.
- Teste cada uma das condições, salve prints, arquive

---

### Considerações:

Esse código foi primeiramente desenvolvido pelo professor Cicero Woshington. Onde fiz alterações no código para solucionar o exercício proposto.

### Descrição da Abordagem:

Para solucionar esse exercício, em vez de criar 5 Dockerfiles para cada um dos microsserviços, optei em criar apenas um, como sendo o modelo base para os restantes, através do uso do comando `ENTRYPOINT`.

Neste exercício também foi criado um script capaz de realizar o build e push da imagem.

### Execução da aplicação:

A etapa de build da imagem base pode ser realizada ao executar o script de `build-n-push.sh` em um novo terminal. Mas antes precisaremos definir uma variável de ambiente com o seu usuário do Docker Hub.

```bash
export DOCKER_HUB_USER=<INSIRA_AQUI_SEU_USUÁRIO>
```

Agora que temos uma variável definida, podemos executar o build e push da imagem:

```bash
bash build-n-push.sh
```
