import parce as pe
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

def print_header():
    print(Fore.CYAN + Style.BRIGHT + r"""
  __  __       _        
 |  \/  |     (_)       
 | \  / | __ _ _ _ __   
 | |\/| |/ _` | | '_ \  
 | |  | | (_| | | | | | 
 |_|  |_|\__,_|_|_| |_| 
    """)

def print_menu():
    print(Back.GREEN + Fore.WHITE + Style.BRIGHT + "======================================/n")
    print( "             MAIN MENU                ")
    print(Back.GREEN + Fore.WHITE + Style.BRIGHT + "======================================")
    print(Fore.YELLOW + "[1] Option 1 - EVALUAR LENGUAJE")
    print(Fore.RED + "[4] Exit")
    print(Back.GREEN + Fore.WHITE + Style.BRIGHT + "======================================")
    print(Fore.WHITE + "Select an option by entering a number:")

def print_footer():
    print(Fore.CYAN + Style.BRIGHT + "======================================")
    print(Fore.CYAN + Style.BRIGHT + "              GRACIAS                 ")
    print(Fore.CYAN + Style.BRIGHT + "======================================")

def evaluate_language():
    name = input(Fore.YELLOW + "BUENOS DIAS PORFAVOR poner la dirrección de archivo separado por \\ LEER README  :  ")
    z = pe.readFile(name)
    y = pe.parce_program(z)
    # Assuming y should be the actual result of parce_program, not hardcoded to False
    if y:
        print(Fore.GREEN + """
                     __
                     .'  '.
                 _.-'/  |  \\
    ,        _.-"  ,|  /  0 `-.
    |\\    .-"       `--""-.__.'=====================-,
    \\ '-'`        .___.--._)=========================|
     \\            .'      |                           |
      |     /,_.-'        |                           |
    _/   _.'(             |     TRUE                  |
   /  ,-' \\  \\            |                           |
   \\  \\    `-'            |                           |
    `-'                   '-------------------------- '
""")
    else:
        print(Fore.RED + """
                     __
                     .'  '.
                 _.-'/  |  \\
    ,        _.-"  ,|  /  0 `-.
    |\\    .-"       `--""-.__.'=====================-,
    \\ '-'`        .___.--._)=========================|
     \\            .'      |                           |
      |     /,_.-'        |                           |
    _/   _.'(             |       False               |
   /  ,-' \\  \\            |                           |
   \\  \\    `-'            |                           |
    `-'                   '-------------------------- '
""")

def main():
    while True:
        print_header()
        print_menu()
        choice = input()

        if choice == "1":
            evaluate_language()
        elif choice == "4":
            print_footer()
            break
        else:
            print(Fore.RED + "Invalid selection, please try again.")

if __name__ == "__main__":
    main()
