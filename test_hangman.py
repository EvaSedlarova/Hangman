import hangman
import pytest
from io import StringIO

def test_choose_word():
    "Test, zda se se vybere slovo z listu"
    assert hangman.choose_word() == "aftershock" or "background" or "trampoline" or "cat"

def test_set_stage():
    "Testuji, zda se nastaví prázdné pole o správném počtu znaků"
    lenght = hangman.set_stage("aftershock")
    assert len(lenght) == 10

inputs = StringIO('a\n')

def test_input_letter(monkeypatch):
    "Testuji, zda vrátí správný výsledek, při zadání písměna ve slově"
    monkeypatch.setattr('sys.stdin', inputs)
    assert hangman.input_letter('--c--') == 'a'


@pytest.mark.parametrize('stage, output', [('-------', 'GAME OVER'), # prázdné pole
                                          ('troubl-', 'GAME OVER'), # 2 znaky
                                          ('nope', 'YOU WON!' )] # plné pole
)

def test_game_result(stage, output):
    "Testuji, zda vrátí správný výsledek hry"
    assert hangman.game_result(stage) == output

