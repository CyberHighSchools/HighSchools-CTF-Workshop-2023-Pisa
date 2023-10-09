# Internet Festival 2023 - HighSchools CTF Workshop

## [web] lovely encoding (15 risoluzioni)

All'interno del codice HTML della pagina, visualizzabile con i devtools, è presente un tag `script` contenente il seguente codice JavaScript:

```js
document.getElementById("myForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const inputText = document.getElementById("inputText").value;
  const encoded_flag = "synt{jnvg_vf_guvf_pelcgb_be_jro}";
  check_value(encoded_flag, inputText);
});

function customEncode(inputString, shift) {
  if (typeof inputString !== "string" || typeof shift !== "number") {
    throw new Error("Input must be a string, and shift must be a number");
  }

  let encodedString = "";

  for (let i = 0; i < inputString.length; i++) {
    const char = inputString.charAt(i);
    const charCode = inputString.charCodeAt(i);

    if (/[a-zA-Z]/.test(char)) {
      const isUpperCase = char === char.toUpperCase();
      const baseCharCode = isUpperCase ? "A".charCodeAt(0) : "a".charCodeAt(0);
      const shiftedCharCode =
        ((((charCode - baseCharCode + shift) % 26) + 26) % 26) + baseCharCode;
      encodedString += String.fromCharCode(shiftedCharCode);
    } else {
      encodedString += char;
    }
  }

  return encodedString;
}

function customDecode(encodedString, shift) {
  return customEncode(encodedString, -shift);
}

function check_value(encodedString, plaintext) {
  if (encodedString === customEncode(plaintext, 13)) {
    document.getElementById("success").innerHTML =
      "Winner winner chicken dinner!!!";
  }
}
```

Dal codice si nota che, oltre alla funzione `customEncode`, utilizzata per la cifratura della flag che poi viene mostrata a schermo, è presente la funzione customDecode.

Chiamare tale funzione dala console, passando come input la flag criptata mostrata a schermo permette di decifrarla.
