#!/usr/bin/python

###########################################
# module: var.py
# description: var class for creating
# variable instances.
# bugs to vladimir kulyukin in canvas.
###########################################

class var(object):
    def __init__(self, name='var'):
        assert isinstance(name, str)
        self.__name__ = name

    def get_name(self):
        return self.__name__

    def __str__(self):
        return self.__name__
