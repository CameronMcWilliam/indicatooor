from trading.executor import Executor
import getpass
import os.path
from colorama import Fore, Back, Style, init
from utils.api import Client
from trading.backtest import Backtester
import inquirer

def main():
    
    # initilaise colorama
    init()
    
    questions = [
          inquirer.List('mode',
                        message="Mode selection",
                        choices=['Live', 'Backtest'],
                    ),
        ]
    answer = inquirer.prompt(questions)
    mode = answer['mode']
    if mode == 'Live':
        print('You selected: ' + Fore.GREEN + mode)
        _live()
    else:
        print('You selected: ' + Fore.GREEN + mode)
        _backtest()

def _live():
    if not os.path.isfile('.secrets.txt'):
        bb_api_key = input(Fore.WHITE + "Enter your ByBit API Key: ")   
        bb_api_secret = getpass.getpass(prompt='Enter your ByBit API Secret: ', stream=None)
        file_name = '.secrets.txt'
        f = open(file_name, 'a+')
        f.write('BB_Api=\''+bb_api_key+'\'')
        f.write('BB_Secret=\''+bb_api_secret+'\'')
        f.close()
        print(Fore.GREEN + 'Saved API Key')
    else:
        myvars = _read_keys()
        bb_api_key = myvars['BB_Api']
        bb_api_secret = myvars['BB_Secret']
    print(Fore.GREEN + 'Got API Key!' + Fore.WHITE)
    myvars = _read_keys()
    api_key = myvars['AV_Api']
    bb_api_key = bb_api_key.rstrip("\n")
    bb_api_secret = bb_api_secret.rstrip("\n")
    client = Client(api_key, bb_api_key, bb_api_secret)
    executor = Executor(client)
    

def _backtest():
    print(Fore.YELLOW + "WIP")
    if not os.path.isfile('.secrets.txt'):   
        api_key = input(Fore.WHITE + "Enter your AlphaVantage API Key: ")
        file_name = '.secrets.txt'
        f = open(file_name, 'a+')
        f.write('AV_Api=\''+api_key+'\'')
        f.close()
        print(Fore.GREEN + 'Saved API Key')
    else:
        myvars = _read_keys()
        api_key = myvars['AV_Api']
        print(Fore.GREEN + 'Got API Key!')
    client = Client(api_key, "stinky")
    print(Fore.WHITE + "Backtesting now...")
    back_trader = Backtester(client)
    

def _read_keys():
    myvars = {}
    with open(".secrets.txt") as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            myvars[name.strip()] = str(var)
    return myvars
    
if __name__ == "__main__":
    main()