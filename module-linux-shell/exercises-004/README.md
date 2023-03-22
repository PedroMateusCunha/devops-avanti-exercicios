# Exercícios 4

---

### Criação do ambiente de testes
Primeiramente é necessário a configuração do ambiente de testes. Neste caso iremos instalar o serviço de ssh através do openssh na própria máquina do usuário. Além disso o script irá manter uma conexão ssh aberto, então feche o terminal somente após os testes.

Para configurar o ambiente execute em um terminal:

```bash
sudo bash install-env.sh
```
Note que será necessário inserir a senha de usuário para acessar a máquina. Caso já tenha o ssh configurado, acesse da maneira que preferir.

---

### Testando a aplicação
Para testar a aplicação basta executar em um outro terminal:

```bash
bash exercises-004.sh
```
