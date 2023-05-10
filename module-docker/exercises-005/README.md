# Exercícios 5

---
**Requisitos**

- Verifique a instalação do Airflow baseada em Docker-compose apresentada em https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html.
- Baixe, adapte o docker-compose para usar as credenciais airflow e wolfria199188177. - Acesse a interface de acesso pelo navegador. Veja a lista de DAGs, abra example_python_operator, verifique o código e veja o gráfico de tasks.
- O desafio aqui é submeter-se a um docker-compose mais complexo, feito por outros e ainda assim rodar corretamente o serviço. Compreender quais informações do seu docker-compose você precisa passar para terceiros utilizarem corretamente.
- Teste cada uma das condições, salve prints, arquive.
---

### Descrição da Abordagem:

Neste exercício foi construído um Dockerfile para o código binary_search.py.

### Preparação do ambiente:

Primeiramente teremos que realizar o download do manifesto:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.0/docker-compose.yaml'
```
Logo após é preciso configurar o usuário correto do Airflow:

```bash
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Além disso, configurar as variáveis de ambiente referentes as credenciais de acesso da UI:
```bash
echo _AIRFLOW_WWW_USER_USERNAME=airflow >> .env; \
echo _AIRFLOW_WWW_USER_PASSWORD=wolfria199188177 >> .env
```

### Inicializando o Banco de Dados:

Em todos os sistemas operacionais , você precisa executar migrações de banco de dados e criar a primeira conta de usuário. Para fazer isso, execute.

```bash
docker compose up airflow-init
```
E seguir as instruções para realizar a busca binária em uma lista.

### Executando a stack completa:

Para realizar o deploy da stack completa, execute:

```bash
docker compose up -d
```
