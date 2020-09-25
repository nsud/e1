from random import random

import pytest
import visilica

dict_ = {'0t': '-', '1e': '-', '2s': '-', '3t': '-'}
join = {1: '9', 2: '1', 3: '1'}
WORDS = 'test'


def test_one():
    return_word = visilica.one(words=['test'])
    assert return_word == 'test'


def test_mask():
    mask_word = visilica.mask(word='test')
    print(mask_word)
    assert '-' in mask_word.get('0t')
    assert dict_ == mask_word


def test_game():
    result = visilica.game_s(word='test', d_=dict_, a='t')
    assert result == 't--t'


def test_jo():
    result = visilica.jo(d_=join)
    assert result == '911'
