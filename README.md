Acest script Python permite utilizatorului să gestioneze parole pentru diferite site-uri sau aplicații. Utilizatorul poate adăuga parole, vizualiza parolele existente și șterge parole dintr-un fișier text numit passwords.txt. Parolele sunt stocate într-un fișier text într-un format simplu, unde fiecare linie conține numele site-ului/aplicației și parola asociată, separate de un semn egal (=).

Funcționalități:
Adaugă o parolă (addPass):

Solicită utilizatorului să introducă numele site-ului/aplicației.
Verifică dacă numele conține simbolul "=" și oprește execuția dacă acesta este prezent.
Întreabă utilizatorul dacă dorește să genereze automat o parolă sau să introducă una manual.
Dacă se alege generarea automată, parola va avea o lungime de 8 caractere, inclusiv litere și cifre.
Salvează numele și parola în fișierul passwords.txt într-un format de tipul: site = parola.
Vizualizează o parolă (viewPass):

Solicită utilizatorului numele site-ului/aplicației pentru care dorește să vadă parola.
Caută în fișierul passwords.txt și afișează parola asociată.
Dacă site-ul/aplicația nu este găsit, se afișează un mesaj că acesta nu există.
Șterge o parolă (deletePass):

Solicită utilizatorului numele site-ului/aplicației pentru care dorește să șteargă parola.
Caută în fișierul passwords.txt și elimină intrarea corespunzătoare.
Dacă numele este găsit, contul este șters și restul fișierului este rescris fără acea intrare.
Utilizare:
Rularea Scriptului:

La rulare, scriptul solicită una dintre următoarele opțiuni:
Adăugă o parolă (add): Introduce o parolă nouă pentru un site sau o aplicație.
Vezi parola existentă (view): Vizualizează parola pentru un site/aplicație existentă.
Șterge parola (delete): Șterge o parolă existentă din fișier.
După selectarea opțiunii, scriptul va continua cu acțiunile specifice acesteia.
Formatul Fișierului passwords.txt:

Fiecare linie din fișier are formatul:
makefile
Copy code
site = parola
Comenzi specifice:

Adăugă parolă:
Introdu numele aplicației sau site-ului.
Alege dacă dorești generarea automată a parolei sau introdu o parolă manual.
Vizualizează parolă: Introdu numele aplicației/site-ului pentru care dorești să vezi parola.
Șterge parolă: Introdu numele aplicației/site-ului pentru care dorești să ștergi parola.
Excepții și Erori:
Dacă numele site-ului/aplicației conține simbolul "=", scriptul va afișa un mesaj de eroare și se va opri.
Dacă parola pentru un cont nu există, va fi afișat un mesaj corespunzător.
Scriptul nu face diferența între majuscule și minuscule când caută numele aplicației.
Instalare:
Asigură-te că ai instalat Python (versiunea 3.x).
Salvează scriptul într-un fișier main.py.
Execută scriptul folosind comanda python main.py în terminal.
