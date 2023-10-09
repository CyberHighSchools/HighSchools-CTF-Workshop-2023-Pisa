# Internet Festival 2023 - HighSchools CTF Workshop

## [crypto] Cifrario di Vigenère (3 risoluzioni)

Il server prende un input fornito dall'utente e lo cifra con il cifrario di Vigenère, lo scopo è recuperale la chiave usata per la cifratua. La peculiarità sta nel fatto che prima della cifratura vengono aggiunti dei caratteri casuali all'inizio del testo.

Vediamo gli step per risolvere la challenge:

1. mandiamo un input sufficientemente lungo, per esempio: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
2. il server ci restituisce il testo cifrato: `DOMADPUNJQYRPDFOGUTGHFKKIWZ`, osserviamo che è lungo 27 caratteri, quindi è stato aggiunto un carattere casuale all'inizio del testo, eliminiamolo e otteniamo il testo cifrato: `OMADPUNJQYRPDFOGUTGHFKKIWZ`
3. ora osservando la tabella di Vigenère, vediamo che per ottenere il carettere cifrato `O` partendo dal carattere del testo in chiaro `A` il carattere della chiave deve essere `O`; il secondo carettere cifrato `M` è stato ottenuto partendo dal carattere del testo in chiaro `B` dunque il carattere della chiave deve essere `L`.
4. i due caratteri della chiave recuperati fino al ora sono `OL`, ripetendo questo procedimento per tutti i caratteri del testo cifrato, si ottiene: `OLYALPHCIPHERSARECOOLPOLYA`
5. per il ragionamento fatto al punto 2, sappiamo mancare un carattere all'inizio della chiave, inoltre sappiamo che la chiave viene ripetuta se non è abbastanza lunga per cifrare tutto il testo, quindi si evince che la chiave è: `POLYALPHCIPHERSARECOOL|POLYA` (la parte dopo la pipe è la chiave ripetuta)
