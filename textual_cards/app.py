import pathlib

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Label, Static


def get_cards(path):
    cards = pathlib.Path(path).read_text().splitlines()
    cards = [card for card in cards if card]  # no blank lines
    cards = [card for card in cards if not card.startswith("#")]  # no comment lines
    return cards


class Cards(App):
    BINDINGS = [
        Binding("left,h", "change_card(-1)", "Prev"),
        Binding("right,l", "change_card(1)", "Next"),
        Binding("space", "flip_card", "Flip"),
    ]
    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:  # type: ignore
        self.card_text = Static("Welcome!", id="CardText")
        yield self.card_text
        yield Footer()
        self.current_card_num_label = Label(id="CardNumLabel")
        yield self.current_card_num_label

    def on_mount(self):
        self.cards = get_cards("deck")
        self.current_card_indx = 0
        self.action_change_card(0)
        self.question_side = True

    def action_change_card(self, move_amt):
        # Creates a looping effect where the last card
        # wraps to the first and vice versa
        if self.current_card_indx == 0 and move_amt == -1:
            self.current_card_indx = len(self.cards) - 1
        elif self.current_card_indx == len(self.cards) - 1 and move_amt == 1:
            self.current_card_indx = 0
        else:
            self.current_card_indx += move_amt
        self.question_side = True

        card = self.cards[self.current_card_indx]
        question, _ = card.split("|")
        self.card_text.update(f"[red]Question[/]: {question}")
        self.current_card_num_label.update(f"{self.current_card_indx + 1}/{len(self.cards)}")

    def action_flip_card(self):
        card = self.cards[self.current_card_indx]
        question, answer = card.split("|")
        if self.question_side:
            self.card_text.update(f"[red]Answer[/]: {answer}")
            # ? Could this be question_side = not question_side
            # Maybe. 😌
            self.question_side = False
        else:
            self.card_text.update(f"[red]Question[/]: {question}")
            self.question_side = True
