# Internet Festival 2023 - HighSchools CTF Workshop

## [web] traverse_me_more (0 risoluzioni)

Rispetto a `traverse me`, in questa challenge il server esegue un sanitize sul filename fornito dall'utente.
Leggendo il codice della funzione di sanitize ci si può accorgere del fatto che dopo la sanificazione:

- `.../` -> `.`
- `\/` -> `/`

Notando ciò, si ha che la stringa `....\/` viene sanitizzata come `../`.

La soluzione consiste perciò nell'inviare la stringa `....\/....\/....\/flag.txt` che verrà sanitizzata in `../../../flag.txt`.

Una soluzione efficace era anche ottenibile fuzzando la funzione di sanitize; per saperne di più: `https://owasp.org/www-community/Fuzzing`.
