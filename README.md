# readwise-roam-template

[![Lint](https://github.com/natterstefan/readwise-roam-template/actions/workflows/lint.yml/badge.svg)](https://github.com/natterstefan/readwise-roam-template/actions/workflows/lint.yml)

## Requirements

```bash
python 3.8.0
```

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Add new dependencies
pip install <name of package>
pip freeze > requirements.txt
```

## Preview

Either copy and paste the Jinja2 templates into Readwise or run the following
command:

```bash
# EXAMPLE: python preview.py src/highlight.jinja2
python preview.py <path to the file>
```

## Docs

- Readwise
  - [How can I customize the Readwise to Roam Export?](https://help.readwise.io/article/112-how-can-i-customize-the-roam-export#title)
- Jinja
  - [Jina2 Documentation](https://jinja.palletsprojects.com/en/2.11.x/)
- How to Test Templates
  - [Jinja live parser](https://cryptic-cliffs-32040.herokuapp.com/)
    - An [updated version](https://stackoverflow.com/a/48907913/1238150) can be found here.
  - [qn7o/jinja2-live-parser: Jinja2 live (web) parser](https://github.com/qn7o/jinja2-live-parser)

## License

[MIT](./LICENSE)
