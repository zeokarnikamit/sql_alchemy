# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from e2 import imdb, children


def insert_data(db, data):
    response = {'response': 'failure', 'msg': ''}
    try:
        cmd = db.insert()
        for i in data:
            cmd.execute(i)
        else:
            response['response'] = 'success'
            response['msg'] = 'passed'
    except Exception, e:
        response['msg'] = e
    return response

if __name__ == '__main__':
    data = [{'name': 'John', 'age': 15, 'marks': 35},
            {'name': 'Susan', 'age': 14, 'marks': 90},
            {'name': 'Carl', 'age': 15, 'marks': 78},
            {'name': 'Amit', 'age': 18, 'marks': 92}]
    print insert_data(children, data)
