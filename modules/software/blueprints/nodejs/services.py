from cmd import services as cmd

def install():
    if cmd.single_line_command('sudo apt-get install nodejs') == 0:
        return 'Ok'

def uninstall():
    if cmd.single_line_command('sudo apt-get autoremove nodejs') == 0:
        return 'Ok'

