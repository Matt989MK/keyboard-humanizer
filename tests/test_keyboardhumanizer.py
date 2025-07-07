import pytest
from keyboardhumanizer import type_text, press_key, hotkey

def test_type_text():
    type_text('Hello, world!')
    # No assertion: just check for errors

def test_press_key():
    press_key('enter')
    # No assertion: just check for errors

def test_hotkey():
    hotkey('ctrl', 'a')
    # No assertion: just check for errors 