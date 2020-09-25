from random import random

import pytest
import viselica

dict_ = {'0t': '-', '1e': '-', '2s': '-', '3t': '-'}
join = {1: '9', 2: '1', 3: '1'}
WORDS = 'test'


def test_one():
    return_word = viselica.one(words=['test'])
    assert return_word == 'test'


def test_mask():
    mask_word = viselica.mask(word='test')
    print(mask_word)
    assert '-' in mask_word.get('0t')
    assert dict_ == mask_word


def test_game():
    result = viselica.game_s(word='test', d_=dict_, a='t')
    assert result == 't--t'


def test_jo():
    result = viselica.jo(d_=join)
    assert result == '911'
