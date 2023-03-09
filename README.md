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
> If you, for whatever reason, want to use it *now*, follow these steps
```console
git clone https://github.com/joshpaulie/textual-cards
cd textual-cards
python -m venv .venv
<activate venv>
python -m pip -e install .
python -m textual_cards
```

## Usage
> These usage instructions are for the concept of the app. The app lacks most of the functionality as-is. To use the app during development, follow the [manual install](#manual) instructions. While inside the repo directory, edit the `deck` file with your pipe (|) seperated Q & A cards

After installation, run `cards` in your terminal. Your decks directory will be read, and a list presented. From this list you can pick which deck to load up, and use the (hopefully intuitive) keyboard shortcuts

### Decks
Flashcards are collected as "deck" files, in the directory `~/decks`. This file is recursively checked, allowing for the decks to be categorized into subdirectories

These deck files can be named anything, but are "Pipe (`|`) seperated files." The left hand side is the question, while the right is the answer

An example deck may look like
```
What is the powerhouse of the cell?|The mitochondria
Who is the best programmer?|bexli, of course
Textual is _________|So rad!
```

### Keyboard shortcuts

## License
`textual-cards` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
