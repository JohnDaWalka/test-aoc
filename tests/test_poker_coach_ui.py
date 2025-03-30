import pytest
import tkinter as tk
from poker_coach.ui import PokerCoachUI

@pytest.fixture
def app():
    root = tk.Tk()
    app = PokerCoachUI(root)
    yield app
    root.destroy()

def test_initial_state(app):
    assert app.hand_entry.get() == ""
    assert app.result_label.cget("text") == ""

def test_analyze_hand_empty(app):
    app.hand_entry.delete(0, tk.END)
    app.analyze_hand()
    assert app.result_label.cget("text") == ""

def test_analyze_hand_valid(app):
    app.hand_entry.insert(0, "AS KS QS JS TS")
    app.analyze_hand()
    assert "Analysis result for hand: AS KS QS JS TS" in app.result_label.cget("text")
