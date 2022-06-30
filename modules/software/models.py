from database import db
from sqlalchemy.sql import func

class Software(db.Model):
    __tablename__ = 'software'
    cursor = None
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String(250), unique=True)  # module name + unique key ex : FTP_ADD_USER
    name = db.Column(db.String(250), unique=True, nullable=False)
    installed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    def __init__(self, key,  name, installed):
        self.key = key
        self.name = name
        self.installed = installed

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'installed': self.installed,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }