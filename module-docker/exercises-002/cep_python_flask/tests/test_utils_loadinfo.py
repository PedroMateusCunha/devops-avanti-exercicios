#!/bin/usr/python3
""" Tests utils/loadinfo.py module
"""

import sys, os
up_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(up_directory)
import utils.loadinfo
import testresources

def test__enviroment_var__properties():
    function_result = utils.loadinfo.environment_vars()
    assert type(function_result) is dict
    assert len(function_result) == 24

def test__enviroment_var__load():
    function_result = utils.loadinfo.environment_vars()
    assert function_result['main_container_name'] == 'localhost'
    assert function_result['main_container_port'] == '5000'
    assert function_result['main_container_protocol'] == 'http'
    assert function_result['quest_container_name'] == 'localhost'
    assert function_result['quest_container_port'] == '5001'
    assert function_result['quest_container_protocol'] == 'http'
    assert function_result['keep_container_name'] == 'localhost'
    assert function_result['keep_container_port'] == '5002'
    assert function_result['keep_container_protocol'] == 'http'
    assert function_result['list_csv_container_name'] == 'localhost'
    assert function_result['list_csv_container_port'] == '5003'
    assert function_result['list_csv_container_protocol'] == 'http'
    assert function_result['list_html_container_name'] == 'localhost'
    assert function_result['list_html_container_port'] == '5004'
    assert function_result['list_html_container_protocol'] == 'http'
    assert function_result['search_csv_container_name'] == 'localhost'
    assert function_result['search_csv_container_port'] == '5005'
    assert function_result['search_csv_container_protocol'] == 'http'
    assert function_result['search_html_container_name'] == 'localhost'
    assert function_result['search_html_container_port'] == '5006'
    assert function_result['search_html_container_protocol'] == 'http'
    assert int(function_result['main_container_port']) == 5000
    assert int(function_result['quest_container_port']) == 5001
    assert int(function_result['keep_container_port']) == 5002
    assert int(function_result['list_csv_container_port']) == 5003
    assert int(function_result['list_html_container_port']) == 5004
    assert int(function_result['search_csv_container_port']) == 5005
    assert int(function_result['search_html_container_port']) == 5006
 
def test__main_root_content__properties():
    function_result = utils.loadinfo.main_root_content()
    assert type(function_result) is str
    assert len(function_result) > 300

def test__postal_code_keeped__properties():
    function_result = utils.loadinfo.postal_code_keeped()
    assert type(function_result) is str
    assert len(function_result) > 50

def test__error_empty_postal_code__properties():
    function_result = utils.loadinfo.error_empty_postal_code()
    assert type(function_result) is str
    assert len(function_result) > 50

def test__error__error_invalid_postal_code__properties():
    function_result = utils.loadinfo.error_invalid_postal_code()
    assert type(function_result) is str
    assert len(function_result) > 50

def test__error__error_outdated_postal_code__properties():
    function_result = utils.loadinfo.error_outdated_postal_code()
    assert type(function_result) is str
    assert len(function_result) > 50

def test__error__generate_list_html__properties():
    function_result = utils.loadinfo.generate_list_html(testresources.test_list_postal_code)
    assert type(function_result) is str
    assert len(function_result) > 2300

def test__error__generate_list_html__load():
    function_result = utils.loadinfo.generate_list_html(testresources.test_list_postal_code)
    assert function_result.find('22050-002') > 0
    assert function_result.find('22041-011') > 0
    assert function_result.find('32310-210') > 0
    assert function_result.find('22050-002') < function_result.find('22041-011')
    assert function_result.find('22041-011') < function_result.find('32310-210')
    assert function_result.find('de 583 a 831 - lado ímpar') > 0
    assert function_result.find('Nova York') == -1
    assert function_result.find('Califórina') == -1
    assert function_result.find('California') == -1
