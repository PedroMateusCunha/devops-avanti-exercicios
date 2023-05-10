#!/bin/usr/python3
"""
Application to request Brazilian postal codes and manage them.
This module list all "cache" in CSV format.
"""

import json

import flask
import requests

import utils.loadinfo
import utils.log

environment_vars = utils.loadinfo.environment_vars()
utils.log.print_log(message=f'Module [{__file__}] initialized',
                    log_type='INFO')

postal_codes_full_list = []

app = flask.Flask(__name__)

@app.route('/')
def root_server():
    """ Shows usage message and finishes """
    return utils.loadinfo.main_root_content()

@app.route('/list_html')
@app.route('/LIST_HTML')
@app.route('/list_html/')
@app.route('/LIST_HTML/')
def list_csv():
    """ Generate a HTML list """
    response_content = ''
    response_code = 200
    postal_code_list = requests.get(f'{environment_vars["keep_container_protocol"]}'
                                    f'://{environment_vars["keep_container_name"]}'
                                    f':{environment_vars["keep_container_port"]}'
                                    f'/retrieve_keeped_list',
                                    timeout = 5)
    postal_code_list_quote = postal_code_list.text.replace("'", '"')
    response_content = utils.loadinfo.generate_list_html(json.loads(postal_code_list_quote))
    return response_content, response_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environment_vars['list_html_container_port']), debug=False)

utils.log.print_log(message=f'Module [{__file__}] finished',
                    log_type='INFO')
