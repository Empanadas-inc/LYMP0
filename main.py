import parce as pe


def run_program():
    name = "pruebas.txt"
    z = pe.readFile(name)
    y = pe.parce_program(y)
    if z == True:
        print("""
                     __
                     .'  '.
                 _.-'/  |  \\
    ,        _.-"  ,|  /  0 `-.
    |\\    .-"       `--""-.__.'=====================-,
    \\ '-'`        .___.--._)=========================|
     \\            .'     | Tu programa funciona      |
      |     /,_.-'        |                           |
    _/   _.'(             |                           |
   /  ,-' \\  \\          |                           |
   \\  \\    `-'          |                           |
    `-'                   '-------------------------- '
""")
    else:
         print("""
                     __
                     .'  '.
                 _.-'/  |  \\
    ,        _.-"  ,|  /  0 `-.
    |\\    .-"       `--""-.__.'=====================-,
    \\ '-'`        .___.--._)=========================|
     \\            .'     | Tu programa no funciona   |
      |     /,_.-'        |                           |
    _/   _.'(             |                           |
   /  ,-' \\  \\          |                           |
   \\  \\    `-'          |                           |
    `-'                   '-------------------------- '
""")

print(run_program())