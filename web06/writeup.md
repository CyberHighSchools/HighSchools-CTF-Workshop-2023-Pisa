# Internet Festival 2023 - HighSchools CTF Workshop

## [web] easy_access (0 risoluzioni)

```javascript
const element = req.query.element;
var content = "";
if (element === "flag") {
  content = "you wish";
} else {
  content = data[element] || "Element not found";
}
```

Possiamo passare `element[]=flag` in questo modo il confronto con triplo uguale darà `false` ma quando andremo ad usare `element` come indice dell'array esso verrà convertito nella stringa `flag` e potremo quindi ottenere la flag.
