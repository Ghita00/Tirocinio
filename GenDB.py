from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgresql@localhost:5432/pasticceria"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#TODO setta CASCADE, NOT NULL, LIM STRINGHE

class Persone(db.Model):
    __tablename__ = 'persone'

    Mail = db.Column(db.String(), primary_key=True)
    Nome = db.Column(db.String())
    Cognome = db.Column(db.String())
    DataNascita = db.Column(db.Date())
    Telefono = db.Column(db.String())
    Rating = db.Column(db.Integer)

    Dipedenti = relationship("Dipendenti")
    Clienti = relationship("Clienti")
    Fornitori = relationship("Fornitori")

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

    Mail = db.Column(ForeignKey('persone.Mail', ondelete='CASCADE'), primary_key = True)
    Username = db.Column(db.String())
    Password = db.Column(db.String())
    DataAssunzione = db.Column(db.Date())

    Id_Stipendio = relationship("Stipendi") #da fare relazione

    Articoli = relationship("Blog", back_populates='dipendenti',  cascade="all, delete-orphan")
    Turni = relationship("PersonaleTurni", back_populates='dipendenti',  cascade="all, delete-orphan")

    def __init__(self, Mail, User, Password, DataAssunzione):
        self.Mail = Mail
        self.Username = User
        self.Password = Password
        self.DataAssunzione = DataAssunzione

    def __repr__(self):
        return f"<Dipendente {self.Mail}>"

class Clienti(db.Model):
    __tablename__ = 'clienti'

    Mail = db.Column(ForeignKey('persone.Mail', ondelete='CASCADE'), primary_key = True)
    Username = db.Column(db.String())
    Password = db.Column(db.String())
    DataRegistrazione = db.Column(db.Date())

    Semilavorato_WishList = relationship("WishList", back_populates='clienti',  cascade="all, delete-orphan")
    Semilavorato_Carrello = relationship("Carrello", back_populates='clienti',  cascade="all, delete-orphan")

    def __init__(self, Mail, Username, Password, DataRegistrazione):
        self.Mail = Mail
        self.Username = Username
        self.Password = Password
        self.DataRegistrazione = DataRegistrazione

    def __repr__(self):
        return f"<Cliente {self.Mail}>"

class Fornitori(db.Model):
    __tablename__ = 'fornitori'

    Mail = db.Column(ForeignKey('persone.Mail', ondelete='CASCADE'), primary_key = True)
    Ditta = db.Column(db.String())
    PartitaIVA = db.Column(db.String())

    Id_DDT = relationship("DDT")
    Id_FatturaAcquisto = relationship("FattureAcquisto")

    def __init__(self, Mail, Ditta, PartitaIVA):
        self.Mail = Mail
        self.Ditta = Ditta
        self.PartitaIVA = PartitaIVA

    def __repr__(self):
        return f"<Fornitore {self.Mail}>"

class DDT(db.Model):
    __tablename__ = 'ddt'

    Id = db.Column(db.Integer(), primary_key=True)
    Mail_Fornitore = db.Column(db.String(), ForeignKey("fornitori.Mail", ondelete='CASCADE'))
    NumDocumento = db.Column(db.Integer())
    DataEmissione = db.Column(db.Date())
    Note = db.Column(db.String(500))    #q.tà dei beni trasportati per voce, aspetto esteriore, descrizione
    Importo = db.Column(db.Float())
    Peso = db.Column(db.Float())
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
    Mail_Dipendenti = db.Column(db.String(), ForeignKey('dipendenti.Mail', ondelete='CASCADE')) #da fare, VEDI SE VA MESSO
    DataEmissione = db.Column(db.Date())
    ImportoNetto = db.Column(db.Float())

    def __init__(self, Id, Mail_Dipedendente, DataEmissione, ImportoNetto):
        self.Id = Id
        self.Mail_Dipendenti = Mail_Dipedendente
        self.DataEmissione = DataEmissione
        self.ImportoNetto = ImportoNetto

    def __repr__(self):
        return f"<Stipendi {self.Id}>"

class Articoli(db.Model):
    __tablename__ = 'articoli'

    Id = db.Column(db.Integer(), primary_key=True)
    Titolo = db.Column(db.String())
    Contenuto = db.Column(db.String())
    DataPubblicazione = db.Column(db.Date())

    Dipendente = relationship("Blog", back_populates='articoli', cascade="all, delete-orphan")

    def __init__(self, Id, Titolo, Contenuto, DataPubblicazione):
        self.Id = Id
        self.Titolo = Titolo
        self.Contenuto = Contenuto
        self.DataPubblicazione = DataPubblicazione

    def __repr__(self):
        return f"<Articolo {self.Id}>"

class Turni(db.Model):
    __tablename__ = 'turni'

    Id = db.Column(db.Integer(), primary_key=True)
    Nome = db.Column(db.String())
    OraInizio = db.Column(db.Time())
    OraFine = db.Column(db.Time())
    CompensoOrario = db.Column(db.Float())

    Dipendente = relationship("PersonaleTurni", back_populates='turni', cascade="all, delete-orphan")

    def __init__(self, Id, Nome, OraInizio, OraFine, CompensoOrario):
        self.Id = Id
        self.Nome = Nome
        self.OraInizio = OraInizio
        self.OraFine = OraFine
        self.CompensoOrario = CompensoOrario

    def __repr__(self):
        return f"<Turni {self.Id}>"

class Semilavorati(db.Model):
    __tablename__ = 'semilavorati'

    Id = db.Column(db.Integer(), primary_key=True)
    Nome = db.Column(db.String())
    Quantità = db.Column(db.Integer())
    PrezzoUnitario = db.Column(db.Float())
    IVA = db.Column(db.Float())
    Preparazione = db.Column(db.String())

    Scontrini = relationship("ScontriniSemilavorati", back_populates='semilavorati',  cascade="all, delete-orphan")
    MateriePrime = relationship("Ricette", back_populates='semilavorati', cascade="all, delete-orphan")
    Cliente_WishList = relationship("WishList", back_populates='semilavorati',  cascade="all, delete-orphan")
    Cliente_Carrello = relationship("Carrello", back_populates='semilavorati',  cascade="all, delete-orphan")
    ProduzioneGiornaliera = relationship("Produzione", back_populates='semilavorati',  cascade="all, delete-orphan")
    FatturaVendita = relationship("ContenutoVenditaSemilavorati", back_populates='semilavorati', cascade="all, delete-orphan")

    def __init__(self, Id, Nome, Quantità, PrezzoUnitario, IVA, Preparazione):
        self.Id = Id
        self.Nome = Nome
        self.Quantità = Quantità
        self.PrezzoUnitario = PrezzoUnitario
        self.IVA = IVA
        self.Preparazione = Preparazione

    def __repr__(self):
        return f"<Semilavorati {self.Id}>"

class Scontrini(db.Model):
    __tablename__ = 'scontrini'

    Id = db.Column(db.Integer(), primary_key=True)
    Data = db.Column(db.Date())

    Semilavorato = relationship("ScontriniSemilavorati", back_populates='scontrini', cascade="all, delete-orphan")
    Merce = relationship("ScontriniMerce", back_populates='scontrini',  cascade="all, delete-orphan")

    def __init__(self, Id, Data):
        self.Id = Id
        self.Data = Data

    def __repr__(self):
        return f"<scontrini {self.Id}>"

class Allergeni(db.Model):
    __tablename__ = 'allergeni'

    Id = db.Column(db.Integer(), primary_key=True)
    Nome = db.Column(db.String())

    Merce = relationship("Merce")

    def __init__(self, Id, Nome):
        self.Id = Id
        self.Nome = Nome

    def __repr__(self):
        return f"<allergeni {self.Id}>"

class Merce(db.Model):
    __tablename__ = 'merce'

    Id = db.Column(db.Integer(), primary_key=True)
    Nome = db.Column(db.String())
    Quantità = db.Column(db.Integer())
    PrezzoUnitario = db.Column(db.Float())
    IVA = db.Column(db.Float)
    MateriaPrima = db.Column(db.Boolean())  #ATTENZIONE, solo se True può far parte di una ricetta
    Id_Allergene = db.Column(ForeignKey('allergeni.Id', ondelete='CASCADE')) #vedi se è da mettere nel costruttore

    Semilavorati = relationship("Ricette", back_populates='merce', cascade="all, delete-orphan")
    Scontrini = relationship("ScontriniMerce", back_populates='merce', cascade="all, delete-orphan")
    FatturaAcquisto = relationship("ContenutoAcquisto", back_populates='merce',  cascade="all, delete-orphan")
    FatturaVendita = relationship("ContenutoVenditaMerce", back_populates='merce',  cascade="all, delete-orphan")

    def __init__(self, Id, Nome, Quantità, PrezzoUnitario, IVA, MateriaPrima):
        self.Id = Id
        self.Nome = Nome
        self.Quantità = Quantità
        self.PrezzoUnitario = PrezzoUnitario
        self.IVA = IVA
        self.MateriaPrima = MateriaPrima

    def __repr__(self):
        return f"<Merce {self.Id}>"

class ProduzioneGiornaliera(db.Model):
    __tablename__ = 'produzioneGiornaliera'

    Data = db.Column(db.Date(), primary_key=True)
    Note = db.Column(db.String())

    Semilavorato = relationship("produzione", back_populates='produzioneGiornaliera', cascade="all, delete-orphan")

    def __init__(self, Data, Note):
        self.Data = Data
        self.Note = Note

    def __repr__(self):
        return f"<produzioneGiornaliera {self.Data}>"

class FattureAcquisto(db.Model):
    __tablename__ = 'fattureAcquisto'

    Id = db.Column(db.Integer(), primary_key=True)
    Mail_Fornitore = db.Column(db.String(), ForeignKey('fornitori.Mail', ondelete='CASCADE'))
    NumDocumento = db.Column(db.Integer())
    Data = db.Column(db.Date())

    NoteVariazioneRicevute = relationship("NoteVariazioneRicevute")

    Merce = relationship("ContenutoAcquisto", back_populates='fattureAcquisto',  cascade="all, delete-orphan")

    def __init__(self, Id, Mail_Fornitore, NumDocumento, Data):
        self.Id = Id
        self.Mail_Fornitore = Mail_Fornitore
        self.NumDocumento = NumDocumento
        self.Data = Data

    def __repr__(self):
        return f"<FattureAcquisto {self.Id}>"

class FattureVendita(db.Model):
    __tablename__ = 'fattureVendita'

    Id = db.Column(db.Integer(), primary_key=True)
    Mail_Cliente = db.Column(db.String(), ForeignKey('clienti.Mail', ondelete='CASCADE'))
    NumDocumento = db.Column(db.Integer())
    Data = db.Column(db.Date())

    NoteVariazioneEmesse = relationship("NotevariazioneEmesse")

    Merce = relationship("ContenutoVenditaMerce", back_populates='fattureVendita', cascade="all, delete-orphan")
    Semilavorati = relationship("ContenutoVenditaSemilavorato", back_populates='fattureVendita',  cascade="all, delete-orphan")

    def __init__(self, Id, Mail_Fornitore, NumDocumento, Data):
        self.Id = Id
        self.Mail_Fornitore = Mail_Fornitore
        self.NumDocumento = NumDocumento
        self.Data = Data

    def __repr__(self):
        return f"<FattureVendita {self.Id}>"

class NoteVariazioneRicevute(db.Model):
    __tablename__ = 'noteVariazioneRicevute'

    Id = db.Column(db.Integer(), primary_key=True)
    Id_fatturaAcquisto = db.Column(db.Integer(), ForeignKey('fattureAcquisto.Id', ondelete='CASCADE'))
    NumDocumento = db.Column(db.Integer())
    Data = db.Column(db.Date())
    Note = db.Column(db.String())
    Variazione = db.Column(db.Float())

    def __init__(self, Id, Id_fatturaAcquisto, NumDocumento, Data, Note, Variazione):
        self.Id = Id
        self.Id_fatturaAcquisto = Id_fatturaAcquisto
        self.NumDocumento = NumDocumento
        self.Data = Data
        self.Note = Note
        self.Variazione = Variazione

    def __repr__(self):
        return f"<NotediVariazioneRicevute {self.Id}>"

class NoteVariazioneEmesse(db.Model):
    __tablename__ = 'noteVariazioneEmesse'

    Id = db.Column(db.Integer(), primary_key=True)
    Id_fatturaVendita = db.Column(db.Integer(), ForeignKey('fattureVendita.Id', ondelete='CASCADE'))
    NumDocumento = db.Column(db.Integer())
    Data = db.Column(db.Date())
    Note = db.Column(db.String())
    Variazione = db.Column(db.Float())

    def __init__(self, Id, Id_fatturaVendita, NumDocumento, Data, Note, Variazione):
        self.Id = Id
        self.Id_fatturaVendita = Id_fatturaVendita
        self.NumDocumento = NumDocumento
        self.Data = Data
        self.Note = Note
        self.Variazione = Variazione

    def __repr__(self):
        return f"<NotediVariazioneEmesse {self.Id}>"

#assciazione diendeti articoli
class Blog(db.Model):
    __tablename__ = 'blog'

    Mail_Dipendente = db.Column(ForeignKey('dipendenti.Mail', ondelete='CASCADE'), primary_key = True)
    Id_Articolo = db.Column(ForeignKey('articoli.Id', ondelete='CASCADE'), primary_key = True)

#assciazione personale turni
class PersonaleTurni(db.Model):
    __tablename__ = 'personaleTurni'

    Mail_Dipendente = db.Column(ForeignKey('dipendenti.Mail', ondelete='CASCADE'), primary_key=True)
    Id_Turno = db.Column(ForeignKey('turni.Id', ondelete='CASCADE'), primary_key=True)
    Data = db.Column(db.Date())
    OraInizio = db.Column(db.Time())
    OraFine = db.Column(db.Time())

# associazione tra materie prime e semilavorati
class Ricette(db.Model):
    __tablename__ = 'ricette'

    Id_Semilavorato = db.Column(ForeignKey('semilavorati.Id', ondelete='CASCADE'), primary_key=True)
    Id_MateriaPrima = db.Column(ForeignKey('merce.Id', ondelete='CASCADE'), primary_key=True)   #in quanto specificato che solo le merci che sono materie prime possono comporre ricette

#assciazione clienti semilavorati
class WishList(db.Model):
    __tablename__ = 'wishList'

    Mail_Cliente = db.Column(ForeignKey('clienti.Mail', ondelete='CASCADE'), primary_key=True)
    Id_Semilavorato = db.Column(ForeignKey('semilavorati.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

#assciazione clienti semilavorati
class Carrello(db.Model):
    __tablename__ = 'carrello'

    Mail_Cliente = db.Column(ForeignKey('clienti.Mail', ondelete='CASCADE'), primary_key=True)
    Id_Semilavorato = db.Column(ForeignKey('semilavorati.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

#assciazione produzioneGiornaliera semilavorati
class Produzione(db.Model):
    __tablename__ = 'produzione'

    Data_Produzione = db.Column(ForeignKey('produzioneGiornaliera.Data', ondelete='CASCADE'), primary_key=True)
    Id_Semilavorato = db.Column(ForeignKey('semilavorati.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

#assciazione scontrini semilavorati
class ScontriniSemilavorati(db.Model):
    __tablename__ = 'scontriniSemilavorati'

    Id_Scontrino = db.Column(ForeignKey('scontrini.Id', ondelete='CASCADE'), primary_key=True)
    Id_Semilavorato = db.Column(ForeignKey('semilavorati.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

#assciazione scontrini merce
class ScontriniMerce(db.Model):
    __tablename__ = 'scontriniMerce'

    Id_Scontrino = db.Column(ForeignKey('scontrini.Id', ondelete='CASCADE'), primary_key=True)
    Id_Merce = db.Column(ForeignKey('merce.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

#assciazione fatture acquisto merce
class ContenutoAcquisto(db.Model):
    __tablename__ = 'contenutoAcquisto'

    Id_FatturaAcquisto = db.Column(ForeignKey('fattureAcquisto.Id', ondelete='CASCADE'), primary_key=True)
    Id_Merce = db.Column(ForeignKey('merce.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

#assciazione fatture vendita merce
class ContenutoVenditaMerce(db.Model):
    __tablename__ = 'contenutoVenditaMerce'

    Id_FatturaVendità = db.Column(ForeignKey('fattureVendita.Id', ondelete='CASCADE'), primary_key=True)
    Id_Merce = db.Column(ForeignKey('merce.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

# assciazione fatture vendita semilavorati
class ContenutoVenditaSemilavorati(db.Model):
    __tablename__ = 'contenutoVenditaSemilavorati'

    Id_FatturaVendità = db.Column(ForeignKey('fattureVendita.Id', ondelete='CASCADE'), primary_key=True)
    Id_Semilavorato = db.Column(ForeignKey('semilavorati.Id', ondelete='CASCADE'), primary_key=True)
    Quantità = db.Column(db.Integer())

