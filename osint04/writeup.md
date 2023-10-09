# Internet Festival 2023 - HighSchools CTF Workshop

## [osint] Una nuova azienda 04 (19 risoluzioni)

Sarà necessario trovare in primo luogo il profilo di github del CTO. La cosa da fare in questo caso è cercare il vero nome e cognome del CTO su github e filtrando la ricerca per utenti.

Una volta aperto il profilo github del CTO si noterà che all'interno vi è una repository che contiene un file python. Apparentemente il file sembra non contenere niente di importante, ma ad uno sgurado più attento agli specifici commit si nota che il file è stato prima creato e poi modificato.

Guardando la modifica apportata, cioè cliccando nello specifico su uno dei commit, si nota come in principio nella funzione `print` ci fosse la flag (sostituita poi da `hello Pisa`).
