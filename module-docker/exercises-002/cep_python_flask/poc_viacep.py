#!/bin/usr/python3
"""
Module Docstring: Explanation about code in this module/file
Proof of Concept to test main Python elements.
This code feeds a list of dictionaries based in ViaCep webservice.
Tested with Python 3.10.
pip3 install requests==2.27.1
To create a list of postal codes use:
    export POSTAL_CODES='["02739000","02201000","22041011","22050002","32310210","33120510"]'
"""

# Imports
import os 
import json 
import requests 
import sys       # out of order
#TODO: include other libraries
#FIXME: include other methods

# Constants and Variables
postal_codes_full_list = []
postal_codes_to_search = json.loads(os.getenv('POSTAL_CODES'))
not_used_variable = 4

# Function / Classes
def search_viacep(postal_code_to_search: str):
    """ Function Docstring: Explanation about code in this function/method.
        This function accesses ViaCEP to retrive postal code."""
    response_viacep = requests.get('http://viacep.com.br/ws/'
                                   + postal_code_to_search
                                   + '/json',
                                   timeout = 5)
    if response_viacep.status_code == 200:
        viacep_content = json.loads(response_viacep.text)
        if 'erro' not in viacep_content:
            print(f'Found {postal_code}!!!')
            #print(str(response_viacep.text))
            postal_codes_full_list.append(viacep_content)
        else:
            print(f'Error: found {postal_code} but it is outdated.')
    else:
        print(f'Error: {postal_code} generated error {response_viacep.status_code}')


# Main code
if postal_codes_to_search is not None:
    for postal_code in postal_codes_to_search:
        print(f'Search postal code {postal_code} in ViaCEP webservice...')
        search_viacep(postal_code)
        print('----------------')
    print('================')
    for response in postal_codes_full_list:
        print(str(response))
    for response in postal_codes_full_list:
        print(f'CEP="{response["cep"]}" '
              f'DDD="{response["ddd"]}" '
              f'UF="{response["uf"]}" '
              f'CIDADE="{response["localidade"]}"')
else:
    print('Error: No postal codes are loaded.')
