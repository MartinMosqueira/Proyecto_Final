from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

login_persona = Table('association', Base.metadata, Column('login_id', Integer, ForeignKey('login.id'))
                      )
class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer,
                   primary_key=True)
    nombre = db.Column(db.String(20),
                       index=False,
                       unique=False,
                       nullable=False)
    apellido = db.Column(db.String(30),
                         index=False,
                         unique=False,
                         nullable=False)
    modelo = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        login = Login.query.all()
        return login

    def __repr__(self):
        return '<Personas {}, {}>'.format(self.nombre, self.apellido)