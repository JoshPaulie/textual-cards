import pathlib
from random import shuffle
from typing import Optional

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Label, Static

from .screens.results import Results


def get_cards(path):
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
    ]
    SCREENS = {"results": Results}
    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:  # type: ignore
        self.card_text = Static(id="CardText")
        yield self.card_text
        yield Footer()
        self.current_card_num_label = Label(id="CardNumLabel")
        yield self.current_card_num_label

    def on_mount(self):
        self.deck = get_cards("deck")
        self.current_card_indx = 0
        self.current_question = ""
        self.current_answer = ""
        self.action_change_card(0)
        self.question_side = True
        self.memorized_cards = []
        self.init_deck_len = len(self.deck)

    def update_current_num_label(self):
        self.current_card_num_label.update(f"{self.current_card_indx + 1}/{len(self.deck)}")

    def action_change_card(self, move_amt):
        # Creates a looping effect where the last card
        # wraps to the first and vice versa
        if self.current_card_indx == 0 and move_amt == -1:
            self.current_card_indx = len(self.deck) - 1
        elif self.current_card_indx == len(self.deck) - 1 and move_amt == 1:
            self.current_card_indx = 0
        else:
            self.current_card_indx += move_amt

        card = self.deck[self.current_card_indx]
        self.current_question, self.current_answer = card.split("|")

        self.action_flip_card(question_side_up=True)
        self.update_current_num_label()

    def action_flip_card(self, question_side_up: Optional[bool] = None):
        formatted_question = f"Q: [italic]{self.current_question}"

        # used with self.change_card()
        if question_side_up:
            self.question_side = True
            self.card_text.update(formatted_question)
            return

        # If not used with change card, flip the card back and forth
        if self.question_side:
            self.card_text.update(self.current_answer)
            self.question_side = False
        else:
            self.card_text.update(formatted_question)
            self.question_side = True

    def action_memorized(self):
        card = self.deck[self.current_card_indx]
        self.deck.remove(card)
        self.action_change_card(0)
        self.update_current_num_label()

    def action_shuffle_deck(self):
        shuffle(self.deck)
        self.action_change_card(-self.current_card_indx)


def main():
    app = CardsApp()
    app.run()
