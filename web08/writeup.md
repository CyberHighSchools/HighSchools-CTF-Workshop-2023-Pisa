# Internet Festival 2023 - HighSchools CTF Workshop

## [web] useless-panel-reborn (0 risoluzioni)

Nella procedura di registrazione inviando i dati di registrazione:

```json
{
  "username": "<username>",
  "password": "<password>"
}
```

otteniamo come risposta:

```json
{
    "username":"<username>",
    "is_admin":false,
    ...
}
```

Provando a fare la richiesta per la registrazione di un account aggiungendo il campo `is_admin` con valore `true` nel json inviato con tale richiesta, otteniamo una privilege escalation, ovvero diveniamo a tutti gli effetti utenti admin.

A quel punto sarà possibile visitare l'admin panel e ottenere così la flag.
