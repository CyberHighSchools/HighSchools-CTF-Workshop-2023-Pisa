# Internet Festival 2023 - HighSchools CTF Workshop

## [network] Corrupted Mascotte (5 risoluzioni)

All'interno del pcap è presente una connessione FTP, da cui viene scaricata una immagine chiamata `gabibbo.png`.
Possiamo estrarla usando la funzione `Estrai oggetti` di Wireshark.

Provando ad aprirla, però, l'immagine risulta corrotta.
Ispezionando il file tramite Cyberchef o hexdump, si può vedere che i primi 8 bytes sono la stringa `"GABIBBO!"`

```bash
$ hexdump -C gabibbo.png | head
00000000  47 41 42 49 42 42 4f 21  00 00 00 0d 49 48 44 52  |GABIBBO!....IHDR|
00000010  00 00 02 a6 00 00 03 20  08 06 00 00 00 f1 e5 a0  |....... ........|
00000020  ee 00 00 08 88 65 58 49  66 49 49 2a 00 08 00 00  |.....eXIfII*....|
00000030  00 0f 00 00 01 04 00 01  00 00 00 a6 02 00 00 01  |................|
00000040  01 04 00 01 00 00 00 20  03 00 00 02 01 03 00 03  |....... ........|
00000050  00 00 00 c2 00 00 00 0e  01 02 00 76 00 00 00 c8  |...........v....|
00000060  00 00 00 0f 01 02 00 18  00 00 00 3e 01 00 00 10  |...........>....|
```

Possiamo rimpiazzare questi bytes, tramite un hex editor o tramite Cyberchef, con i magic bytes del formato PNG.
Questi si possono trovare su [wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures) e sono `89 50 4E 47 0D 0A 1A 0A`.

```bash
$ hexdump -C gabibbo_recovered.png | head
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
00000010  00 00 02 a6 00 00 03 20  08 06 00 00 00 f1 e5 a0  |....... ........|
00000020  ee 00 00 08 88 65 58 49  66 49 49 2a 00 08 00 00  |.....eXIfII*....|
00000030  00 0f 00 00 01 04 00 01  00 00 00 a6 02 00 00 01  |................|
00000040  01 04 00 01 00 00 00 20  03 00 00 02 01 03 00 03  |....... ........|
00000050  00 00 00 c2 00 00 00 0e  01 02 00 76 00 00 00 c8  |...........v....|
00000060  00 00 00 0f 01 02 00 18  00 00 00 3e 01 00 00 10  |...........>....|
00000070  01 02 00 11 00 00 00 56  01 00 00 12 01 03 00 01  |.......V........|
00000080  00 00 00 01 00 00 00 1a  01 05 00 01 00 00 00 68  |...............h|
00000090  01 00 00 1b 01 05 00 01  00 00 00 70 01 00 00 28  |...........p...(|
```

Il file modificato può essere adesso aperto ed è possibile leggere la flag all'interno.
