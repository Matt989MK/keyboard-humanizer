# This file is a copy of tests/test_keyboard_advanced.py for demo purposes.
# Run this script to see the advanced keyboard humanizer demo.

from keyboardhumanizer import KeyboardHumanizer

if __name__ == "__main__":
    humanizer = KeyboardHumanizer()
    print("Typing demo: 'The quick brown fox jumps over the lazy dog.'")
    humanizer.type_text("The quick brown fox jumps over the lazy dog.")
    print("Demo complete.") 