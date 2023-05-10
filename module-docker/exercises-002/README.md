# Exercícios 2

---
**Requisitos**

- Continuando o exercício anterior, crie um arquivo com o formato:
    ```bash
    main=v1.0.0
    quest=v1.0.1
    keep=v1.0.2
    list_csv=v1.0.3
    list_html=v1.0.4
    ```
- Modifique o script de build para usar essa informação ao criar as imagens. Essa informação deve aparecer em uma label da imagem e na própria tag. Todos também precisam usar a tag latest. 
- Teste cada uma das condições, salve prints, arquive.

---

### Considerações:

Esse código foi primeiramente desenvolvido pelo professor Cicero Woshington. Onde fiz alterações no código para solucionar o exercício proposto.

### Descrição da Abordagem:

Para solucionar esse exercício, em vez de criar 5 Dockerfiles para cada um dos microsserviços, optei em criar apenas um, como sendo o modelo base para os restantes, através do uso do comando `ENTRYPOINT`.

Neste exercício também foi criado um script capaz de realizar o build e push da imagem.

### Execução da aplicação:

A etapa de build da imagem base pode ser realizada ao executar o script de `build-versions.sh` em um novo terminal. Mas antes precisaremos criar um arquivo `versions.txt` com essas versões, então para isso, execute:

```bash
echo "main=v1.0.0" > versions.txt && \
echo "quest=v1.0.1" >> versions.txt && \
echo "keep=v1.0.2" >> versions.txt &&\
echo "list_csv=v1.0.3" >> versions.txt &&\
echo "list_html=v1.0.4" >> versions.txt 

```

Agora que já temos um arquivo de versões, podemos executar o build das imagens:

```bash
bash build-versions.sh
```

### Verificando os metadados

Para verificarmos os metadados dessa imagem, podemos inspecionar as labels através do comando:

```bash
docker image inspect --format '{{json .Config.Labels}}' list_html:latest
```