# Exercícios 2

---

### Criação do ambiente de testes
Primeiramente é necessário a configuração do ambiente de testes. Neste caso iremos criar um grupo chamado `avanti-teste` e um usuário `user-teste` que vai fazer parte desse grupo. Para configurar o ambiente execute em um terminal:

```bash
sudo bash install-env.sh
```

---

### Testando a aplicação
Para testar a aplicação basta executar em um terminal:

```bash
sudo bash exercises-002.sh
```

Note que não passamos nenhuma opção ou parâmetro para o código, logo, ele irá selecionar o usuário que executou o código, nesse caso, como estamos utilizando sudo, o usuário será o root. 

Existe a possibilidade de selecionar um usuário diretamente, apenas passando como parâmetro para o script.

```bash
sudo bash exercises-002.sh $USER
```
ou

```bash
sudo bash exercises-002.sh user-teste
```

---

### Limpando o Ambiente
Para limpar o ambiente, basta executar o seguinte código:

```bash
sudo bash uninstall.sh
```
Esse script irá remover o grupo  e usuário que foram criados.
