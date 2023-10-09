# Internet Festival 2023 - HighSchools CTF Workshop

## [network] Document Naming System (7 risoluzioni)

Il file di cattura contiene molte richieste DNS, ma possiamo notare che alcune richieste sono fatte per dei sottodomini di `attacker.eve`.
Possiamo in Wireshark filtrare per le richieste DNS che contengono la stringa `"attacker"` nella query con il seguente filtro

```txt
dns and dns.qry.name contains "attacker.eve"
```

Le richieste DNS filtrate sono queste:

```txt
Standard query 0xf9d0 A f.0.attacker.eve OPT
Standard query 0xbbd7 A l.1.attacker.eve OPT
Standard query 0x4992 A a.2.attacker.eve OPT
Standard query 0xbb1f A g.3.attacker.eve OPT
Standard query 0x557b A {.4.attacker.eve OPT
Standard query 0xe73b A 3.5.attacker.eve OPT
Standard query 0xed9d A v.6.attacker.eve OPT
Standard query 0x5c74 A i.7.attacker.eve OPT
Standard query 0x1fa4 A l.8.attacker.eve OPT
Standard query 0x2ceb A _.9.attacker.eve OPT
Standard query 0xf95f A d.10.attacker.eve OPT
Standard query 0xd395 A n.11.attacker.eve OPT
Standard query 0x33aa A s.12.attacker.eve OPT
Standard query 0xea4a A _.13.attacker.eve OPT
Standard query 0x78ae A s.14.attacker.eve OPT
Standard query 0x6739 A 3.15.attacker.eve OPT
Standard query 0x2be9 A r.16.attacker.eve OPT
Standard query 0xd4db A v.17.attacker.eve OPT
Standard query 0x0d49 A 3.18.attacker.eve OPT
Standard query 0xea85 A r.19.attacker.eve OPT
Standard query 0x24ea A !.20.attacker.eve OPT
Standard query 0xbaec A }.21.attacker.eve OPT
```

e possiamo notare che ogni richiesta contiene un carattere della flag (e la sua posizione).
