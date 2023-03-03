from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static


class Results(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Static("🐢")
