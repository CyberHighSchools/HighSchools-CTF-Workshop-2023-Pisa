# Internet Festival 2023 - HighSchools CTF Workshop

## [forensics] Last Standing Bytes (7 risoluzioni)

Dalla descrizione della challenge capiamo che bisogna recuperare un segreto nascosto in una immagine PNG.

Il segreto è nascosto usando la codifica LSB, quindi l'immagine a occhio nudo appare normale.

Per recuperare la flag è sufficiente importare l'immagine su Cyberchef e applicare l'operazione `Extract LSB`, ottenendo questa stringa:

```text
ZmxhZ3tMU0JfaDFkZDNuX3MzY3JldF8xc19uMHRfczBfaGlkZGVuX3MzY3JldH0=
```

Notiamo che alla fine è presente un `=`, che è un indizio che potrebbe trattarsi di dati codificati in base64, quindi proviamo a estrarli sempre su Cyberchef usando l'operazione `From Base64` e otteniamo la flag.
