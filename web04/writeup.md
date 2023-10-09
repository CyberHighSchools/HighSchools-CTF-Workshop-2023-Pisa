# Internet Festival 2023 - HighSchools CTF Workshop

## [web] traverse_me (3 risoluzioni)

Con l'endpoint `/serve_file` è possibile visualizzare singolarmente le immagini mostrate nella home. L'endpoint accetta come query parameter `filename` che contiene il nome dell'immagine desiderata.

Nell'accesso alle foto c'è una `path traversal`; fornendo come `filename` la stringa `../../../flag.txt` possiamo accedere al file della flag situato nella root folder.

Per saperne di più riguardo le vulnerabilità di tipo `path traversal`: `https://portswigger.net/web-security/file-path-traversal`
