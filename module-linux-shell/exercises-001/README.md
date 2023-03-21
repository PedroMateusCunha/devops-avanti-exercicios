# Exercícios 1

---

### Criação do ambiente de testes
Primeiramente é necessário a configuração do ambiente de testes. Neste caso iremos utilizar a pasta `/tmp` para montar nosso ambiente de teste, pois ao reiniciar o sistema todo o conteúdo que está dentro dela é resetado.

Para configurar o ambiente execute em um terminal:

```bash
bash install-env.sh
```

Esse arquivo é responsável por criar exemplos simples de diretórios, arquivos, links e permissões.

---

### Testando a aplicação
Para testar a aplicação basta executar em um terminal:

```bash
sudo bash exercises-001.sh
```

Note que não passamos nenhuma opção ou parâmetro para o código, logo, ele irá selecionar o diretório de execução. 

Existe a possibilidade de selecionar o diretório alvo, apenas passando como parâmetro para o script.

```bash
sudo bash exercises-001.sh /tmp/diretorio-generico
```
ou

```bash
sudo bash exercises-001.sh /tmp/diretorio-generico-link
```

---

### Limpando o Ambiente
Caso queira limpar o ambiente antes de reiniciar a máquina, basta executar o seguinte comando:

```bash
rm -rf /tmp/diretorio-generico*
```
