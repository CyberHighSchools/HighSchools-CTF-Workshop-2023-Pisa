# Internet Festival 2023 - HighSchools CTF Workshop

## [web] useless-panel (16 risoluzioni)

Una volta registrati nella piattaforma ed effettuato il login, tramite i devtools è possibile vedere i cookie impostati dal sito.

Analizzandoli si nota che il cookie di sessione è un json in cui, tra i vari elementi è presente il campo `is_admin` con valore `false`.

Modificandone il valore a `true` otteniamo i privilegi da admin e possiamo perciò visitare l'admin panel, ottenendo così la flag.
