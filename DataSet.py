from GenDB import *

Persone = [Persone(Mail='vioricadanci@gmail.com', Nome='Viorica', Cognome='Danci', Username='vioricadanci', Password='Viorica79', DataNascita='1979-07-12', Telefono='3283187029', Rating='0'),
           Persone(Mail='larissadanci@gmail.com', Nome='Larissa', Cognome='Danci', Username='larissadanci', Password='Larissa03', DataNascita='2003-03-01', Telefono='3205608445', Rating='0'),
           Persone(Mail='rominadanci@gmail.com', Nome='Romina', Cognome='Danci', Username='rominadanci', Password='Romina00', DataNascita='2000-01-20', Telefono='3290301407', Rating='0'),
           Persone(Mail='prova@gmail.com', Nome='Prova', Cognome='ProvaCognome', Username='prova', Password='Prova000', DataNascita='2003-03-01', Telefono='123456789', Rating='0')
           ]

Dipendenti = [Dipendenti(Mail='vioricadanci@gmail.com', DataAssunzione='11-07-2022'),
              Dipendenti(Mail='larissadanci@gmail.com', DataAssunzione='11-07-2022')]

Clienti = [Clienti(Mail='prova@gmail.com', DataRegistrazione='11-07-2022'),
           Clienti(Mail='rominadanci@gmail.com', DataRegistrazione='11-07-2022')]

DittaFornitrice = [DittaFornitrice(PartitaIVA='86334519757', NomeDitta='StoccoSRL', Mail='stoccosrl@gmail.com', Telefono='0423406067', Via='Rossini 5', Città='Treviso', Stato='Italia'),
                   DittaFornitrice(PartitaIVA='88924578120', NomeDitta='ColorantiSRL', Mail='colorantisrl@gmail.com', Telefono='0423807699', Via='San Marco 3', Città='Salzano', Stato='Italia'),
                   DittaFornitrice(PartitaIVA='89671233099', NomeDitta='DolciariaSPA', Mail='dolciariaspa@gmail.com', Telefono='0423809766', Via='Cristoforo Colombo 15', Città='Treviso', Stato='Italia')]

Allergeni = [Allergeni(Nome='Cereali contenenti glutine'),
             Allergeni(Nome='Soia'),
             Allergeni(Nome='Frutta secca in guscio'),
             Allergeni(Nome='Arachidi'),
             Allergeni(Nome='Semi di sesamo'),
             Allergeni(Nome='Latte'),
             Allergeni(Nome='Uova'),
             Allergeni(Nome='Pesce'),
             Allergeni(Nome='Crostacei'),
             Allergeni(Nome='Sedano'),
             Allergeni(Nome='Senape'),
             Allergeni(Nome='Biossido di zolfo e solfiti'),
             Allergeni(Nome='Lupini'),
             Allergeni(Nome='Molluschi'),
             Allergeni(Nome='Nessuno')]

Turni = [Turni(Nome='Mattiniero', OraInizioTurno='05:00:00', OraFineTurno='13:00:00', CompensoOrario='8.90'),
         Turni(Nome='Pomeridiano', OraInizioTurno='13:00:00', OraFineTurno='18:00:00', CompensoOrario='8.90'),
         Turni(Nome='Serale', OraInizioTurno='18:00:00', OraFineTurno='23:00:00', CompensoOrario='8.90'),
         Turni(Nome='Giornaliero', OraInizioTurno='05:00:00', OraFineTurno='17:00:00', CompensoOrario='8.90')]

Semilavorati = [Semilavorati(Nome='Brioche Crema', Quantità='20', PrezzoUnitario='1.10', IVA='10', Preparazione=None, Categoria='Brioche', Descrizione="", Incipit="", TempoPreparazione=0, Porzioni=1),
                Semilavorati(Nome='Brioche Cioccolato', Quantità='20', PrezzoUnitario='1.10', IVA='10', Preparazione=None, Categoria='Brioche', Descrizione="", Incipit="", TempoPreparazione=0, Porzioni=1),
                Semilavorati(Nome='Brioche Vuota', Quantità='20', PrezzoUnitario='1.10', IVA='10', Preparazione=None, Categoria='Brioche', Descrizione="", Incipit="", TempoPreparazione=0, Porzioni=1),
                Semilavorati(Nome='Brioche Marmellata', Quantità='20', PrezzoUnitario='1.10', IVA='10', Preparazione=None, Categoria='Brioche', Descrizione="", Incipit="", TempoPreparazione=0, Porzioni=1),
                Semilavorati(Nome='Brioche Frutti di bosco', Quantità='20', PrezzoUnitario='1.10', IVA='10', Preparazione=None, Categoria='Brioche', Descrizione="", Incipit="", TempoPreparazione=0, Porzioni=1)]

Merce = [Merce(Nome='Farina', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=True, Id_Allergene=1),
         Merce(Nome='Uova', Quantità='60', PrezzoUnitario='2.00', IVA='10', MateriaPrima=True, Id_Allergene=7),
         Merce(Nome='Burro', Quantità='20', PrezzoUnitario='4.00', IVA='10', MateriaPrima=True, Id_Allergene=6),
         Merce(Nome='Latte', Quantità='50', PrezzoUnitario='15.00', IVA='10', MateriaPrima=True, Id_Allergene=6),
         Merce(Nome='Gelatina', Quantità='10', PrezzoUnitario='25.00', IVA='10', MateriaPrima=True, Id_Allergene=12),
         Merce(Nome='Colorante Blu', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Rosa', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Rosso', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Nero', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Oro', Quantità='10', PrezzoUnitario='7.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Argento', Quantità='10', PrezzoUnitario='7.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Giallo', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Arancione', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=False, Id_Allergene=15),
         Merce(Nome='Colorante Verde', Quantità='10', PrezzoUnitario='5.00', IVA='10', MateriaPrima=False, Id_Allergene=15)]

Articoli = [Articoli(Titolo='Ricette fresche per l estate', Categoria="", Contenuto='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis ligula nec tempus posuere. Aliquam consequat ipsum eu viverra maximus. Nam lobortis, arcu a sollicitudin vulputate, enim odio efficitur mauris, et sollicitudin purus nisl at odio. Proin fringilla, urna posuere tristique cursus, lectus neque posuere diam, et posuere nibh tortor eget quam.', DataPubblicazione='21-07-2022'),
            Articoli(Titolo='Le cinque torte più richieste del mese', Categoria="", Contenuto='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis ligula nec tempus posuere. Aliquam consequat ipsum eu viverra maximus. Nam lobortis, arcu a sollicitudin vulputate, enim odio efficitur mauris, et sollicitudin purus nisl at odio. Proin fringilla, urna posuere tristique cursus, lectus neque posuere diam, et posuere nibh tortor eget quam.', DataPubblicazione='21-07-2022'),
            Articoli(Titolo='NOVITA, Brioche variegate disponibili', Categoria="", Contenuto='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis ligula nec tempus posuere. Aliquam consequat ipsum eu viverra maximus. Nam lobortis, arcu a sollicitudin vulputate, enim odio efficitur mauris, et sollicitudin purus nisl at odio. Proin fringilla, urna posuere tristique cursus, lectus neque posuere diam, et posuere nibh tortor eget quam.', DataPubblicazione='21-07-2022')]

Blog = [Blog(Mail_Dipendente='larissadanci@gmail.com', Id_Articolo=1),
        Blog(Mail_Dipendente='larissadanci@gmail.com', Id_Articolo=2),
        Blog(Mail_Dipendente='larissadanci@gmail.com', Id_Articolo=3)]

WishList = [WishList(Mail_Cliente='rominadanci@gmail.com', Id_Semilavorato=1),
            WishList(Mail_Cliente='rominadanci@gmail.com', Id_Semilavorato=3),
            WishList(Mail_Cliente='rominadanci@gmail.com', Id_Semilavorato=5),
            WishList(Mail_Cliente='prova@gmail.com', Id_Semilavorato=1),
            WishList(Mail_Cliente='prova@gmail.com', Id_Semilavorato=3),
            WishList(Mail_Cliente='prova@gmail.com', Id_Semilavorato=5)]

FattureAcquisto = [FattureAcquisto(Id_Fornitore='86334519757', NumDocumento=1, Data='11-07-2022')]

FattureVendita = [FattureVendita(Mail_Cliente='prova@gmail.com', NumDocumento=1,Data='11-01-2022')]

DDT = [DDT(Id_Fornitore='86334519757', NumDocumento=1, DataEmissione='11-01-2022', Note='Urgenza', Importo=50, Peso=10, Colli=7),
       DDT(Id_Fornitore='86334519757', NumDocumento=2, DataEmissione='11-03-2022', Note='Fragile', Importo=100, Peso=50, Colli=8),
       DDT(Id_Fornitore='86334519757', NumDocumento=3, DataEmissione='11-02-2022', Note='Importante', Importo=300, Peso=80, Colli=10),
       DDT(Id_Fornitore='86334519757', NumDocumento=4, DataEmissione='11-04-2022', Note='Trattare con cura', Importo=500, Peso=100, Colli=90),
       DDT(Id_Fornitore='86334519757', NumDocumento=5, DataEmissione='11-05-2022', Note='Collo n 5 difettoso', Importo=70, Peso=40, Colli=80),
       DDT(Id_Fornitore='88924578120', NumDocumento=1, DataEmissione='11-06-2022', Note='Fragile', Importo=80, Peso=20, Colli=100),
       DDT(Id_Fornitore='88924578120', NumDocumento=2, DataEmissione='11-03-2022', Note='Fragile', Importo=20, Peso=10, Colli=5),
       DDT(Id_Fornitore='88924578120', NumDocumento=3, DataEmissione='11-07-2022', Note='Urgente', Importo=50, Peso=5, Colli=6),
       DDT(Id_Fornitore='88924578120', NumDocumento=4, DataEmissione='11-08-2022', Note='Importante', Importo=60, Peso=90, Colli=1),
       DDT(Id_Fornitore='88924578120', NumDocumento=5, DataEmissione='11-08-2022', Note='Scontato', Importo=150, Peso=40, Colli=2),
       DDT(Id_Fornitore='88924578120', NumDocumento=6, DataEmissione='11-02-2022', Note='Da mettere in frigo', Importo=15, Peso=8, Colli=10)]

Scontrini = [Scontrini(Data='10-08-2022'),
             Scontrini(Data='09-07-2022'),
             Scontrini(Data='06-02-2022'),
             Scontrini(Data='12-04-2022'),
             Scontrini(Data='19-05-2022'),
             Scontrini(Data='19-04-2022'),
             Scontrini(Data='29-06-2022'),
             Scontrini(Data='30-05-2022'),
             Scontrini(Data='11-01-2022'),
             Scontrini(Data='03-02-2022'),
             Scontrini(Data='03-03-2022')]

ScontriniMerce = [ScontriniMerce(Id_Scontrino=1, Id_Merce=1, Quantità=4),
                  ScontriniMerce(Id_Scontrino=2, Id_Merce=2, Quantità=3),
                  ScontriniMerce(Id_Scontrino=3, Id_Merce=3, Quantità=2),
                  ScontriniMerce(Id_Scontrino=4, Id_Merce=1, Quantità=1),
                  ScontriniMerce(Id_Scontrino=5, Id_Merce=2, Quantità=6)]

ScontriniSemilavorati = [ScontriniSemilavorati(Id_Scontrino=6, Id_Semilavorato=1, Quantità=1),
                         ScontriniSemilavorati(Id_Scontrino=7, Id_Semilavorato=2, Quantità=5),
                         ScontriniSemilavorati(Id_Scontrino=8, Id_Semilavorato=3, Quantità=8),
                         ScontriniSemilavorati(Id_Scontrino=9, Id_Semilavorato=4, Quantità=10),
                         ScontriniSemilavorati(Id_Scontrino=10, Id_Semilavorato=5, Quantità=4),
                         ScontriniSemilavorati(Id_Scontrino=11, Id_Semilavorato=1, Quantità=9)]

ContenutoAcquisto = [ContenutoAcquisto(Id_FatturaAcquisto=1, Id_Merce=1, Quantità=50),
                     ContenutoAcquisto(Id_FatturaAcquisto=1, Id_Merce=2, Quantità=70),
                     ContenutoAcquisto(Id_FatturaAcquisto=1, Id_Merce=3, Quantità=90)]

ContenutoVenditaSemilavorati = [ContenutoVenditaSemilavorati(Id_FatturaVendità=1, Id_Semilavorato=1, Quantità=50),
                                ContenutoVenditaSemilavorati(Id_FatturaVendità=1, Id_Semilavorato=2, Quantità=60),
                                ContenutoVenditaSemilavorati(Id_FatturaVendità=1, Id_Semilavorato=3, Quantità=10)]


Data = []
#Data = [Persone, Dipendenti, Clienti, DittaFornitrice, Allergeni, Turni, Semilavorati, Merce, Blog
# Articoli, FattureAcquisto, FattureVendita, DDT, Scontrini, ScontriniMerce, ScontriniSemilavorati,
# ContenutoVenditaSemilavorati, ContenutoAcquisto]


for i in Data:
    session.add_all(i)

session.commit()

if __name__ == '__main__':
    app.run(debug=True)

