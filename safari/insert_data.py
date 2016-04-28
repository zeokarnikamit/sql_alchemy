# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from e1 import cookies
ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)
if __name__ == '__main__':
    result = connection.execute(ins)