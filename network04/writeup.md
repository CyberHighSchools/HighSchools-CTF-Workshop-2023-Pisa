# Internet Festival 2023 - HighSchools CTF Workshop

## [forensics] Nothing to see here (10 risoluzioni)

La challenge ci presenta una immagine JPEG e si può vedere che nella parte bassa ci sono degli artefatti.

Proviamo a importare l'immagine su Cyberchef e applicare l'operazione `Extract Files` per provare a estrarre possibili files posizionati all'interno dell'immagine.

Cyberchef riesce a individuare i seguenti files:

```txt
extracted_at_0x0.jpg        398.343 bytes
extracted_at_0xb1b9.zlib    373 bytes
extracted_at_0x2b574.zlib   7.136 bytes
extracted_at_0x33fbf.zlib   45.613 bytes
extracted_at_0x51275.zip    402 bytes
extracted_at_0x512ba.zip    333 bytes
extracted_at_0x512ba.jar    333 bytes
extracted_at_0x5132f.zip    216 bytes
extracted_at_0x5c556.zlib   161 bytes
```

Possiamo notare che ci sono 3 file ZIP, il file `extracted_at_0x51275.zip` è l'unico ZIP ben formato e apribile.
Al suo interno si trova una cartella `secret`, che contiene il file `flag.txt` con la flag.
