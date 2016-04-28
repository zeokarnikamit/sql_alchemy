# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from sqlalchemy.sql import select
from e1 import cookies, engine
s = select([cookies])
rp = engine.execute(s)
print rp.fetchall()