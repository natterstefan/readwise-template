#!/usr/bin/env python

# inspired by https://stackoverflow.com/a/37939821/1238150
import sys
from jinja2 import Environment, FileSystemLoader

# setup jinja
env = Environment(loader=FileSystemLoader('./'))

# add custom filters (actual filters are implemented by Readwise)
# see https://stackoverflow.com/a/25450294/1238150
def pluralize(input):
    """Readwise pluralize"""
    if input == 1:
      return ''
    else:
      return 's'

env.filters['pluralize'] = pluralize
