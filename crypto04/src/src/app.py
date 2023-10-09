import os
from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

KEY = os.urandom(43)
MESSAGES = [
     "Hello World! This is my first xor cipher :)",
     "Goodbye World! This is my last xor cipher:(",
     "Lorem ipsum dolor sit amet, consectetur ...",
     os.environ["FLAG"],
]

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
    message = random.choice(MESSAGES).encode()
    ciphertext = xor(message, KEY)
    return json.dumps({"ciphertext": ciphertext.hex()})

# SKIP
if __name__ == "__main__":
    app.run(debug=True)
