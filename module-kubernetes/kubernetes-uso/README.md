# Exercícios 1

---
**Requisitos**

- Volte ao exercício cep-python-flask usado na revisão sobre e Python e:
    1. faça o ConfigMap e Secret com as variáveis de ambiente;
    1. crie os Deployments e Services para cada microsserviço;
    1. aplique os manifestos ao seu cluster;
    1. exponha o Service do módulo main;
    1. verifique se os serviços funcionam.
- Teste cada uma das condições, salve prints, arquive.

---

### Considerações:

O código cep-python-flask foi originalmente desenvolvido pelo professor Cicero Woshington. Onde fiz alterações no código para solucionar o exercício proposto.

### Pré-requisitos para o ambiente

É necessário que tenha exista a imagem base no seu Docker Hub privado de acordo com o script de build-n-deploy na seção dos módulos Docker.

### Descrição da Abordagem:

Neste exercício foram criados os manifestos necessários para subir a aplicação cep-python-flask com kubernetes. Ambos os microsserviços estão fazendo uso da imagem base que está no Docker Hub.

### Execução da aplicação:

Para subir essa stack, basta executar em seu terminal preferido, no mesmo diretório do arquivo docker-compose.yml:

```bash
kubectl apply -f kubernetes/
```

### Acessando a aplicação:

- Host: 192.168.49.2 (IP do Minikube)
- Porta: 5000
- URL: http://localhost:5000

Para conseguir acessar a aplicação, basta acessar alguma das rotas abaixo:

| Método HTTP | Rota | Descrição |
|-------------|------|-----------|
| `GET` | / | exibe mensagem de uso da aplicação |
| `GET` | /quest/<postal_code> | encaminha a requisição para o módulo Quest |
| `GET` | /list_csv | solicita uma lista em formato CSV |
| `GET` | /list_html | solicita uma lista em formato HTML |
| `GET` | /search_csv/<postal_code> | pesquisa um código postal específico na lista e retorna em formato CSV |
| `GET` | /search_html/<postal_code> |  pesquisa um código postal específico na lista e retorna em formato HTML |

Lembrando que cada um dos microsserviços podem ser acessados separadamente ao fazer
a requisição diretamente na porta do microsserviço. Por exemplo, se quiser acessar o
microsserviço de ```search_csv```, basta trocar a porta: http://192.168.49.2:5005/search_csv/64260000

**Obs:** certifique-se de ter pesquisado pelo menos algum cep antes, caso queira usar o de Piripiri-PI, faça a requisição para: http://192.168.49.2:5000/quest/64260000

### Verificando o status:

Para verificar se todos os serviços estão rodando, podemos executar:

```bash
kubectl -n cep get po,svc,cm,svc,secret
```
