import getpass
import os.path
from colorama import Fore, Back, Style, init
from utils.api import Client

def main():
    
    # initilaise colorama
    init()
    
    # user input for live or backtest
    valid = False
    while not valid:
        mode = input("Live or Backtest: ")
        if mode.lower() == "live":
            print('You selected: ' + Fore.GREEN + mode)
            _live()
            valid = True
        elif mode.lower() == "backtest":
            print('You selected: ' + Fore.GREEN + mode)
            _backtest()
            valid = True
        else:
            print("Invalid input")

def _live():
    print(Fore.RED + "NOT READY")
    return
    api_key = input("Enter your ByBit API Key: ")
    api_secret = getpass.getpass(prompt='Enter your ByBit API Secret: ', stream=None)

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
    client = Client(api_key)
    print(Fore.WHITE + "Backtesting now...")
    print(client.intraday_query('BTC', 'USD', '5min', 'full'))

def _read_keys():
    myvars = {}
    with open(".secrets.txt") as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            myvars[name.strip()] = str(var)
    return myvars
    
if __name__ == "__main__":
    main()