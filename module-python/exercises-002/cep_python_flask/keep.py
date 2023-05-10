#!/bin/usr/python3
"""
Application to request Brazilian postal codes and manage them.
This module is a "cache" to all searched postal codes.
"""

import json

import flask

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

@app.route('/keep', methods=['POST'])
@app.route('/KEEP', methods=['POST'])
@app.route('/keep/', methods=['POST'])
@app.route('/KEEP/', methods=['POST'])
def keep_postal_code():
    """ Evaluate request and send to quest module """
    response_content = utils.loadinfo.postal_code_keeped()
    response_code = 200
    if flask.request.get_json() is None:
        response_content = utils.loadinfo.error_empty_postal_code()
        response_code = 400
    else:
        postal_codes_full_list.append(json.loads(flask.request.get_json()))
        print(postal_codes_full_list)
    return response_content, response_code

@app.route('/retrieve_keeped_list')
@app.route('/RETRIEVE_KEEPED_LIST')
@app.route('/retrieve_keeped_list/')
@app.route('/RETRIEVE_KEEPED_LIST/')
def retreive_keeped_list():
    """ Sends the the entire list """
    return str(postal_codes_full_list), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environment_vars['keep_container_port']), debug=False)

utils.log.print_log(message=f'Module [{__file__}] finished',
                    log_type='INFO')
