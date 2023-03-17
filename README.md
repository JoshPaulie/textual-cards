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
      - [Custom *Deck Path*](#custom-deck-path)
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
2. Create `~/decks` directory, create your [deck](#decks) files
3. Run `cards` 💤
4. Pick which deck to load up, start studying! 🤓

### Decks
Flashcards are collected as "deck" files, in the directory `~/decks`. This directory is recursively checked, allowing for the decks to be categorized into subdirectories

- These deck files can be named anything, but are "Pipe (`|`) seperated values" files
- Each line in the deck file considered a [card](#cards)
- Check out this [example deck](sample_deck.txt)

#### Custom *Deck Path*
If you don't like `~/decks`, and directory can be specified. Simply set an environment variable for `DECK_PATH`
- `export DECK_PATH=path/to/deck/files` ← Add to your shell rc Linux/MacOS
- [Windows instructions](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3#saving-environment-variables-with-the-system-control-panel)

### Cards
- are represented as line entries in your deck file
- are pipe (`|`) seperated, each line using the syntax `Question | Answer`
- ignore blank lines
- ignore lines starting with `#` (comments)
- can be styled with Rich's "[Console Markup](https://rich.readthedocs.io/en/latest/markup.html)"
  - for example `The [green]mitochondria[/] is the _____ of the cell?`
- ignore trailing and leading whitespace (tabs, spaces), allowing for cards like
  - `How is bexli going to get this package & publish this app when he's done? | He has no idea!`

### Keyboard shortcuts
All keyboard shortcuts can be found in the footer, expect
- `q` or `escape` to exit the app

## License
`textual-cards` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
