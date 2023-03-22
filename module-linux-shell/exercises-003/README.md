# Exercícios 3

---

### Criação do ambiente de testes
Primeiramente é necessário a configuração do ambiente de testes. Neste caso iremos criar um arquivo `config-teste.cfg` em `/tmp`, pois ao reiniciar o sistema essa pasta reseta todo o conteúdo.

```bash
sudo bash install-env.sh
```

---

### Testando a aplicação
Para testar a aplicação basta executar em um terminal:

```bash
bash exercises-003.sh
```

Note que não passamos nenhuma opção ou parâmetro para o código, logo, ele irá reclamar que é obrigatório indicar as opções e seus parametros respectivos como descrito na função de help.

Existe a possibilidade de selecionar um usuário diretamente, apenas passando como parâmetro para o script.

```bash
bash exercises-003.sh -f config-teste.cfg -k debug -v on
```

ou

```bash
bash exercises-003.sh -v off -f config-teste.cfg -k debug
```

---

### Limpando o Ambiente
Caso queira limpar o ambiente antes de reiniciar a máquina, basta executar o seguinte comando:

```bash
rm -rf /tmp/config-teste.cfg
```
