import os
from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

KEY = os.environ["FLAG"]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_encrypt(message: str, key: str) -> str:
    ciphertext = ""
    for i, c in enumerate(message):
        msg_as_num = ALPHABET.index(c)
        key_as_num = ALPHABET.index(key[i % len(key)])
        ciphertext += ALPHABET[(msg_as_num + key_as_num) % len(ALPHABET)]
    return ciphertext

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

@app.route("/encrypt_message/<message>")
def get_encrypted_message(message: str):
    if not all(c in ALPHABET for c in message):
        return json.dumps({"error": "Message must only contain characters in the alphabet"})
    if len(set(message)) < len(message):
        return json.dumps({"error": "Message must not contain duplicate characters"})
    random_prefix = "".join(random.choices(ALPHABET, k=random.randint(1, 4)))
    ciphertext = vigenere_encrypt(random_prefix + message, KEY)
    return json.dumps({"ciphertext": ciphertext})


# SKIP
if __name__ == "__main__":
    app.run(debug=True)
