
from cmd import services as cmd

def install():
    cmd.single_line_command("sudo apt-get install php")
    return 'Ok'

def uninstall():
    cmd.single_line_command("sudo apt-get autoremove php")
    return 'Ok'