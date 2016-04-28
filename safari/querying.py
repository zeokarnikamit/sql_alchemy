# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from e2 import children


def run(command):
    response = {'response': 'failure', 'msg': ''}
    try:
        ex = command.execute()
        response['response'] = 'success'
        response['docs'] = ex.fetchall()
        response['msg'] = 'passed'
    except Exception, e:
        response['msg'] = e
    return response


if __name__ == '__main__':
    '''
    1. get a particular document
    2. get docs depending on particular condition
    '''
    c = children.select(children.c.name == 'Amit')
    # c = children.select(children.c.age < 16)
    resp = run(c)
    if resp.get('response') == 'success':
        for i in resp['docs']:
            print i
    else:
        print 'failed', resp['msg']
