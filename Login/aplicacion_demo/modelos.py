from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

tarjeta_persona = Table('association', Base.metadata,
                          Column('tarjeta_id', Integer, ForeignKey('tarjeta.id')),
                          Column('persona_id', Integer, ForeignKey('persona.id'))
                          )

class TarjetaPersona(db.Model):
    __tablename__ = 'tarjetapersona'
    tarjeta_id = Column(Integer, ForeignKey('tarjeta.id'), primary_key=True)
    persona_id = Column(Integer, ForeignKey('persona.id'), primary_key=True)

class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'
    id = db.Column(db.Integer,
                   primary_key=True)
    tipo = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    numero = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    cods= db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    vencimiento = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    montomax = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    
    
    personas = relationship("Persona", secondary='tarjetapersona')

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
        tarjetas = Tarjeta.query.all()
        return tarjetas

    def __repr__(self):
        return '<Tarjeta {}, {}, {}, {}, {}>'.format(self.tipo, self.numero, self.cods, self.vencimiento, self.montomax)

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
    tarjetas = relationship("Tarjeta", secondary='tarjetapersona')

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
