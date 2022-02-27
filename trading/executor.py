import inquirer
from utils.api import Client
import asyncio

class Executor:
    def __init__(self, client):
        self.client = client
        self._init_strategy()
    
    def _init_strategy(self):
        questions = [
          inquirer.List('strat',
                        message="What strategy we using?",
                        choices=['KCB+RSI'],
                    ),
        ]
        answer = inquirer.prompt(questions)
        if answer['strat'] == 'KCB+RSI':
            self._kcb_rsi_strat()
    
    def _kcb_rsi_strat(self):
        self.client.get_pos()

        