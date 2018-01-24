from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class InstructionsRead(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [Instructions, InstructionsRead]
