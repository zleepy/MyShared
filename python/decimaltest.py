#!/usr/bin/env python

from decimal import *

def to_decimal(value):
    '''Convert a string to a Decimal
    
    Eventual culture specific decimal separators is
    replaced with a dot (.).
    
    '''
    try:
        return Decimal(value.replace(u',', u'.'))
    except DecimalException:
        return None

def test_value(value):
    print value, '=', to_decimal(value)

if __name__ == '__main__':
    print "==== Test 'to_decimal()' ===="
    
    print
    print "++ Should pass:"
    print
    test_value('123.412')
    test_value('123,412')
    test_value(' 12.34 ')
    test_value(' 12,34 ')
    
    print
    print "++ Should return 'None':"
    print
    test_value('-')
    test_value('text')
    test_value('5%')
