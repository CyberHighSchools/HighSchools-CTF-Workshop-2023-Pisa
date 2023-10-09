# Internet Festival 2023 - HighSchools CTF Workshop

## [crypto] Many Time Pad (4 risoluzioni)

Il server ha una funzione che sceglie casualmente una stringa da una lista di stringhe note più la flag, e la cifra tramite xor con una chiave segreta sempre uguale. Chiamiamo i messaggi noti $m_1$, $m_2$, $m_3$ ed i rispettivi testi cifrati $c_1$, $c_2$, $c_3$. Sia $f$ la flag, $k$ la chiave segreta e $c_f$ il testo cifrato della flag. Ricordiamo che per definizione $c_i = m_i \oplus k$ e $c_f = f \oplus k$.

Osserviamo che la seguente uguaglianza è vera:

$$ (m_1 \oplus c_1) \oplus (m_2 \oplus c_2) \oplus (m_3 \oplus c_3) \oplus c_f = f$$

Infatti dal momento che $c_i = m_i \oplus k$, vale anche $m_i \oplus c_i = k$ (lo stesso vale per $c_f$), e dunque sostituiendo otteniamo:

$$ k \oplus k \oplus k \oplus (f \oplus k) = f$$

Per le proprietà dell'operatore xor: $x \oplus x = 0$ (ogni elemento è l'inverso di se stesso) e $x \oplus 0 = x$ (lo zero è l'identità), è semplice verificare che l'uguaglianza è vera.

A primo impatto può sembrare che per utilizzare la formula sia necessario conoscere esattamente quale dei testi cifrati si riferisce a quale messaggio noto, in realtà non è necessario perché lo xor è commutativo ed associativo, dunque purchè compaiano tutti i termini, non importa in quale ordine.

Per ricapitolare, per risolvere la challenge occorre prendere i 4 test cifrati, i 3 testi noti e fare lo xor tre tutti i loro valori, il risultato sarà la flag. È possibile farlo a mano tramite i tool grafici della challenge, oppure con il seguente script da eseguire nella console del browser (nella pagina della challenge):

```js
const ms = [
  "Hello World! This is my first xor cipher :)",
  "Goodbye World! This is my last xor cipher:(",
  "Lorem ipsum dolor sit amet, consectetur ...",
];
const cs = new Set();
while (cs.size < 4) {
  const c_hex = (await get_encrypted_message()).ciphertext;
  cs.add(hex2a(c_hex));
}
const flag = [...cs, ...ms].reduce(xor);
console.log(flag);
```
