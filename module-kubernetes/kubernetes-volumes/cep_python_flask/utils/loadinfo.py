#!/bin/usr/python3
""" Module with all load data utilities """

import os

def environment_vars() -> dict:
    """ Load all environment variables needed """
    return { "viacep_container_name": os.getenv('VIACEP_CONTAINER_NAME'),
             "viacep_container_port": os.getenv('VIACEP_CONTAINER_PORT'),
             "viacep_container_protocol": os.getenv('VIACEP_CONTAINER_PROTOCOL'),
             "main_container_name": os.getenv('MAIN_CONTAINER_NAME'),
             "main_container_port": os.getenv('MAIN_CONTAINER_PORT'),
             "main_container_protocol": os.getenv('MAIN_CONTAINER_PROTOCOL'),
             "quest_container_name": os.getenv('QUEST_CONTAINER_NAME'),
             "quest_container_port": os.getenv('QUEST_CONTAINER_PORT'),
             "quest_container_protocol": os.getenv('QUEST_CONTAINER_PROTOCOL'),
             "keep_container_name": os.getenv('KEEP_CONTAINER_NAME'),
             "keep_container_port": os.getenv('KEEP_CONTAINER_PORT'),
             "keep_container_protocol": os.getenv('KEEP_CONTAINER_PROTOCOL'),
             "list_csv_container_name": os.getenv('LIST_CSV_CONTAINER_NAME'),
             "list_csv_container_port": os.getenv('LIST_CSV_CONTAINER_PORT'),
             "list_csv_container_protocol": os.getenv('LIST_CSV_CONTAINER_PROTOCOL'),
             "list_html_container_name": os.getenv('LIST_HTML_CONTAINER_NAME'),
             "list_html_container_port": os.getenv('LIST_HTML_CONTAINER_PORT'),
             "list_html_container_protocol": os.getenv('LIST_HTML_CONTAINER_PROTOCOL'),
             "search_csv_container_name": os.getenv('SEARCH_CSV_CONTAINER_NAME'),
             "search_csv_container_port": os.getenv('SEARCH_CSV_CONTAINER_PORT'),
             "search_csv_container_protocol": os.getenv('SEARCH_CSV_CONTAINER_PROTOCOL'),
             "search_html_container_name": os.getenv('SEARCH_HTML_CONTAINER_NAME'),
             "search_html_container_port": os.getenv('SEARCH_HTML_CONTAINER_PORT'),
             "search_html_container_protocol": os.getenv('SEARCH_HTML_CONTAINER_PROTOCOL'),
             "csv_file_path": os.getenv('CSV_FILE_PATH'),}

def main_root_content() -> str:
    """ Generates root content """
    return ("<h1>CEP Main</h1>\n"
            "<b>/</b> this usage page<br>\n"
            "<b>/quest/[CEP]</b> choose CEP to request and keep<br>\n"
            "<b>/list_csv</b> list all CEP keeped in CSV format<br>\n"
            "<b>/list_html</b> list all CEP keeped in HTML format<br>\n"
            "<b>/search_csv/[CEP]</b> search CEP only in keeped list and show in CSV format<br>\n"
            "<b>/search_html/[CEP]</b> search CEP only in keeped list and show in HTML format<br>\n" )

def postal_code_keeped() -> str:
    """ Gerenrates answer to keeped postal code """
    return ("<h1>CEP Main</h1>\n"
            "<b>Info: </b>postal code keeped<br>\n")

def error_empty_postal_code() -> str:
    """ Gererates aswer to empyt postal code """
    return ("<h1>CEP Main</h1>\n"
            "<b>Error: </b>postal code is empty<br>\n")

def error_invalid_postal_code() -> str:
    """ Gererates aswer to invalid postal code """
    return ("<h1>CEP Main</h1>\n"
            "<b>Error: </b>postal code is invalid<br>\n")

def error_outdated_postal_code() -> str:
    """ Gererates aswer to empyt outdated code """
    return ("<h1>CEP Main</h1>\n"
            "<b>Error: </b>postal code is outdated in ViaCEP service<br>\n")

def generate_list_html(list_postal_codes) -> str:
    """ Gererates HTML list """
    lines = ""
    for postal_code in list_postal_codes:
        line = open('html/list_line_template.html', encoding='utf-8').read()
        line = line.replace('%%CEP%%', str(postal_code['cep']))
        line = line.replace('%%PLACE%%', str(postal_code['logradouro']))
        line = line.replace('%%ADDITION%%', str(postal_code['complemento']))
        line = line.replace('%%DISTRICT%%', str(postal_code['bairro']))
        line = line.replace('%%CITY%%', str(postal_code['localidade']))
        line = line.replace('%%STATE%%', str(postal_code['uf']))
        line = line.replace('%%IBGE%%', str(postal_code['ibge']))
        line = line.replace('%%GIA%%', str(postal_code['gia']))
        line = line.replace('%%DDD%%', str(postal_code['ddd']))
        line = line.replace('%%SIAFI%%', str(postal_code['siafi']))
        lines += line
    response = (open('html/header_content.html', encoding='utf-8').read() +
                open('html/list_top_content.html', encoding='utf-8').read() +
                lines +
                open('html/list_bottom_content.html', encoding='utf-8').read() +
                open('html/bottom_content.html', encoding='utf-8').read())
    return response
