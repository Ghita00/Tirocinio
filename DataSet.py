from GenDB import *

Immagini = [Immagini(Id = '1', img = '')]

Persone = [Persone(Mail = 'vioricadanci@gmail.com', Nome = 'Viorica', Cognome = 'Danci', Username ='vioricadanci', Password = 'Viorica79', DataNascita = '1979-07-12', Telefono = '3283187029', Rating = '0')]

Dipendenti = [Dipendenti(Mail = 'vioricadanci@gmail.com', DataAssunzione = '11-07-2022')]


Data = [Persone, Dipendenti]

for i in Data:
    session.add_all(i)

session.commit()

if __name__ == '__main__':
    app.run(debug=True)

