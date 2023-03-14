# textual-cards

<!-- [![PyPI - Version](https://img.shields.io/pypi/v/textual-cards.svg)](https://pypi.org/project/textual-cards)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textual-cards.svg)](https://pypi.org/project/textual-cards) -->
**Table of Contents**

- [textual-cards](#textual-cards)
  - [About](#about)
  - [Installation](#installation)
    - [`pipx`](#pipx)
    - [Manual](#manual)
  - [Usage](#usage)
    - [Decks](#decks)
    - [Cards](#cards)
    - [Keyboard shortcuts](#keyboard-shortcuts)
  - [License](#license)

## About
`textual-cards` is a simple flashcard app built with [textual](https://github.com/Textualize/textual)

## Installation
_This is not a published package._

### `pipx`
> After publishing, this will be the preferred method
```console
pipx install <TBD>
```

### Manual
> If you, for whatever reason, want to use it *now*
```console
git clone https://github.com/joshpaulie/textual-cards
cd textual-cards
python -m venv .venv
<activate venv>
python -m pip -e install .
python -m textual_cards
```

## Usage
> **In development**: The app lacks some functionality as-is
> 
> To use the app during development, follow the [manual install](#manual) steps and read below
> 
> Anything annotated with 💤 are features yet to be implemented

1. [Install](#installation)
2. Run `cards` 💤
3. Your `~/decks` directory will be read, and a list of decks presented
4. Pick which deck to load up, start studying! 🤓

### Decks
Flashcards are collected as "deck" files, in the directory `~/decks`. This directory is recursively checked, allowing for the decks to be categorized into subdirectories

- These deck files can be named anything, but are "Pipe (`|`) seperated values" files
- Each line in the deck file considered a [card](#cards)

### Cards
- Cards are represented as line entries in your deck file
- They are pipe (`|`) seperated, each line using the syntax `Question | Answer`
- Blank lines are ignored
- Lines starting with `#` are considered comments and also ignored
- Cards are `.strip()`ed, meaning any spaces at the end or begining of your question or answer will be trimmed off, allowing for cards like
  - `How is bexli going to get this package & publish this app when he's done? | He has no idea!`

### Keyboard shortcuts
All keyboard shortcuts can be found in the footer, expect
- `q` or `escape` to exit the app

## License
`textual-cards` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
