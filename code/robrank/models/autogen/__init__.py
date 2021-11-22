import rich
c = rich.get_console()
c.print('''[white on red]
[!] Maybe you forgot to run `robrank/models/autogen/autogen.py` ?
    You can use the shortcut script: `$ bash tools/autogen.bash` as well.
''')
