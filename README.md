<div>
  
  ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
  ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
  ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
  
</div>

# Tirocinio
## Progetto di tirocinio: Gestionale pasticceria
Nella nostra proposta di tirocinio e tesi vorremmo presentare il progetto per la realizzazione di un sistema dedicato ad una specifica pasticceria.
Questo strumento deve garantire l’integrale controllo degli aspetti contabili ed organizzativi dell’attività, inoltre vogliamo proporre una comoda vetrina per il sito della pasticceria ove possa presentare i diversi servizi e prodotti che potrebbe offrire.
Tutto ciò presentato sotto forma di una WebApp.
Un'altra componente che abbiamo pensato per il sistema è un’applicazione dedicata al personale dipendente dell’attività, che verrà approfondita nei prossimi paragrafi.

### WebApp
Questa componente del sistema a sua volta è composta da:
Gestionale, privato dedicato al titolare
Sito, pubblico dedicato alle interazioni con i clienti
Dal sito sarà possibile accedere al gestionale attraverso un login presente nella sezione area riservata.
##### Descrizione Gestionale
Qui troviamo la possibilità di gestire diversi aspetti contabili e organizzativi dell’attività, elencandoli sono:
- Fornitori
  - Ingredienti, giacenze di magazzino
  - Ordini, acquisto materie prime
- Clienti
  - Anagrafe clienti, gestione dei clienti profilizzati 
  - Storico ordini
- Ricettario, elenco ricette per lancio di produzione
- Documenti, gestione, visione e creazione dei documenti necessari
  - DDT
  - Fatture
  - Note di credito
  - Storico documenti
- Costi, anagrafica dei costi 
  - Gestione del personale
  - Gestione infrastrutturali
  - Gestione ingredienti
  - Costi fiscali
- Ricavi, anagrafica ricavi
  - Gestione vendite (e-commerce)
  - Gestione vendite (in loco), registrate manualmente
- Lancio di produzione, organizzazione della produzione 
    - Produzione giornaliera, scheduling produzione
    - Extra, attività non ordinarie

##### Descrizione del sito 
Qui troviamo le diverse componenti che vanno a formare la vetrina che la pasticceria può sfruttare per l’autopromozione dei propri servizi e prodotti offerti. Elenchiamo le voci che abbiamo pensato per il sito, sono:
- Team, presentazione del personale di lavoro
- La pasticceria, presentazione generale dell’attività, dei servizi e prodotti offerti (HomePage)
- Contatti
- Servizi e prodotti
  - Shop, e-commerce dedicato al Take Away e al Delivery
    - Prodotti, listino dei prodotti offerti
  - Prenotazione tavolo
  - Catering, possibilità di ingaggiare l’attività per servizio di catering ad eventi speciali
- Blog, aggiornamenti costanti relativi all’attività

![uml_webapp](https://github.com/Ghita00/Tirocinio/blob/master/Image_ReadMe/UML_WebApp.jpg "uml_webapp")

#### Architettura e tecnologie del sistema
L'architettura finale del sistema presenta un DataBase centrale con il quale andranno ad interagire (in lettura e in scrittura) sia la WebApp (sito + gestionale) che l’applicazione.
Le tecnologie da noi pensate sono:
- HTML e CSS per la presentazione
- JavaScript per le gestioni delle API
- Python con la libreria Flask per la gestione BackEnd 
- Postgresql per la gestione del DataBase
- Python con la libreria SQLAlchemy per le interrogazioni al DataBase
- Kotlin per l’applicazione

![Architettura](https://github.com/Ghita00/Tirocinio/blob/master/Image_ReadMe/architettura.png "Architettura")
