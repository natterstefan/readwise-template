#!/usr/bin/env python

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

data = {
  'author': 'Jane Doe',
  # TODO: add support for more categories
  'category': 'books',
  'date': '01-01-2021',
  'full_title': 'Sed sit. Donec lacus. Morbi quis.',
  'highlight_location_url': 'https://example.com/highlight_location_url',
  'highlight_location': 'example.com',
  'highlight_note': 'Nunc in ligula feugiat, ornare ligula nec, elementum dui.',
  'highlight_tags': ['tag1', 'tag2'],
  'highlight_text': 'Vivamus in.',
  'image_url': 'https://example.com/image_url.png',
  'num_highlights': 2,
  'source': 'kindle',
  'title': 'Sed sit.',
  'url': 'https://example.com/url',
}

print(env.get_template(sys.argv[1]).render(data))