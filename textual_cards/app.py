import pathlib
from random import shuffle
from typing import Optional

from rich.text import Text
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Footer, Label, Static

from .screens.pick_deck import PickDeckScreen
from .static.ctp_colors import ctp_green


def get_cards(path: str) -> list[str]:
    cards = pathlib.Path(path).read_text().splitlines()
    cards = [card for card in cards if card]  # no blank lines
    cards = [card for card in cards if not card.startswith("#")]  # no comment lines
    return cards


class CardsApp(App):
    BINDINGS = [
        Binding("left,h", "change_card(-1)", "Prev", key_display="←"),
        Binding("right,l", "change_card(1)", "Next", key_display="→"),
        Binding("space,j,k,up,down", "flip_card", "Flip", key_display="↑"),
        Binding("enter", "memorized", "Got it! 👍", key_display="⏎"),
        Binding("s", "shuffle_deck", "Shuffle"),
        Binding("r", "reset_deck", "Reset"),
        Binding("c", "change_deck", "Change"),
        # todo | this should push a screen with a list of all the memorized cards
        # todo | maybe the user can add selected cards back to the deck?
        Binding("m", "show_memorized", "Currently prints a list", show=False),
        Binding("q,escape", "app.quit", "Quit", show=False),
    ]
    SCREENS = {}
    CSS_PATH = "style.scss"

    deck_path = reactive(str)
    deck = reactive([])
    memorized_cards = reactive([])
    current_card_indx = reactive(int, always_update=True)
    current_question = reactive(str)
    current_answer = reactive(str)
    question_side = reactive(bool, always_update=True)

    def watch_deck_path(self) -> None:
        if self.deck_path:
            self.deck = get_cards(self.deck_path)
            self.current_card_indx = 0
            self.memorized_cards.clear()

    def watch_current_card_indx(self) -> None:
        """Triggers whenever current_card_indx is modified"""
        if len(self.deck) == 0:
            self.card_text.update("Well done! 🙌")
            self.current_card_num_label.update(f"")
            return

        # fyi if the pervious card was multi-lined and the new card is single, a graphical glitch occurs.
        # fyi quick remedy: clear the card text before updating it
        self.card_text.update("")

        current_card = self.deck[self.current_card_indx]
        self.current_question, self.current_answer = current_card.split("|")
        self.current_question = Text(self.current_question.strip())
        self.current_answer = Text(self.current_answer.strip())

        self.current_card_num_label.update(f"[{ctp_green}]{self.current_card_indx + 1}[/]/{len(self.deck)}")

        self.question_side = True

    def watch_question_side(self) -> None:
        if self.question_side:
            self.card_text.update(f"Q: [italic]{self.current_question}")
        else:
            self.card_text.update(f"[{ctp_green}]{self.current_answer}")

    def validate_current_card_indx(self, indx: int) -> int:
        """Provides looping effects, prevents deck from going out of bounds"""
        if indx < 0:
            indx = len(self.deck) - 1
        elif indx > len(self.deck) - 1:
            indx = 0
        return indx

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(id="Card"):
                self.card_text = Static(id="CardText")
                yield self.card_text

            with Horizontal(id="StatusBar"):
                self.current_card_num_label = Static(id="CardNumLabel")
                yield self.current_card_num_label
        yield Footer()

    def on_mount(self) -> None:
        self.push_screen(PickDeckScreen())

    def action_change_card(self, move_amt: int) -> None:
        self.current_card_indx += move_amt

    def action_flip_card(self) -> None:
        """Swap the self.questions_side attribute, which determines which side of the card is "side up" """
        # no flip card if no card to be flipped 😡
        if len(self.deck) == 0:
            return

        if self.question_side:
            self.question_side = False
        else:
            self.question_side = True

    def action_memorized(self) -> None:
        """Moves current card from self.deck to self.memorized"""
        # stop deck from doing out of bounds
        if len(self.deck) == 0:
            return

        card = self.deck[self.current_card_indx]
        self.memorized_cards.append(card)
        self.deck.remove(card)

        # fyi If the last card is memorized, while other cards are still present in self.deck, the deck goes out of bounds. This prevents that
        if self.current_card_indx == len(self.deck):
            self.current_card_indx -= 1

        # fyi because the card indx is set to auto update, nudging it like this refreshes the app
        self.current_card_indx = self.current_card_indx

    def action_shuffle_deck(self) -> None:
        shuffle(self.deck)
        self.current_card_indx = 0

    def action_reset_deck(self) -> None:
        """Move all the cards in self.memorized_cards back into the deck, shuffle it for goodluck"""
        self.deck.extend(self.memorized_cards)
        self.memorized_cards.clear()
        self.current_card_indx = 0
        self.action_shuffle_deck()

    def action_show_memorized(self) -> None:
        print(self.memorized_cards)

    def action_change_deck(self) -> None:
        self.push_screen(PickDeckScreen())


def main():
    app = CardsApp()
    app.run()
