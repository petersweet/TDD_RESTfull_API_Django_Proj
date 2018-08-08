# TDD_RESTfull_API_Django_Proj
Small Django project with RESTfull API using test driven development

Quickstart

virtualenv {{ project_name }}
source {{ project_name }}/bin/activate
cd path/to/{{ project_name }}/repository
pip install -r requirements.pip
pip install -e .
cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py
manage.py syncdb --migrate