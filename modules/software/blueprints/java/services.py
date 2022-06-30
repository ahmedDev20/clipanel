
from cmd import services as cmd

def install(name):
    cmd.single_line_command("sudo apt-get install openjdk-17-jdk")
    return 'Ok'

def uninstall(name):
    cmd.single_line_command("sudo apt-get autoremove openjdk-17-jdk")
    return 'Ok'