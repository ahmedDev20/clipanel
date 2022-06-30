import click

from database import db
from . import services, python_app
from ... import Software


@python_app.cli.command("install")
def install():
    services.install()

    soft = Software('SOFTWARE_INSTALL_PYTHON', 'python', True)
    db.session.add(soft)
    db.session.commit()

    return 'Ok'

@python_app.cli.command("uninstall")
def uninstall():
    services.uninstall()

    soft = Software.query.filter_by(key='SOFTWARE_INSTALL_PYTHON').first()
    soft.installed = False
    db.session.commit()
    return 'Ok'
