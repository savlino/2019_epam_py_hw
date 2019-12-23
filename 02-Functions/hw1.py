"""
function returns array of latin letters in alphabet order in given range
, default values are: start='a', stop='z', step=1;
function accepts: single parameter as stop key,
two parameters as start and stop keys respectively,
three parameters as start, stop and step key respectively,

function also allows to accept a dictionary
to replace default letters for tranliteration
"""

import string


def letters_range(start='a', stop='z', step=1, **kwargs):
    letters = string.ascii_lowercase

    if type(start) != str or type(stop) != str:
        raise ValueError(
            'start and stop arguments should be single letter as string'
        )
    if len(start) > 1 or len(stop) > 1:
        raise ValueError(
            'start and stop arguments should be single letter, not word'
        )

    if stop == 'z':
        stop, start = start, 'a'
    start_index = letters.find(start.lower())
    stop_index = letters.find(stop.lower())

    if kwargs:
        for k in kwargs:
            letters = letters.replace(k, str(kwargs[k]))
    letters_arr = []

    if step < 0:
        for i in range(stop_index + 1, start_index + 1, -step):
            letters_arr.append(letters[i])
        letters_arr.reverse()
        return letters_arr

    for i in range(start_index, stop_index, step):
        letters_arr.append(letters[i])
    return letters_arr
