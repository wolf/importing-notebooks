import jupyter_notebook_importer
from random import choice
from notebooks.My_Notebook import Foo

person = choice(["Wolf", "Miranda", "Ezay"])
foo = Foo()
foo.say_hello(person)
