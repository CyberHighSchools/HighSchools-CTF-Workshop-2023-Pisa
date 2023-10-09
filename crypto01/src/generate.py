import os
from base64 import b64encode

FLAG = os.environ["FLAG"]

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def rot13(message: str) -> str:
    """Performs a ROT13 encryption on the message

    Args:
            message (str): The message to encrypt
    Returns:
            str: The encrypted message
    """
    return "".join(
        chr((ord(c) - ord("a") + 13) % 26 + ord("a")) if c in ALPHABET else c
        for c in message
    )


def tohex(message: str) -> str:
    """Converts the message to hex

    Args:
            message (str): The message to convert
    Returns:
            str: The converted message
    """
    return message.encode().hex()


def b64(message: str) -> str:
    """Performs a base64 encoding on the message

    Args:
            message (str): The message to encode
    Returns:
            str: The encoded message
    """
    return b64encode(message.encode()).decode()


rounds = [rot13, tohex, b64, b64, tohex, b64]

ciphertext = FLAG
for round in rounds:
	ciphertext = round(ciphertext)
print(ciphertext)
