#!/bin/usr/python3
"""
Application to request Brazilian postal codes and manage them.
This module requests information in viacep service.
"""

import json

import flask
import requests

import utils.loadinfo
import utils.log

environment_vars = utils.loadinfo.environment_vars()

utils.log.print_log(message=f'Module [{__file__}] initialized',
                    log_type='INFO')

app = flask.Flask(__name__)

@app.route('/')
def root_server():
    """ Shows usage message and finishes """
    return utils.loadinfo.main_root_content()

@app.route('/quest/<postal_code>')
@app.route('/QUEST/<postal_code>')
@app.route('/quest/<postal_code>/')
@app.route('/QUEST/<postal_code>/')
def quest_postal_code(postal_code=None):
    """ Request postal code from viacep service """
    response_content = ''
    response_code = 0
    if postal_code is None:
        response_content = utils.loadinfo.error_empty_postal_code()
        response_code = 400
    else:
        response_viacep = requests.get(f'{environment_vars["viacep_container_protocol"]}'
                                       f'://{environment_vars["viacep_container_name"]}'
                                       f':{environment_vars["viacep_container_port"]}'
                                       f'/ws/{postal_code}/json',
                                       timeout=5)
        if response_viacep.status_code == 200:
            viacep_content = json.loads(response_viacep.text)
            if 'erro' not in viacep_content:
                response_content = response_viacep.text
                response_code = 200
                requests.post(f'{environment_vars["keep_container_protocol"]}'
                              f'://{environment_vars["keep_container_name"]}'
                              f':{environment_vars["keep_container_port"]}'
                              f'/keep',
                              json=response_content,
                              timeout=5)
            else:
                response_content = utils.loadinfo.error_outdated_postal_code()
                response_code = 400
        if response_viacep.status_code == 400:
            response_content = utils.loadinfo.error_invalid_postal_code()
            response_code = 400
    return response_content, response_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environment_vars['quest_container_port']), debug=False)

utils.log.print_log(message=f'Module [{__file__}] finished',
                    log_type='INFO')
