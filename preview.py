#!/usr/bin/env python

import sys

import data
from utils import outputToFileAndConsole

print('-- BOOK')
outputToFileAndConsole("examples/book.md", "src/highlight.jinja2", data.book)

print('-- ARTICLE')
outputToFileAndConsole("examples/article.md", "src/highlight.jinja2", data.article)

print('-- PODCAST')
outputToFileAndConsole("examples/podcast.md", "src/highlight.jinja2", data.podcast)

print('-- TWEET')
outputToFileAndConsole("examples/tweet.md", "src/highlight.jinja2", data.tweet)

print('-- PAGE META DATA')
outputToFileAndConsole("examples/page.md", "src/pageMetadata.jinja2", data.article)
