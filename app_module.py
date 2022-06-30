import auth
import cmd
import modules.files
import modules.software

from flask import current_app as app

app.register_blueprint(auth.auth_app, url_prefix='/auth')
app.register_blueprint(cmd.cmd_app, url_prefix='/cmd')
app.register_blueprint(modules.files.files_app, url_prefix='/files')
app.register_blueprint(modules.software.software_app, url_prefix="/software")
