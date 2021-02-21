# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_sqlitem import SqlItem
from db.models.boe_disposition import BoeDisposition, Departamento


class BoeDispositionItem(SqlItem):
    sqlmodel = BoeDisposition


class DepartamentoItem(SqlItem):
    sqlmodel = Departamento
