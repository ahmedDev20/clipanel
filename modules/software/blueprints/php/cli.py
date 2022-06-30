import click

from database import db
from . import services, php_app
from ... import Software


@php_app.cli.command("install")
def install():
    services.install()

    soft = Software('SOFTWARE_INSTALL_PHP', 'php', True)
    db.session.add(soft)
    db.session.commit()

    return 'Ok'


@php_app.cli.command("uninstall")
def uninstall():
    services.uninstall()

    soft = Software.query.filter_by(key='SOFTWARE_INSTALL_PHP').first()
    soft.installed = False
    return 'Ok'