# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from e2 import children


def insert_data(db, data):
    """
    @:param db --> db object where data has to be inserted
    @:param data --> data to be inserted
    :return {'response': 'success/failure', 'msg': if any exceptions occur}
    """
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
    docs = [{'name': 'sathvik', 'age': 25, 'marks': 85},
            {'name': 'yathiraj', 'age': 24, 'marks': 70},
            {'name': 'vijay', 'age': 25, 'marks': 87},
            {'name': 'nikhil', 'age': 25, 'marks': 82}]
    print insert_data(children, docs)
