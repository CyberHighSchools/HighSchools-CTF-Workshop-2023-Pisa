import os
from flask import Flask, render_template, request
import json
import random
from Crypto.Util.number import isPrime

app = Flask(__name__)

FLAG = os.environ["FLAG"]

def dh(g: int, A: int, p: int) -> tuple[int, int]:
    """Performs the Diffie-Hellman key exchange
    
    Args:
        g (int): The base
        A (int): The public key of the other party
        p (int): The prime modulus
    Returns:
        tuple[int, int]: The public key and shared secret
    """
    b = random.randint(1, p - 1) # private key
    shared_secret = pow(A, b, p)
    B = pow(g, b, p) # public key

    return B, shared_secret

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

@app.route("/send_pubkey/<g>/<A>/<p>")
def get_encrypted_message(g, A, p):
    # validate input
    try:
        g, A, p = int(g), int(A), int(p)
    except ValueError:
        return json.dumps({"error": "All arguments must be integers"})
    if g < 2 or g > p - 1:
        return json.dumps({"error": "g must be in the range [2, p - 1]"})
    if A < 1 or A > p - 1:
        return json.dumps({"error": "A must be in the range [1, p - 1]"})
    if not isPrime(p):
        return json.dumps({"error": "p must be prime"})
    if p.bit_length() < 512:
        return json.dumps({"error": "p must be at least 512 bits"})

    # derive shared secret and encrypt flag with xor
    B, shared_secret = dh(g, A, p)
    encryption_key = str(shared_secret).encode()

    ciphertext = xor(FLAG.encode(), encryption_key)

    return json.dumps({"ciphertext": ciphertext.hex(), "B": str(B)})


# SKIP
if __name__ == "__main__":
    app.run(debug=True)
