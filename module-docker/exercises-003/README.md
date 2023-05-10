# Exercícios 3

---
**Requisitos**

- Ainda baseado no exercício dos 5 microsserviços, crie um docker-compose.yaml que rode automaticamente a versão latest dos containers.
- Teste cada uma das condições, salve prints, arquive.

---

### Considerações:

Esse código foi primeiramente desenvolvido pelo professor Cicero Woshington. Onde fiz alterações no código para solucionar o exercício proposto.

### Descrição da Abordagem:

Neste exercício foi elabora um docker-compose.yml para rodar automaticamente a versão latest de cada um dos cinco microsserviços. Para que isso fosse possível, foi criado um serviço auxiliar, nomeado de base, que será o responsável por buildar a imagem que servirá de modelo para todos os outros serviços. A partir do momento em que a imagem está disponível, os serviços se baseiam nela e sobrescrevem através do uso de volumes os arquivos referentes aos seus respectivos serviços.

### Preparação do ambiente:

Certifique-se de ter no diretório raiz um arquivo nomeado como ```.env```. Nesse arquivo serão adicionadas as variáveis de ambiente necessárias para o código.

| Variável                       | Valor Padrão             | Descrição                                                  |
| ------------------------------| ------------------------| -----------------------------------------------------------|
| VIACEP_CONTAINER_NAME         | viacep.com.br            | Nome do container do ViaCEP                                 |
| VIACEP_CONTAINER_PORT         | 80                       | Porta do container do ViaCEP                                |
| VIACEP_CONTAINER_PROTOCOL     | http                     | Protocolo utilizado para acessar o container do ViaCEP       |
| MAIN_CONTAINER_NAME           | main-dev                 | Nome do container principal da aplicação                    |
| MAIN_CONTAINER_PORT           | 5000                     | Porta do container principal da aplicação                   |
| MAIN_CONTAINER_PROTOCOL       | http                     | Protocolo utilizado para acessar o container principal       |
| QUEST_CONTAINER_NAME          | quest-dev                | Nome do container Quest da aplicação                        |
| QUEST_CONTAINER_PORT          | 5001                     | Porta do container Quest da aplicação                       |
| QUEST_CONTAINER_PROTOCOL      | http                     | Protocolo utilizado para acessar o container Quest           |
| KEEP_CONTAINER_NAME           | keep-dev                 | Nome do container Keep da aplicação                         |
| KEEP_CONTAINER_PORT           | 5002                     | Porta do container Keep da aplicação                        |
| KEEP_CONTAINER_PROTOCOL       | http                     | Protocolo utilizado para acessar o container Keep            |
| LIST_CSV_CONTAINER_NAME       | list-csv-dev             | Nome do container List-CSV da aplicação                     |
| LIST_CSV_CONTAINER_PORT       | 5003                     | Porta do container List-CSV da aplicação                    |
| LIST_CSV_CONTAINER_PROTOCOL   | http                     | Protocolo utilizado para acessar o container List-CSV        |
| LIST_HTML_CONTAINER_NAME      | list-html-dev            | Nome do container List-HTML da aplicação                    |
| LIST_HTML_CONTAINER_PORT      | 5004                     | Porta do container List-HTML da aplicação                   |
| LIST_HTML_CONTAINER_PROTOCOL  | http                     | Protocolo utilizado para acessar o container List-HTML       |
| SEARCH_CSV_CONTAINER_NAME     | search-csv-dev           | Nome do container Search-CSV da aplicação                   |
| SEARCH_CSV_CONTAINER_PORT     | 5005                     | Porta do container Search-CSV da aplicação                  |
| SEARCH_CSV_CONTAINER_PROTOCOL | http                     | Protocolo utilizado para acessar o container Search-CSV      |
| SEARCH_HTML_CONTAINER_NAME    | search-html-dev          | Nome do container Search-HTML da aplicação                  |
| SEARCH_HTML_CONTAINER_PORT    | 5006                     | Porta do container Search-HTML da aplicação                 |
| SEARCH_HTML_CONTAINER_PROTOCOL| http                     | Protocolo utilizado para acessar o container Search-HTML     |


### Execução da aplicação:

As etapas de build e deploy desses microsserviços foram montadas utilizando uma stack no docker-compose.yml.

Para subir essa stack, basta executar em seu terminal preferido, no mesmo diretório do arquivo docker-compose.yml:

```bash
docker compose up -d --build
```

### Acessando a aplicação:

- Host: localhost
- Porta: 5000
- URL: http://localhost:5000

Para conseguir acessar a aplicação, basta acessar alguma das rotas abaixo:

| Método HTTP | Rota | Descrição |
|-------------|------|-----------|
| `GET` | / | : exibe mensagem de uso da aplicação |
| `GET` | /quest/<postal_code> | encaminha a requisição para o módulo Quest |
| `GET` | /list_csv | solicita uma lista em formato CSV |
| `GET` | /list_html | solicita uma lista em formato HTML |
| `GET` | /search_csv/<postal_code> | pesquisa um código postal específico na lista e retorna em formato CSV |
| `GET` | /search_html/<postal_code> |  pesquisa um código postal específico na lista e retorna em formato HTML |

Lembrando que cada um dos microsserviços podem ser acessados separadamente ao fazer
a requisição diretamente na porta do microsserviço. Por exemplo, se quiser acessar o
microsserviço de ```search_csv```, basta trocar a porta: http://localhost:5005/search_csv/64260000

**Obs:** certifique-se de ter pesquisado pelo menos algum cep antes, caso queira usar o de Piripiri-PI, faça a requisição para: http://localhost:5000/quest/64260000

### Verificando o status:

Em cada um dos microsserviços, foi adicionado um espaço para health-check.
Para visualizar o esses status basta executar em seu terminal preferido, no mesmo diretório do arquivo docker-compose.yml:

```bash
$ docker-compose ps

NAME                IMAGE               COMMAND                  SERVICE             CREATED             STATUS                 PORTS
keep-dev            keep:dev            "python3 keep.py"        keep                2 hours ago         Up 2 hours (healthy)   0.0.0.0:5002->5002/tcp, :::5002->5002/tcp
list-csv-dev        list-csv:dev        "python3 list_csv.py"    list-csv            2 hours ago         Up 2 hours (healthy)   0.0.0.0:5003->5003/tcp, :::5003->5003/tcp
list-html-dev       list-html:dev       "python3 list_html.py"   list-html           2 hours ago         Up 2 hours (healthy)   0.0.0.0:5004->5004/tcp, :::5004->5004/tcp
main-dev            main:dev            "python3 main.py"        main                2 hours ago         Up 2 hours (healthy)   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp
quest-dev           quest:dev           "python3 quest.py"       quest               2 hours ago         Up 2 hours (healthy)   0.0.0.0:5001->5001/tcp, :::5001->5001/tcp
search-csv-dev      search-csv:dev      "python3 search_csv.…"   search-csv          2 hours ago         Up 2 hours (healthy)   0.0.0.0:5005->5005/tcp, :::5005->5005/tcp
```