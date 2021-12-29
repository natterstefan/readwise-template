#!/usr/bin/env python

# inspired by https://stackoverflow.com/a/37939821/1238150
import sys
import os
from jinja2 import Environment, FileSystemLoader

# setup jinja
env = Environment(loader=FileSystemLoader('./src'))

# add custom filters (actual filters are implemented by Readwise)
# see https://stackoverflow.com/a/25450294/1238150
def pluralize(input):
    """Readwise pluralize"""
    return input

env.filters['pluralize'] = pluralize

# files to lint
templates = [x for x in env.list_templates() if x.endswith('.jinja2')]

for template in templates:
    t = env.get_template(template)
    env.parse(t)