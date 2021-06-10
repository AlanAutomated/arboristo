# arboristo
[![Build Status](https://github.com/AlanAutomated/arboristo/workflows/CI/badge.svg)](https://github.com/AlanAutomated/arboristo/actions)
[![codecov](https://codecov.io/gh/AlanAutomated/arboristo/branch/master/graph/badge.svg?token=IYHABMICSN)](https://codecov.io/gh/AlanAutomated/arboristo) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/7c212a68576d4536a08a4a448361b497)](https://www.codacy.com/gh/AlanAutomated/arboristo/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AlanAutomated/arboristo&amp;utm_campaign=Badge_Grade) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)

A light-weight package to lazily traverse a deeply nested dictionary.

![demo](https://raw.githubusercontent.com/AlanAutomated/arboristo/master/demo.gif)

## Installation
```
pip install arboristo
```

## Basic Usage

```python
>>> from arboristo.arbor import Tree
>>>
>>> t = Tree()
>>>
>>> my_dict = {
...   "a": {
...     "b": "bar",
...     "c": {
...       "d": {
...         "e": {
...           "f": "foo"
...         }
...       }
...     }
...   }
... }
>>>
>>> print(t.get('b').from_dict(my_dict))
[{'path': 'a.b', 'value': 'bar'}]
>>>
>>> print(t.get('a.d.f').from_dict(my_dict))
[{'path': 'a.c.d.e.f', 'value': 'foo'}, {'path': 'a.c.d.e', 'value': {'f': 'foo'}}]
```