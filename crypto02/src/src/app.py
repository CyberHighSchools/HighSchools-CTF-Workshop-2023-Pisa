import os
from flask import Flask, render_template, request
import json
import random
from secret import MESSAGE

app = Flask(__name__)

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def monoalphabetic_substitution_encrypt(message: str, map: dict[str, str]) -> str:
    return "".join(map[c] if c in map else c for c in message)

# SKIP
@app.route("/")
def index():
    # This is a hack to get the source code of this file, excluding the SKIP
    source = []
    with open(__file__) as f:
        try:
            for line in f:
                if line == "# SKIP\n":
                    while line != "# /SKIP\n":
                        line = next(f)
                    continue
                source.append(line)
        except StopIteration:
            pass
        
    return render_template("index.html", source="".join(source))
# /SKIP

@app.route("/get_encrypted_message/")
def get_encrypted_message():
    random_permutation = random.sample(ALPHABET, len(ALPHABET)) # encryption key
    substitution_map = {k: v for k, v in zip(ALPHABET, random_permutation)}
    ciphertext = monoalphabetic_substitution_encrypt(MESSAGE, substitution_map)
    return json.dumps({"ciphertext": ciphertext})


# SKIP
if __name__ == "__main__":
    app.run(debug=True)
