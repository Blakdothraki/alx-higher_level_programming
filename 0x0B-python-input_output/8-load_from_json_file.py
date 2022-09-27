#!/usr/bin/python3
from json import loads

def load_from_file(filename):
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
