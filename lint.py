#!/usr/bin/env python

import sys
from setup import env

# files to lint
templates = [x for x in env.list_templates() if x.endswith('.jinja2')]

for template in templates:
    t = env.get_template(template)
    env.parse(t)