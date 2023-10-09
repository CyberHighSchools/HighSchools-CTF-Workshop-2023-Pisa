# Internet Festival 2023 - HighSchools CTF Workshop

## [web] was_it_a_flag (6 risoluzioni)

La webapp pusha l'header Location per ridirezionare l'utente su `/roll` ma non termina l'esecuzione del codice php.

Di conseguenza la flag viene stampata al momento della richiesta ed è visibile se si impedisce il redirect.

Questo può essere fatto richiedendo la pagina con curl oppure utilizzando un proxy, come quello forninto da Burp, che registra tutte le richieste.

Con curl in particolare, il comando da eseguire è `curl -v -X POST -d password=qualsiasicosa [url]/flag.php`.
