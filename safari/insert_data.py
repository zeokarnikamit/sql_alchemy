# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from e1 import cookies
from sqlalchemy import create_engine, MetaData, select


engine = create_engine('sqlite:///:memory:')
metadata = MetaData()
metadata.create_all(engine)
ins = cookies.insert()
inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    },
    {
        'cookie_name': 'peanut ',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/butter.html',
        'cookie_sku': 'PB01',
        'quantity': '240',
        'unit_cost': '0.25'
    }
]
result = engine.execute(ins, inventory_list)
s = select([cookies])
s = s.order_by(cookies.c.quantity)
rp = engine.execute(s)
for i in rp:
    print i