from database import db
from . import services, java_app
from ... import Software


@java_app.cli.command("install")
def install():
    soft = Software('SOFTWARE_INSTALL_JAVA', 'java', True)

    db.session.add(soft)
    db.session.commit()

    services.install()
    return 'Ok'

@java_app.cli.command("uninstall")
def uninstall():
    services.uninstall()

    soft = Software.query.filter_by(key='SOFTWARE_INSTALL_JAVA').first()
    soft.installed = False
    db.session.commit()
    return 'Ok'

