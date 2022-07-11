from GenDB import *

Immagini = [Immagini(Id = '1', img = '')]

Persone = [Persone(Mail = 'vioricadanci@gmail.com', Nome = 'Viorica', Cognome = 'Danci', DataNascita = '1979-07-12', Telefono = '3283187029', Rating = '0'),
           Persone(Mail = 'larissadanci@gmail.com', Nome = 'Larissa', Cognome = 'Danci', DataNascita = '2003-03-01', Telefono = '3318380776', Rating = '1'),
           Persone(Mail = 'cassandradanci@gmail.com', Nome = 'Cassandra', Cognome = 'Danci', DataNascita = '2005-07-26', Telefono = '3498100631', Rating = '1'),
           Persone(Mail = 'rominadanci@gmail.com', Nome = 'Romina', Cognome = 'Danci', DataNascita = '2000-01-30', Telefono = '3920301407', Rating = '5'),
           Persone(Mail = 'vanessadanci@gmail.com', Nome = 'Vanessa', Cognome = 'Danci', DataNascita = '2013-02-27', Telefono = '3289098762', Rating = '8'),
           Persone(Mail = 'vasiledanci@gmail.com', Nome = 'Vasile', Cognome = 'Danci', DataNascita = '1973-07-02', Telefono = '3205608445', Rating = '10'),
           Persone(Mail = 'giorgiobasile@gmail.com', Nome = 'Giorgio', Cognome = 'Basile', DataNascita = '2000-07-19', Telefono = '3208761554', Rating = '1'),
           Persone(Mail = 'loredanagiannella@gmail.com', Nome = 'Loredana', Cognome = 'Giannella', DataNascita = '1969-12-05', Telefono = '3289091209', Rating = '0'),
           Persone(Mail = 'claudioivascu@gmail.com', Nome = 'Claudio', Cognome = 'Ivasco', DataNascita = '1999-02-13', Telefono = '3290908765', Rating = '2'),
           Persone(Mail = 'denisdanci@gmail.com', Nome = 'Denis', Cognome = 'Danci', DataNascita = '2003-09-16', Telefono = '3210987603', Rating = '3')]

Data = [Persone]

for i in Data:
    session.add_all(i)

#session.commit()

if __name__ == '__main__':
    app.run(debug=True)