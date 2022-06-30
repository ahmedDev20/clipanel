from sqlalchemy.exc import SQLAlchemyError

from . import services, nodejs_cli
from modules.software.models import *


@nodejs_cli.command('install')
def install():
    if services.install() == 'Ok':
        try:
            soft = Software('SOFTWARE_INSTALL_NODEJS', 'nodejs', True)
            db.session.add(soft)
            db.session.commit()
            print("Nodejs installed succesfully")
            return 'Ok'

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print("Error installing nodejs", error)
            return error
    else:
        print("Error installing nodejs")
        soft = Software.query.filter_by(key='SOFTWARE_INSTALL_NODEJS').first()
        soft.installed = False
        db.session.commit()
        return None


@nodejs_cli.command('uninstall')
def install():
    if services.uninstall() == 'Ok':
        try:
            soft = Software.query.filter_by(key='SOFTWARE_INSTALL_NODEJS').first()
            soft.installed = False
            db.session.commit()

            print("Nodejs uninstalled succesfully")
            return 'Ok'

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print("Error uninstalling nodejs", error)
            return error
    else:
        print("Error uninstalling nodejs")
        return None

