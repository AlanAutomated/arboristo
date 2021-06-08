import pytest

from arboristo import __version__
from arboristo.arbor import Tree

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def return_dict():
    """
        "interfaces": {
            "Tunnel0": {
                "state": "UP"
            },
            "Tunnel1": {
                "state": "DOWN"
            }
        }
    }
    """
    return {"interfaces":{"Tunnel0":{"state":"UP"},"Tunnel1":{"state":"DOWN"}}}

def test_path_type():
    """A non-string value raises a type error"""
    with pytest.raises(TypeError):
        t = Tree()
        assert t.path()

def test_path_value():
    """Value of path is the argument passed to get()""" 
    t = Tree()
    t.get('abc')
    assert t.path == 'abc'

def test_path_not_none():
    """Calling from_dict() before get() raises a type error"""
    with pytest.raises(ValueError):
        t = Tree()
        assert t.from_dict()

def test_from_dict_type():
    """A non-dict value raises a type error"""
    with pytest.raises(TypeError):
        t = Tree()
        assert t.get('abc').from_dict('def')
    
def test_from_dict_empty():
    """An empty dict raises a value error"""
    with pytest.raises(ValueError):
        t = Tree()
        assert t.get('abc').from_dict({})

def test_source_value(return_dict):
    """Value of source is the argument passed to from_dict()""" 
    t = Tree()
    t.get('abc').from_dict(return_dict)
    assert t.source is return_dict

def test_return_value_count(return_dict):
    """The list should contain a single dictionary"""
    t = Tree()
    t.get('Tunnel0.state').from_dict(return_dict)
    assert len (t.branch) == 1

def test_return_path_key(return_dict):
    """The value of branch path is 'interfaces.Tunnel0.state'"""
    t = Tree()
    t.get('Tunnel0.state').from_dict(return_dict)
    assert t.branch[0]['path'] == 'interfaces.Tunnel0.state'

def test_return_value_key(return_dict):
    """The value of branch value is 'UP'"""
    t = Tree()
    t.get('Tunnel0.state').from_dict(return_dict)
    assert t.branch[0]['value'] == 'UP'