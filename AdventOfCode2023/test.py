import dbf
import sys

fileName = "/Users/georgris/Downloads/kladr1251.dbf"
table = dbf.Table(fileName)
print(len(table))