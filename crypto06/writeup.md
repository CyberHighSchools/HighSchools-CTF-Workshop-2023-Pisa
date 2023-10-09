# Internet Festival 2023 - HighSchools CTF Workshop

## [crypto] OTP++ (0 risoluzioni)

Quando viene chiamata la funzione `get_encrypted_message` il server della challenge genera una chiave segreta e lunga quanto la flag e la usa per cifrare usando lo xor. Prima di restituire il risultato il server controlla che nessun carattere della flag sia rimasto inalterato, altrimenti genera una nuova chiave e tenta di nuovo la cifratura.

Se prendiamo in considerazione solo il primo carattere del testo cifrato (ossia i primi due caratteri in hex), vediamo che cambia se usiamo più volte la funzione `get_encrypted_message`, questo è normale perché la chiave cambia ogni volta; tuttavia il primo carattere del testo cifrato non assumerà mai il valore `f` (o `66` in hex, ossia il primo carattere della flag) perché il server controlla che non sia così prima di restituire il risultato.

Dunque se chiama la funzione `get_encrypted_message` abbastanza volte, il primo carattere del testo cifrato assumerà tutti i valori tranne `f`, e quindi possiamo dedurre che il primo carattere della flag è `f`, e lo stesso ragionamento vale per tutti gli altri caratteri della flag.

Farlo a mano risulterebbe molto lungo, ma possiamo farlo facilmente con il seguente script da eseguire nella console del browser (nella pagina della challenge):

```js
/* store all the bytes seen at each position, when the size of the set is 255,
 * we know the missing one is the flag byte for that position
 */
let c = (await get_encrypted_message()).ciphertext;
const seen = [...hex2a(c)].map((e) => new Set([e]));

while (seen.some((e) => e.size < 255)) {
  c = (await get_encrypted_message()).ciphertext;
  [...hex2a(c)].forEach((e, i) => seen[i].add(e));
  console.log(Math.min(...seen.map((e) => e.size)));
}

const all_bytes = [...Array(256).keys()].map((e) => String.fromCharCode(e));
const flag = seen
  .map((e) => [...all_bytes].filter((f) => !e.has(f))[0])
  .join("");
console.log(flag);
```
