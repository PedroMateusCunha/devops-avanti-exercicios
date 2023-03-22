# Exercícios 6

---

### Criação do ambiente de testes
Primeiramente é necessário a configuração do ambiente de testes. Neste caso iremos criar um arquivo `file-test.cfg` em `/tmp`, pois ao reiniciar o sistema essa pasta reseta todo o conteúdo.

```bash
bash install-env.sh
```

---

### Testando a aplicação
Para testar a aplicação basta executar em um terminal:

```bash
bash exercises-006.sh
```

Note que não passamos nenhuma opção ou parâmetro para o código, logo, ele irá reclamar que é obrigatório indicar as opções e seus parametros respectivos como descrito na função de help.

Existe a possibilidade de selecionar um arquivo diretamente, apenas passando como parâmetro para o script.

```bash
bash exercises-006.sh /tmp/file-test.cfg
```
---

### Limpando o Ambiente
Para limpar o ambiente, basta executar o seguinte código:

### Limpando o Ambiente
Caso queira limpar o ambiente antes de reiniciar a máquina, basta executar o seguinte comando:

```bash
rm -rf /tmp/file-test.cfg
```
