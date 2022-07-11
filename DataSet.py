from GenDB import *

Immagini = [Immagini(Id = '1', img = '')]

Persone = [Persone(Mail = 'vioricadanci@gmail.com', Nome = 'Viorica', Cognome = 'Danci', DataNascita = '1979-07-12', Telefono = '3283187029', Rating = '0'),
           Persone(Mail = 'larissadanci@gmail.com', Nome = 'Larissa', Cognome = 'Danci', DataNascita = '2003-03-01', Telefono = '3318380776', Rating = '1'),
           Persone(Mail = 'cassandradanci@gmail.com', Nome = 'Cassandra', Cognome = 'Danci', DataNascita = '2005-07-26', Telefono = '3498100631', Rating = '1'),
           Persone(Mail = 'rominadanci@gmail.com', Nome = 'Romina', Cognome = 'Danci', DataNascita = '2000-01-30', Telefono = '3920301407', Rating = '5'),
           Persone(Mail = 'vanessadanci@gmail.com', Nome = 'Vanessa', Cognome = 'Danci', DataNascita = '2013-02-27', Telefono = '3289098762', Rating = '8'),
           Persone(Mail = 'vasiledanci@gmail.com', Nome = 'Vasile', Cognome = 'Danci', DataNascita = '1973-07-02', Telefono = '3205608445', Rating = '10'),
           Persone(Mail = 'giorgiobasile@gmail.com', Nome = 'Giorgio', Cognome = 'Basile', DataNascita = '2000-07-19', Telefono = '3208761554', Rating = '1'),
           Persone(Mail = 'loredanagiannella@gmail.com', Nome = 'Loredana', Cognome = 'Giannella', DataNascita = '1969-12-05', Telefono = '3289091209', Rating = '10'),
           Persone(Mail = 'claudioivascu@gmail.com', Nome = 'Claudio', Cognome = 'Ivasco', DataNascita = '1999-02-13', Telefono = '3290908765', Rating = '2'),
           Persone(Mail = 'denisdanci@gmail.com', Nome = 'Denis', Cognome = 'Danci', DataNascita = '2003-09-16', Telefono = '3210987603', Rating = '1'),
           Persone(Mail = 'annabianchi@gmail.com', Nome = 'Anna', Cognome = 'Bianchi', DataNascita = '1986-02-23', Telefono = '3456712345', Rating = '9'),
           Persone(Mail = 'marcorossi@gmail.com', Nome = 'Marco', Cognome = 'Rossi', DataNascita = '1979-12-13', Telefono = '3216789012', Rating = '10'),
           Persone(Mail = 'chiaraverdi@gmail.com', Nome = 'Chiara', Cognome = 'Verdi', DataNascita = '1999-03-23', Telefono = '3209187623', Rating = '5'),
           Persone(Mail = 'giuliamelchior@gmail.com', Nome = 'Giulia', Cognome = 'Melchior', DataNascita = '2000-07-03', Telefono = '3198723908', Rating = '1'),
           Persone(Mail = 'giovannibruni@gmail.com', Nome = 'Giovanni', Cognome = 'Bruni', DataNascita = '1998-06-18', Telefono = '3298765320', Rating = '9'),
           Persone(Mail = 'martinagialli@gmail.com', Nome = 'Martina', Cognome = 'Gialli', DataNascita = '1996-01-10', Telefono = '3509479800', Rating = '6'),
           Persone(Mail = 'mariachiaratossi@gmail.com', Nome = 'Mariachiara', Cognome = 'Tossi', DataNascita = '1999-12-25', Telefono = '3290887654', Rating = '0'),
           Persone(Mail = 'giovannagrossi@gmail.com', Nome = 'Giovanna', Cognome = 'Grossi', DataNascita = '1989-04-23', Telefono = '3290986572', Rating = '3'),
           Persone(Mail = 'mariomartini@gmail.com', Nome = 'Mario', Cognome = 'Martini', DataNascita = '2006-09-17', Telefono = '3209876541', Rating = '5'),
           Persone(Mail = 'cristianotovassi@gmail.com', Nome = 'Cristiano', Cognome = 'Tovassi', DataNascita = '1986-08-23', Telefono = '3289761239', Rating = '9'),
           Persone(Mail = 'dianastrozzer@gmail.com', Nome = 'Diana', Cognome = 'Strozzer', DataNascita = '1999-12-13', Telefono = '3209871235', Rating = '8'),
           Persone(Mail = 'giuliarusu@gmail.com', Nome = 'Giulia', Cognome = 'Rusu', DataNascita = '2003-09-07', Telefono = '3109127612', Rating = '5'),
           Persone(Mail = 'giorgiamart@gmail.com', Nome = 'Giorgia', Cognome = 'Mart', DataNascita = '2000-01-03', Telefono = '3098123450', Rating = '10'),
           Persone(Mail = 'francescopelosin@gmail.com', Nome = 'Francesco', Cognome = 'Pelosin', DataNascita = '1998-11-18', Telefono = '3450981128', Rating = '2'),
           Persone(Mail = 'matteobonato@gmail.com', Nome = 'Matteo', Cognome = 'Bonato', DataNascita = '1996-05-19', Telefono='3209812225', Rating = '6'),
           Persone(Mail = 'gaiamartini@gmail.com', Nome = 'Gaia', Cognome = 'Martini', DataNascita = '2000-04-23', Telefono = '3408881239', Rating = '3'),
           Persone(Mail = 'michaeltoretto@gmail.com', Nome = 'Michael', Cognome = 'Toretto', DataNascita = '1989-12-03', Telefono = '3451219998', Rating = '4'),
           Persone(Mail = 'cristinaapostol@gmail.com', Nome = 'Cristina', Cognome = 'Apostol', DataNascita = '2005-03-13', Telefono = '3209876661', Rating = '4'),
           Persone(Mail = 'gianmariarussin@gmail.com', Nome = 'Gianmaria', Cognome = 'Russin', DataNascita = '2001-06-23', Telefono = '3211112356', Rating = '7'),
           Persone(Mail = 'rebeccarubini@gmail.com', Nome = 'Rebecca', Cognome = 'Rubini', DataNascita = '1988-06-18', Telefono = '3456667812', Rating = '6'),
           Persone(Mail = 'giuliochiari@gmail.com', Nome = 'Giulio', Cognome = 'Chiari', DataNascita = '1986-07-19', Telefono = '3221349980', Rating = '3'),
           Persone(Mail = 'robertomattei@gmail.com', Nome = 'Roberto', Cognome = 'Mattei', DataNascita = '2001-09-15', Telefono = '3457776124', Rating = '7'),
           Persone(Mail = 'metteobellon@gmail.com', Nome = 'Matteo', Cognome = 'Bellon', DataNascita = '1992-09-11', Telefono = '3789651130', Rating = '8'),
           Persone(Mail = 'ruggerogiulianelli@gmail.com', Nome = 'Ruggero', Cognome = 'Giulianelli', DataNascita = '2002-08-19', Telefono = '3987121459', Rating = '2'),
           Persone(Mail = 'francoreggi@gmail.com', Nome = 'Franco', Cognome = 'Reggi', DataNascita = '1999-08-03', Telefono = '3679829984', Rating = '1'),
           Persone(Mail = 'martacristini@gmail.com', Nome = 'Marta', Cognome = 'Cristini', DataNascita = '2000-04-19', Telefono = '3782290547', Rating = '8'),
           Persone(Mail = 'matteofilote@gmail.com', Nome = 'Matteo', Cognome = 'Filote', DataNascita = '1985-07-22', Telefono = '3789926518', Rating = '4'),
           Persone(Mail = 'melissaricci@gmail.com', Nome = 'Melissa', Cognome = 'Ricci', DataNascita = '2006-10-30', Telefono = '3792136710', Rating = '0'),
           Persone(Mail = 'vittoriorossi@gmail.com', Nome = 'Vittorio', Cognome = 'Rossi', DataNascita = '1999-01-08', Telefono = '3897651128', Rating = '5'),
           Persone(Mail = 'valeriomarini@gmail.com', Nome = 'Valerio', Cognome = 'Marini', DataNascita = '1976-05-19', Telefono = '3781231195', Rating = '6')
           ]

Dipendenti = [Dipendenti(Mail = 'vioricadanci@gmail.com', Username = 'viordicadanci', Password = 'viorica', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'larissadanci@gmail.com', Username = 'larissadanci', Password = 'larissa', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'rominadanci@gmail.com', Username = 'rominadanci', Password = 'romina', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'giorgiobasile@gmail.com', Username = 'giorgiobasile', Password = 'giorgio', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'claudioivascu@gmail.com', Username = 'claudioivascu', Password = 'claudio', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'giuliarusu@gmail.com', Username = 'giuliarusu', Password = 'giulia', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'giorgiamart@gmail.com', Username = 'giorgiamart', Password = 'giorgia', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'ruggerogiulianelli@gmail.com', Username = 'ruggerogiulianelli', Password = 'ruggero', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'giovannibruni@gmail.com', Username = 'giovannibruni', Password = 'giovanni', DataAssunzione = '11-07-2022'),
              Dipendenti(Mail = 'francoreggi@gmail.com', Username = 'francoreggi', Password = 'franco', DataAssunzione = '11-07-2022')]

Fornitori = [Fornitori(Mail = 'matteofilote@gmail.com', Ditta = 'FiloMit', PartitaIVA = '86334519757'),
             Fornitori(Mail = 'melissaricci@gmail.com', Ditta = 'RicciSRL', PartitaIVA = '88723456188'),
             Fornitori(Mail = 'vasiledanci@gmail.com', Ditta = 'VasiSRL', PartitaIVA = '83127799120')]

Clienti = [Clienti(Mail = 'valeriomarini@gmail.com', Username = 'valeriomarini', Password = 'valerio', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'vittoriorossi@gmail.com', Username = 'vittoriorossi', Password = 'vittorio', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'martacristini@gmail.com', Username = 'martacristini', Password = 'marta', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'metteobellon@gmail.com', Username = 'metteobellon', Password = 'metteo', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'robertomattei@gmail.com', Username = 'robertomattei', Password = 'roberto', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'giuliochiari@gmail.com', Username = 'giuliochiari', Password = 'giulio', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'rebeccarubini@gmail.com', Username = 'rebeccarubini', Password = 'rebecca', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'gianmariarussin@gmail.com', Username = 'gianmariarussin', Password = 'gianmaria', DataRegistrazione = '11-07-2022'),
           Clienti(Mail = 'loredanagiannella@gmail.com', Username = 'loredanagiannella', Password = 'loredana', DataRegistrazione = '11-07-2022')]

Data = [Persone, Dipendenti, Fornitori, Clienti]

for i in Data:
    session.add_all(i)

#session.commit()

if __name__ == '__main__':
    app.run(debug=True)

