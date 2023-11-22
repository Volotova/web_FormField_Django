from tinydb import TinyDB
import json


db = TinyDB('db.json', indent=4)
template_bd = db.table('MyForm')


def insert():
    existing_db = template_bd.all()
    if not existing_db:
        template_bd.insert_multiple([
            {'date': '2020-01-01', 'phone': '+79284582527', 'email': 'qwerty@mail.ru',
             'text': '2test', 'name': 'Alex'},
            {'date': '2020-02-01', 'phone': '+79284582526', 'email': '1qwerty@mail.ru',
             'text': '1test', 'name': 'Bob'},
            {'date': '2020-03-01', 'phone': '+79284582527', 'email': '2qwerty@mail.ru',
             'text': '3test', 'name': 'Vlad'},
        ])


def forma():
    d = {}
    circle = 0
    for id in template_bd:
        if circle < 1:
            d.update(id)
            d.pop('text')
            d.pop('name')
            return json.dumps(d, indent=4)


insert()
