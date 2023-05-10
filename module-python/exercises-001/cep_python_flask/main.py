#!/bin/usr/python3
"""
Application to request Brazilian postal codes and manage them.
This module is an facade to all other services.
"""

#import json

import flask
import requests

import utils.loadinfo
import utils.log

environment_vars = utils.loadinfo.environment_vars()

utils.log.print_log(message=f'Module [{__file__}] initialized',
                    log_type='INFO')

app = flask.Flask(__name__,
            static_url_path='/static-files',
            static_folder='static-files')

@app.route('/')
def root_server():
    """ Shows usage message and finishes """
    return utils.loadinfo.main_root_content(),200

@app.route('/quest/<postal_code>')
@app.route('/QUEST/<postal_code>')
@app.route('/quest/<postal_code>/')
@app.route('/QUEST/<postal_code>/')
def quest_postal_code(postal_code=None):
    """ Evaluate request and send to quest module """
    response_content = ''
    response_code = 0
    if postal_code is None:
        response_content = utils.loadinfo.error_empty_postal_code()
        response_code = 400
    else:
        response_quest = requests.get(f'{environment_vars["quest_container_protocol"]}'
                                      f'://{environment_vars["quest_container_name"]}'
                                      f':{environment_vars["quest_container_port"]}'
                                      f'/quest/{postal_code}',
                                      timeout=5)
        response_content = response_quest.text
        response_code = response_quest.status_code
    return response_content, response_code

@app.route('/list_csv')
@app.route('/LIST_CSV')
@app.route('/list_csv/')
@app.route('/LIST_CSV/')
def list_csv():
    """ Request a CSV list """
    response_quest = requests.get(f'{environment_vars["list_csv_container_protocol"]}'
                                  f'://{environment_vars["list_csv_container_name"]}'
                                  f':{environment_vars["list_csv_container_port"]}'
                                  f'/list_csv',
                                  timeout=5)
    response_content = response_quest.text
    response_code = response_quest.status_code
    return response_content, response_code

@app.route('/list_html')
@app.route('/LIST_HTML')
@app.route('/list_html/')
@app.route('/LIST_HTML/')
def list_html():
    """ Request a HTML list """
    response_quest = requests.get(f'{environment_vars["list_html_container_protocol"]}'
                                  f'://{environment_vars["list_html_container_name"]}'
                                  f':{environment_vars["list_html_container_port"]}'
                                  f'/list_html',
                                  timeout=5)
    response_content = response_quest.text
    response_code = response_quest.status_code
    return response_content, response_code

@app.route('/search_csv/<postal_code>')
@app.route('/SEARCH_CSV/<postal_code>')
@app.route('/search_csv/<postal_code>/')
@app.route('/SEARCH_CSV/<postal_code>/')
def search_csv(postal_code=None):
    """ Search a specific postal code in keep list and return CSV"""
    response_content = ''
    response_code = 0
    if postal_code is None:
        response_content = utils.loadinfo.error_empty_postal_code()
        response_code = 400
    else:
        response_quest = requests.get(f'{environment_vars["search_csv_container_protocol"]}'
                                      f'://{environment_vars["search_csv_container_name"]}'
                                      f':{environment_vars["search_csv_container_port"]}'
                                      f'/search_csv/{postal_code}',
                                      timeout=5)
        response_content = response_quest.text
        response_code = response_quest.status_code
    return response_content, response_code

@app.route('/search_html/<postal_code>')
@app.route('/SEARCH_HTML/<postal_code>')
@app.route('/search_html/<postal_code>/')
@app.route('/SEARCH_HTML/<postal_code>/')
def search_html(postal_code=None):
    """ Search a specific postal code in keep list and return HTML"""
    postal_code += "1" # only to solve PyLint error
    return "To be mplemented method",200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environment_vars['main_container_port']), debug=True)

utils.log.print_log(message=f'Module [{__file__}] finished',
                    log_type='INFO')
