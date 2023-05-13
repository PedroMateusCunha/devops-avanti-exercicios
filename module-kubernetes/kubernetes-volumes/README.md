# Exercícios 1

---
**Requisitos**

- Volte ao exercício cep-python-flask usado na revisão sobre e Docker e Docker-Compose e:
    1. inclua um trecho de código que salva um arquivo CSV sempre que o list_csv for utilizado;
    1. salve o arquivo criado em um volume;
    1. crie um novo container que mapeie o mesmo volume e mostre o seu conteúdo no log a cada 5 min;
    1. crie um novo container que mapeie o mesmo volume e transforme o CSV em um JSON ou um YAML e mostre o conteúdo no log.
- Teste cada uma das condições, salve prints, arquive.
---

### Considerações:

O código cep-python-flask foi originalmente desenvolvido pelo professor Cicero Woshington. Onde fiz alterações no código para solucionar o exercício proposto.

### Descrição da Abordagem:

Neste exercício foram criados os manifestos necessários para subir a aplicação cep-python-flask com kubernetes. Ambos os microsserviços estão fazendo uso da imagem base que está no Docker Hub. Também foi adicionada uma nova funcionalidade na aplicação cep_python_flask para que possa salvar a lista de ceps pesquisados em CSV e JSON. O foco desse exercício é demonstrar o uso de volumes entre 1 ou mais containers. Então, dessa forma, os novos dois containers de log-csv e log-json foram adicionamos no mesmo POD Kubernetes.

### Pré-requisitos para o ambiente

É necessário que tenha exista a imagem base no seu Docker Hub privado de acordo com o script de build-n-deploy na seção dos módulos Docker.

### Build da imagem:

A etapa de build da imagem base pode ser realizada ao executar o script de `build-n-push.sh` em um novo terminal. Mas antes precisaremos definir uma variável de ambiente com o seu usuário do Docker Hub.

```bash
export DOCKER_HUB_USER=<INSIRA_AQUI_SEU_USUÁRIO>
```

Agora que temos uma variável definida, podemos executar o build e push da imagem:

```bash
bash build-n-push.sh
```

### Execução da aplicação:

Para subir essa stack, basta executar em seu terminal preferido, no mesmo diretório do arquivo docker-compose.yml:

```bash
kubectl apply -f kubernetes/
```

Agora que nossa stack está de pé, podemos então realizar algumas pesquisas para popular o arquivo csv. Então para facilitar, podemos executar o script de pesquisa de cep.

```bash
bash pesquisa.sh
```

### Acessando a aplicação:

- Host: 192.168.49.2 (IP do Minikube)
- Porta: 5000
- URL: http://192.168.49.2:5000

Para conseguir acessar a aplicação, basta acessar alguma das rotas abaixo:

| Método HTTP | Rota | Descrição |
|-------------|------|-----------|
| `GET` | / | exibe mensagem de uso da aplicação |
| `GET` | /quest/<postal_code> | encaminha a requisição para o módulo Quest |
| `GET` | /list_csv | solicita uma lista em formato CSV |
| `GET` | /list_html | solicita uma lista em formato HTML |
| `GET` | /search_html/<postal_code> |  pesquisa um código postal específico na lista e retorna em formato HTML |

### Verificando os logs:
Para conseguir visualizar os logs é necessário especificar o namespace, o nome do pod e log após o container. Tudo isso ficaria no formato:

`kubectl -n <namespace> logs -f pods/<nome-do-pod-hash> <nome-do-container>`

Então para esse exemplo, o nome do nosso pod será `cep-python-list-csv-6b97698655-4mq77`

##### Logs em CSV:
```bash
kubectl -n cep logs -f pods/cep-python-list-csv-6b97698655-4mq77 csv-logs
```
##### Logs em JSON
```bash
kubectl -n cep logs -f pods/cep-python-list-csv-6b97698655-4mq77 json-logs
```

### Verificando o status:

Para verificar se todos os serviços estão rodando, podemos executar:

```bash
kubectl -n cep get po,svc,cm,svc,secret
```
