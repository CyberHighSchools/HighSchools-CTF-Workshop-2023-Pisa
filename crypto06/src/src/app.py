import os
from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

FLAG = os.environ["FLAG"]


def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])

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
    """Encrypts the flag using a one-time pad and returns the ciphertext,
    checking that the ciphertext does not contain any plaintext characters"""
    message = FLAG.encode()
    ciphertext = message
    while any(c == m for c, m in zip(ciphertext, message)):
        key = os.urandom(len(FLAG))
        ciphertext = xor(message, key)
    return json.dumps({"ciphertext": ciphertext.hex()})


# SKIP
if __name__ == "__main__":
    app.run(debug=True)
