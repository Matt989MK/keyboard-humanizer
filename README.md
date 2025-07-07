# Keyboard Humanizer

Human-like keyboard automation for Python.

## Installation

```bash
pip install keyboardhumanizer
```

## Features

- Realistic human typing simulation (speed, errors, corrections, pauses)
- Supports multiple typing profiles (casual, professional, etc.)
- **NEW:** Occasionally makes a spelling mistake and does NOT fix it, for extra realism!
- Context-aware typing (emails, code, etc.)
- Copy-paste and quick alt-tab simulation
- Advanced demo and interactive CLI

## Usage

```python
from keyboardhumanizer import KeyboardHumanizer

humanizer = KeyboardHumanizer()
humanizer.type_text("Hello, this is a human-like typing demo!")
```

Or run the advanced demo:

```bash
python demo_advanced.py
```

## License

MIT 