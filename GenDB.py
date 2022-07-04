from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgresql@localhost:5432/pasticceria"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Persone(db.Model):
    __tablename__ = 'persone'

    Mail = db.Column(db.String(), primary_key=True)
    Nome = db.Column(db.String())
    Cognome = db.Column(db.String())
    DataNascita = db.Column(db.Date())
    Telefono = db.Column(db.String())
    Rating = db.Column(db.Integer)

    def __init__(self, Mail, Nome, Cognome, DataNascita, Telefono, Rating):
        self.Mail = Mail
        self.Nome = Nome
        self.Cognome = Cognome
        self.DataNascita = DataNascita
        self.Telefono = Telefono
        self.Rating = Rating

    def __repr__(self):
        return f"<Persona {self.Mail}>"

class Dipendenti(db.Model):
    __tablename__ = 'dipendenti'

    Mail = db.Column(db.String(), primary_key=True) #da fare relazione
    Username = db.Column(db.String())
    Password = db.Column(db.String())
    DataAssunzione = db.Column(db.Date())

    Id_Stipendio = relationship("stipendi") #da fare relazione
    Articoli = relationship("blog", back_populates='dipendenti')
    Turni = relationship("personaleTurni", back_populates='dipendenti')

    def __init__(self, Mail, User, Password, DataAssunzione):
        self.Mail = Mail
        self.Username = User
        self.Password = Password
        self.DataAssunzione = DataAssunzione

    def __repr__(self):
        return f"<Dipendente {self.Mail}>"

class Clienti(db.Model):
    __tablename__ = 'clienti'

    Mail = db.Column(db.String(), primary_key=True) #da fare relazione
    Username = db.Column(db.String())
    Password = db.Column(db.String())
    DataRegistrazione = db.Column(db.Date())

    def __init__(self, Mail, User, Password, DataRegistrazione):
        self.Mail = Mail
        self.Username = User
        self.Password = Password
        self.DataRegistrazione = DataRegistrazione

    def __repr__(self):
        return f"<Cliente {self.Mail}>"

class Fornitori(db.Model):
    __tablename__ = 'fornitori'

    Mail = db.Column(db.String(), primary_key=True) #da fare relazione
    Ditta = db.Column(db.String())
    PartitaIVA = db.Column(db.String())

    Id_DDT = relationship("DDT") #da fare

    def __init__(self, Mail, Ditta, PartitaIVA):
        self.Mail = Mail
        self.Ditta = Ditta
        self.PartitaIVA = PartitaIVA

    def __repr__(self):
        return f"<Fornitore {self.Mail}>"

class DDT(db.Model):
    __tablename__ = 'ddt'

    Id = db.Column(db.Integer(), primary_key=True)
    Mail_Fornitore = db.Column(db.String(), ForeignKey("fornitori.Mail")) #da fare
    DataEmissione = db.Column(db.Date())
    Note = db.Column(db.String(500))    #q.tà dei beni trasportati per voce, aspetto esteriore, descrizione
    Importo = db.Column(db.Double())
    Peso = db.Column(db.Double())
    Colli = db.Column(db.Integer())

    def __init__(self, Id, Mail_Fornitore, DataEmissione, Note, Importo, Peso, Colli):
        self.Id = Id
        self.Mail_Fornitore = Mail_Fornitore
        self.DataEmissione = DataEmissione
        self.Note = Note
        self.Importo = Importo
        self.Colli = Colli
        self.Peso = Peso

    def __repr__(self):
        return f"<DDT {self.Id}>"

class Stipendi(db.Model):
    __tablename__ = 'stipendi'

    Id = db.Column(db.Integer(), primary_key=True)
    Mail_Dipendenti = db.Column(db.String(), ForeignKey("dipendenti.Mail")) #da fare
    DataEmissione = db.Column(db.Date())
    ImportoNetto = db.Column(db.Double())

    def __init__(self, Id, Mail_Dipedendente, DataEmissione, ImportoNetto):
        self.Id = Id
        self.Mail_Dipendenti = Mail_Dipedendente
        self.DataEmissione = DataEmissione
        self.ImportoNetto = ImportoNetto

    def __repr__(self):
        return f"<Stipendi {self.Id}>"

class Articoli(db.Model):
    __tablename__ = 'blog'

    Id = db.Column(db.Integer(), primary_key=True)
    Titolo = db.Column(db.String())
    Contenuto = db.Column(db.String())
    DataPubblicazione = db.Column(db.Date())

    Dipendente = relationship("blog", back_populates='articoli')

    def __init__(self, Id, Titolo, Contenuto, DataPubblicazione):
        self.Id = Id
        self.Titolo = Titolo
        self.Contenuto = Contenuto
        self.DataPubblicazione = DataPubblicazione

    def __repr__(self):
        return f"<Articolo {self.Titolo}>"

#assciazione diendeti articoli
class Blog(db.Model):
    __tablename__ = 'blog'

    Mail_Dipendente = db.Column(ForeignKey('dipendenti.Mail'), primary_key = True)
    Id_Articolo = db.Column(ForeignKey('articoli.Id'), primary_key = True)


class Turni(db.Model):
    __tablename__ = 'turni'

    Id = db.Column(db.Integer(), primary_key=True)
    Nome = db.Column(db.String())
    OraInizio = db.Column(db.Time())
    OraFine = db.Column(db.Time())
    CompensoOrario = db.Column(db.Double())

    Dipendente = relationship("personaleTurni", back_populates='turni')

    def __init__(self, Id, Nome, OraInizio, OraFine, CompensoOrario):
        self.Id = Id
        self.Nome = Nome
        self.OraInizio = OraInizio
        self.OraFine = OraFine
        self.CompensoOrario = CompensoOrario

    def __repr__(self):
        return f"<Turni {self.Titolo}>"

#assciazione personale turni
class PersonaleTurni(db.Model):
    __tablename__ = 'personaleTurni'

    Mail_Dipendente = db.Column(ForeignKey('dipendenti.Mail'), primary_key=True)
    Id_Turno = db.Column(ForeignKey('turni.Id'), primary_key=True)
    Data = db.Column(db.Date())
    OraInizio = db.Column(db.Time())
    OraFine = db.Column(db.Time())

class Semilavorati(db.Model):
    __tablename__ = 'semilavorati'

    Id = db.Column(db.Integer(), primary_key=True)
    Nome = db.Column(db.String())
    Quantità = db.Column(db.Integer())
    Prezounitario = db.Column(db.Double())

    #relazioni da fare

    def __init__(self, Id, Nome, Quantità, Prezzounitario):
        self.Id = Id
        self.Nome = Nome
        self.Quantità = Quantità
        self.Prezounitario = Prezzounitario

    def __repr__(self):
        return f"<Semilavorati {self.Titolo}>"






