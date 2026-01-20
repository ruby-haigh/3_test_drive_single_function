"""
make_snippet("hello, my name is Ruby") => "hello, my name is Ruby"
make_snippet("hello, my nams is Ruby Imogen") => "hello, my name is Ruby ..."
make_snippet("") => ""
"""
from lib.make_snippet import *
def test_make_snippet():
    assert make_snippet("hello, my name is Ruby") == "hello, my name is Ruby"
    assert make_snippet("") == ""
    assert make_snippet("hello, my name is Ruby Imogen") == "hello, my name is Ruby ..."