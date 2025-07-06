# Elaborato-PPM-Backend
## Deployment link
https://elaborato-ppm-backend.onrender.com/
## Traccia scelta
Event Management System: Build an event management system where users can create,manage, and attend events. Implement
features such as event creation, event registration, and event attendance tracking. The model complexity can involve
defining relationships between users, events, and registrations. The templates can focus on displaying event details and
attendee information. Define two user groups with distinct permissions: Attendee that can view events,
register/unregister themselves, view own registrations; Organizer that has all attendee permissions, plus create,
update, and delete their own events and view list of attendees for their events.

## Utenti creati

| Tipologia | Username       | Password         | Email                         |
|-----------|----------------|------------------|-------------------------------|
| Superuser | admin          | Password_123     | salvatore.greco3@edu.unifi.it |
| Attendee  | salvatore      | passwordSicura1! | email@email.com               |
| Organizer | organizzatore  | passwordSicura1! | email_organizzatore@email.com |
| Organizer | organizzatrice | passwordSicura1! | organizzatrice@mail.com       |

## Descrizione sito

Il sito è un event management system.\
Nella homepage è possibile vedere tutti gli eventi disponibili. Dalla pagina di
dettaglio evento
è possibile vedere maggiori informazioni sull'evento e iscriversi, se attendee, oppure, se organizzatori, gestire
l'evento e vedere la lista di utenti iscritti.
L'iscrizione all'evento è possibile solo se loggati come attendee. \
Da utente anonimo è possibile vedere l'homepage e un
dettaglio eventi senza avere la possibilità di iscriversi o di fare le azioni previste dall'utente organizzatore.\
Nella gestione dell'evento è possibile modificare le informazioni relative ad esso oppure cancellarlo; tutto questo
esclusivamente se
l'utente corrente è l'effettivo organizzatore dell'evento (in caso si accedesse ugualmente alla pagina di manage da
attendee o da organizzatore
che non ha organizzato tale evento si riceve 403 Forbidden).\
È presente una profile page dove è possibile vedere gli eventi a cui si è iscritti, se attendee, oppure gli eventi
organizzati se organizzatore.
Tale pagina presenta anche l'accesso ai qr code dei biglietti di ingresso all'evento e alla pagina di scansione per
organizzatori (se si prova ad
accedere alla pagina di scansione con l'utente attendee si riceve 403 Forbidden); tali biglietti sono monouso. 