num_2_word
==========

A python function that returns the english word for a given integer up to 999,999,999,999,999.

Example usage:

>>> from num_2_word import num_2_word
>>> num_2_word(100)
'one hundred'
>>> num_2_word(1000001)
'one million and one'
>>> num_2_word(1000000021)
'one billion and twenty-one'
>>> num_2_word(000)
