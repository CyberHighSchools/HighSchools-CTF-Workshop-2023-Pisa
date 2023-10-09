# Internet Festival 2023 - HighSchools CTF Workshop

## [network] A distracted admin (19 risoluzioni)

Il file di cattura contiene vari pacchetti, analizzando i pacchetti HTTP notiamo una richiesta a `/admin.php`.

Possiamo ispezionare la richiesta nel dissector di Wireshark:

```text
Frame 41: 235 bytes on wire (1880 bits), 235 bytes captured (1880 bits) on interface eth0, id 0
Ethernet II, Src: PcsCompu_cb:7e:f5 (08:00:27:cb:7e:f5), Dst: PcsCompu_d2:8b:f4 (08:00:27:d2:8b:f4)
Internet Protocol Version 4, Src: 10.0.2.15, Dst: 10.0.2.4
Transmission Control Protocol, Src Port: 48908, Dst Port: 900, Seq: 1, Ack: 1, Len: 169
Hypertext Transfer Protocol
    GET /admin.php  HTTP/1.1\r\n
    Host: 10.0.2.4:900\r\n
    Authorization: Basic YWRtaW46ZmxhZ3t1bjRfcDRzc3cwcmRfdmVyYW0zbnRlX240c2Mwc3RhfQ==\r\n
        Credentials: admin:flag{un4_p4ssw0rd_veram3nte_n4sc0sta}
    User-Agent: curl/7.88.1\r\n
    Accept: */*\r\n
    \r\n
    [Full request URI: http://10.0.2.4:900/admin.php]
    [HTTP request 1/1]
    [Response in frame: 44]
```

Si può vedere che la richiesta contiene delle informazioni di autenticazione nell'header HTTP `Authorization`, e la flag è la password dell'admin.
