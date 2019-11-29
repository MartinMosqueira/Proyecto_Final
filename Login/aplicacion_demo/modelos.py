from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer,
                   primary_key=True)
    nombre = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    apellido = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    documento = db.Column(db.String(80),
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
        personas = Persona.query.all()
        return personas

    def __repr__(self):
        return '<Persona {}, {}, {}>'.format(self.apellido, self.nombre, self.documento)
