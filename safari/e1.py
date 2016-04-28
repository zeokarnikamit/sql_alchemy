# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, MetaData, DateTime, Boolean, create_engine, select
from datetime import datetime
metadata = MetaData()

cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2)))

users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

orders = Table('orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id')),
    Column('shipped', Boolean(), default=False)

)

line_items = Table('line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
)


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
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
