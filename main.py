from colorama import Fore, Back, Style, init
import getpass

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
    print(Fore.WHITE + "WIP")
    api_key = input("Enter your ByBit API Key: ")
    api_secret = getpass.getpass(prompt='Enter your ByBit API Secret: ', stream=None)

def _backtest():
    print(Fore.WHITE + "WIP")
    
if __name__ == "__main__":
    main()