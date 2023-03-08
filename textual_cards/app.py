import pathlib
from random import shuffle
from typing import Optional

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Footer, Label, Static


class DoneScreen(Screen):
    # todo app should totally exit (and eventually lead to a list of decks)
    BINDINGS = [("escape,space", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        with Container(id="DoneContainer"):
            yield Static("Congrats! You've finished this deck. 🎉", id="CongratsStatic")


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
        Binding("r", "reset_deck", "Reset"),
        # todo | this should push a screen with a list of all the memorized cards
        # todo | maybe the user can add selected cards back to the deck?
        Binding("m", "show_memorized", "Currently prints a list", show=False),
    ]
    SCREENS = {"DoneScreen": DoneScreen}
    CSS_PATH = "style.scss"

    deck = reactive([])
    memorized_cards = reactive([])
    current_card_indx = reactive(int, always_update=True)
    current_question = reactive(str)
    current_answer = reactive(str)
    question_side = reactive(bool)

    def watch_current_card_indx(self):
        current_card = self.deck[self.current_card_indx]
        self.current_question, self.current_answer = current_card.split("|")
        self.card_text.update(f"Q: [italic]{self.current_question}")
        self.current_card_num_label.update(f"[#a6da95]{self.current_card_indx + 1}[/]/{len(self.deck)}")

        self.question_side = True

    def watch_question_side(self):
        if self.question_side:
            self.card_text.update(f"Q: [italic]{self.current_question}")
        else:
            self.card_text.update(f"[#a6da95]{self.current_answer}")

    # def validate_current_card_indx(self, indx: int):
    #     # Figure out if this would prevent an out of bound expection
    #     # or if I can move the wrapping logic here (? maybe 🤔)
    #     pass

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(id="Card"):
                self.card_text = Static(id="CardText")
                yield self.card_text

            with Horizontal(id="StatusBar"):
                self.current_card_num_label = Static(id="CardNumLabel")
                yield self.current_card_num_label

        yield Footer()

    def on_mount(self):
        self.deck = get_cards("deck")
        self.action_change_card(0)

    def action_change_card(self, move_amt):
        # Creates a looping effect where the last card
        # wraps to the first and vice versa
        if self.current_card_indx == 0 and move_amt == -1:
            self.current_card_indx = len(self.deck) - 1
        elif self.current_card_indx == len(self.deck) - 1 and move_amt == 1:
            self.current_card_indx = 0
        else:
            self.current_card_indx += move_amt

    def action_flip_card(self):
        if self.question_side:
            self.question_side = False
        else:
            self.question_side = True

    def action_memorized(self):
        card = self.deck[self.current_card_indx]
        self.memorized_cards.append(card)
        self.deck.remove(card)

        if self.current_card_indx == len(self.deck):
            self.current_card_indx -= 1

        # ! Checking if the deck is out of cards needs to be moved
        # ! Rn, moving the removing the last card crashes the app (out of bounds)
        if len(self.deck) == 0:
            self.push_screen("DoneScreen")
            self.card_text.update("Well done! 🙌")
        else:
            # fyi because the card indx is set to auto update, nudging it like this refreshes the app
            self.current_card_indx += 0

    def action_shuffle_deck(self):
        shuffle(self.deck)
        self.action_change_card(-self.current_card_indx)

    def action_reset_deck(self):
        self.deck.extend(self.memorized_cards)
        self.memorized_cards.clear()
        self.action_change_card(-self.current_card_indx)
        self.action_shuffle_deck()

    def action_show_memorized(self):
        print(self.memorized_cards)


def main():
    app = CardsApp()
    app.run()
