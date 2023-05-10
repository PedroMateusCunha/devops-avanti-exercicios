#!/usr/bin/python3
"""
Application to request Brazilian postal codes and manage them.
This module searches postal codes in a CSV file.
"""
from io import StringIO
import pandas as pd
import requests
import flask
import utils.loadinfo
import utils.log

environment_vars = utils.loadinfo.environment_vars()

utils.log.print_log(message=f'Module [{__file__}] initialized',
                     log_type='INFO')

app = flask.Flask(__name__)

@app.route('/')
def root_server():
    """ Shows usage message and finishes """
    return utils.loadinfo.main_root_content(),200

@app.route('/search_csv/<postal_code>')
@app.route('/SEARCH_CSV/<postal_code>')
@app.route('/search_csv/<postal_code>/')
@app.route('/SEARCH_CSV/<postal_code>/')
def search_csv(postal_code=None):
    """ Search for postal code in CSV file """
    response_content = ''
    response_code = 0
    df_data = pd.DataFrame()
    if postal_code is None:
        response_content = utils.loadinfo.error_empty_postal_code()
        response_code = 400
    else:
        response_quest = requests.get(f'{environment_vars["list_csv_container_protocol"]}'
                            f'://{environment_vars["list_csv_container_name"]}'
                            f':{environment_vars["list_csv_container_port"]}'
                            f'/list_csv',
                            timeout=5)
        response_content = response_quest.text
        response_code = response_quest.status_code
        if not response_content:
            return utils.loadinfo.error_outdated_postal_code()
        df_data = pd.read_csv(StringIO(response_content), header=None, delimiter=";")
        df_data.columns = ['cep', 'logradouro', 'complemento', 'bairro', 'localidade',
                      'uf', 'vazia', 'ibge', 'gia', 'ddd', 'siafi', 'vazia']
        df_data = df_data.drop(columns=['vazia'])
        df_data = df_data.drop_duplicates(subset='cep')
        cep = postal_code[:5] + "-" + postal_code[5:]
        cep_filter = df_data.loc[df_data['cep']==cep]
        consult = cep_filter.to_csv(index=False, sep=";")
        lines = consult.splitlines()[1:]
        consult_content = '\n'.join(lines)

        if len(consult_content) != 0 :
            response_content = consult
        else:
            response_content = utils.loadinfo.error_outdated_postal_code()
            response_code = 400
    return response_content, response_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environment_vars['search_csv_container_port']), debug=True)

utils.log.print_log(message=f'Module [{__file__}] finished',
                     log_type='INFO')
