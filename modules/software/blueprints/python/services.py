
from cmd import services as cmd

def install():
    cmd.single_line_command("sudo apt-get install python3")
    return 'Ok'

def uninstall():
    cmd.single_line_command("sudo apt-get autoremove python3")
    return 'Ok'