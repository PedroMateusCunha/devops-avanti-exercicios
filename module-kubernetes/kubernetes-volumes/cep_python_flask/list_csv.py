#!/bin/usr/python3
"""
Application to request Brazilian postal codes and manage them.
This module list all "cache" in CSV format.
"""

import json
import csv
import flask
import requests

import utils.loadinfo
import utils.log

environment_vars = utils.loadinfo.environment_vars()
utils.log.print_log(message=f'Module [{__file__}] initialized',
                    log_type='INFO')

postal_codes_full_list = []

app = flask.Flask(__name__)

def save_csv_file(csv_content, csv_file_path):
    """ Save CSV content to file """
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(csv_content)
    return

def csv_to_json(csv_file_path, json_file_path):
    """ Read a CSV file and convert to JSON """
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        next(reader)  # ignora a linha do cabeçalho, se houver
        data = []
        for row in reader:
            item = {
                'cep': row[0],
                'logradouro': row[1],
                'complemento': row[2],
                'bairro': row[3],
                'localidade': row[4],
                'uf': row[5],
                'ibge': row[7],
                'gia': row[8],
                'ddd': row[9],
                'siafi': row[10],
            }
            data.append(item)

        with open(json_file_path, 'w') as jsonfile:
            json.dump(data, jsonfile)

@app.route('/')
def root_server():
    """ Shows usage message and finishes """
    return utils.loadinfo.main_root_content()

@app.route('/list_csv')
@app.route('/LIST_CSV')
@app.route('/list_csv/')
@app.route('/LIST_CSV/')

def list_csv():
    """ Generate a CSV list """
    response_content = ''
    response_code = 200
    postal_code_list = requests.get(f'{environment_vars["keep_container_protocol"]}'
                                    f'://{environment_vars["keep_container_name"]}'
                                    f':{environment_vars["keep_container_port"]}'
                                    f'/retrieve_keeped_list',
                                    timeout = 5)
    postal_code_list_quote = postal_code_list.text.replace("'", '"')
    postal_code_list_csv = []
    for postal_code in json.loads(postal_code_list_quote):
        postal_code_list_csv.append([postal_code["cep"], postal_code["logradouro"],
                                     postal_code["complemento"], postal_code["bairro"],
                                     postal_code["localidade"], postal_code["uf"],
                                     "", postal_code["ibge"], postal_code["gia"],
                                     postal_code["ddd"], postal_code["siafi"]])
    save_csv_file(csv_content=postal_code_list_csv, csv_file_path="csv/postal_codes.csv")
    csv_to_json(csv_file_path="csv/postal_codes.csv", json_file_path="csv/postal_codes.json")
    
    for postal_code in postal_code_list_csv:
        response_content += ';'.join(postal_code) + '\n'
    return response_content, response_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environment_vars['list_csv_container_port']), debug=False)

utils.log.print_log(message=f'Module [{__file__}] finished',
                    log_type='INFO')
