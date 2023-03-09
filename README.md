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
> If you, for whatever reason, want to use it *now*, follow these steps & read [usage](#usage)
```console
git clone https://github.com/joshpaulie/textual-cards
cd textual-cards
python -m venv .venv
<activate venv>
python -m pip -e install .
python -m textual_cards
```

## Usage
> These usage instructions are for the concept of the app. The app lacks most of this functionality as-is.
> To use the app during development, follow the [manual install](#manual) instructions
> 
> While inside the repo directory, edit the `deck` file with your pipe (`|`) seperated Q & A lines. Most of the following applies, but only 1 deck can be loaded at a time and it must be in the example one in repo
> 
> Anything annotated with 💤 are features yet to be implemented


After installation, run `cards` in your terminal. 💤 Your decks directory will be read, and a list presented. 💤 From this list you can pick which deck to load up 💤, and use the (hopefully intuitive) keyboard shortcuts 

### Decks
Flashcards are collected as "deck" files, in the directory `~/decks`. 💤 This file is recursively checked, allowing for the decks to be categorized into subdirectories 💤

- These deck files can be named anything, but are "Pipe (`|`) seperated values" files
- The left hand side of the `|` is the question, while the right is the answer
- Each line in the deck file considered a [card](#cards)

An example deck may look like
```
What is the powerhouse of the cell?|The mitochondria
Who is the best programmer? | bexli, of course
Textual is _________|So rad!
```

#### Cards
- Cards are `.strip()`ed, meaning any spaces at the end or begining of your question or answer will be trimmed off, allowing for cards like
  - `How is bexli going to get this package & publish this app? | He has has no idea!`

### Keyboard shortcuts
All keyboard shortcuts can be found in the footer, expect
- `q` or `escape` to exit the app

## License
`textual-cards` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
