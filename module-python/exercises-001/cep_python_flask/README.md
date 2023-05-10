# ViaCEP App
This is a simple application to request and manage Brazilian postal codes.
Each module is independent and based in Flask to comunicate information.
Once a response is received from ViaCEP, it is keeped in "cache" and can be
listed ou searched.

## Modules Diagram
This simple diagram explains comunication between modules.
```
                    ┌──────┐
                    │viacep│third-party
                    └──────┘  service
                        ▲
                        │
┌────┐    ┌────┐     ┌──┴──┐    ┌────┐
│user├───►│main├─┬──►│quest├───►│keep│
└────┘    └────┘ │   └─────┘    └────┘
                 │                 ▲
                 │   ┌────────┐    │
                 ├──►│list_csv├────┤
                 │   └────────┘    │
                 │                 │
                 │   ┌─────────┐   │
                 ├──►│list_html├───┤
                 │   └─────────┘   │
                 │                 │
                 │   ┌──────────┐  │
                 ├──►│search_csv├──┤
                 │   └──────────┘  │
                 │                 │
                 │   ┌───────────┐ │
                 └──►│search_html├─┘
                     └───────────┘
```
- **viacep**: a third-party service to consult brazilian postal codes;
- **main**: facade to control and forward access to other modules;
- **quest**: module to search a postal code in viacep service;
- **keep**: module to keep all postal codes searched by quest module;
- **list_csv**: list all postal codes in keep module (CSV format);
- **list_html**: list all postal codes in keep module (html format);
- **search_csv**: search a postal code in keep module (CSV format);
- **search_html**: search a postal code in keep module (HTML format).

## Modules implementation
The status of each module is:
- **main**: working, automated tests;
- **quest**: working;
- **keep**: working;
- **list_csv**: working;
- **list_html**: working;
- **search_csv**: not implemented;
- **search_html**: not implemented;
- **utils**: working, automated tests;

## Prepare Development Environment
Install:
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```
Use python3.10 if possible.

Create a Virtual Environment:
```bash
# access pproject root directory
python3.10 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

Check code style with PyLint:
```bash
pip3 install pylint==2.15.9
python3 -m pylint *.py utils/*.py
python3 -m pylint *.py utils/*.py || :
```

Execute tests with PyTest:
```bash
pip3 install pytest==7.2.0
python3 -m pytest -v
```

Deactivate virtual environment:
```bash
deactivate
```

## Start Application Locally
In this example, all modules are running in the same terminal.
Please, consider use a terminal to each module.
```bash
export $(grep -v -e '^#' config/tests_local_vars.env)
python3 main.py &
python3 quest.py &
python3 keep.py &
python3 list_csv.py &
python3 list_html.py &
```

To test run:
```bash
wait_time='2s'
curl -sS localhost:5000
sleep $wait_time
for pc in 02739000 02201000 22041011 22050002 32310210 33120510
do 
  curl -sS localhost:5000/quest/$pc
  sleep $wait_time
done
curl -sS localhost:5000/list_csv
sleep $wait_time
curl -sS localhost:5000/list_html
sleep $wait_time
curl -sS localhost:5000/list_html|grep -A9 22041-011
```

## Known bugs
- The same postal code quest many time will be keeped many times

