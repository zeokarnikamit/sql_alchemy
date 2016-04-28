# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from sqlalchemy import *

db = create_engine('sqlite:///tutorial.db')

db.echo = False  # Don't log execution commands

metadata = MetaData(db)


imdb = Table('imbd', metadata,
             Column('name', String, index=True, primary_key=True),
             Column('raiting', Float),
             Column('release_year', Integer)
             )
children = Table('children', metadata,
                 Column('name', String, index=True, primary_key=True),
                 Column('age', Integer),
                 Column('marks', Float))
