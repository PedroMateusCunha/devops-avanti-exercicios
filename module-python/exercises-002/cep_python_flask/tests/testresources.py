import os

test_list_postal_code = [
    {'cep': '22050-002', 'logradouro': 'Avenida Nossa Senhora de Copacabana', 'complemento': 'de 583 a 831 - lado ímpar', 'bairro': 'Copacabana', 'localidade': 'Rio de Janeiro', 'uf': 'RJ', 'ibge': '3304557', 'gia': '', 'ddd': '21', 'siafi': '6001'},
    {'cep': '22041-011', 'logradouro': 'Rua Santa Clara', 'complemento': 'de 1 ao fim - lado ímpar', 'bairro': 'Copacabana', 'localidade': 'Rio de Janeiro', 'uf': 'RJ', 'ibge': '3304557', 'gia': '', 'ddd': '21', 'siafi': '6001'},
    {'cep': '32310-210', 'logradouro': 'Avenida José Faria da Rocha', 'complemento': 'de 2402/2403 ao fim', 'bairro': 'Eldorado', 'localidade': 'Contagem', 'uf': 'MG', 'ibge': '3118601', 'gia': '', 'ddd': '31', 'siafi': '4371'}
]

os.environ['VIACEP_CONTAINER_NAME']='localhost'
os.environ['VIACEP_CONTAINER_PORT']='5000'
os.environ['VIACEP_CONTAINER_PROTOCOL']='http'
os.environ['MAIN_CONTAINER_NAME']='localhost'
os.environ['MAIN_CONTAINER_PORT']='5000'
os.environ['MAIN_CONTAINER_PROTOCOL']='http'
os.environ['QUEST_CONTAINER_NAME']='localhost'
os.environ['QUEST_CONTAINER_PORT']='5001'
os.environ['QUEST_CONTAINER_PROTOCOL']='http'
os.environ['KEEP_CONTAINER_NAME']='localhost'
os.environ['KEEP_CONTAINER_PORT']='5002'
os.environ['KEEP_CONTAINER_PROTOCOL']='http'
os.environ['LIST_CSV_CONTAINER_NAME']='localhost'
os.environ['LIST_CSV_CONTAINER_PORT']='5003'
os.environ['LIST_CSV_CONTAINER_PROTOCOL']='http'
os.environ['LIST_HTML_CONTAINER_NAME']='localhost'
os.environ['LIST_HTML_CONTAINER_PORT']='5004'
os.environ['LIST_HTML_CONTAINER_PROTOCOL']='http'
os.environ['SEARCH_CSV_CONTAINER_NAME']='localhost'
os.environ['SEARCH_CSV_CONTAINER_PORT']='5005'
os.environ['SEARCH_CSV_CONTAINER_PROTOCOL']='http'
os.environ['SEARCH_HTML_CONTAINER_NAME']='localhost'
os.environ['SEARCH_HTML_CONTAINER_PORT']='5006'
os.environ['SEARCH_HTML_CONTAINER_PROTOCOL']='http'
