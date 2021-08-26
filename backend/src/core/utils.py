import hashlib
import time
import jwt
from dotenv import load_dotenv
from os import getenv

load_dotenv()

token_count = 0


def generate_sha256(string: str) -> str:
    """
    Hashes the supplied string.

    :param string: The string to hash.
    """
    hashed = hashlib.sha256(bytes(string, encoding="utf-8")).hexdigest()
    hashed = hashlib.sha256(bytes(hashed, encoding="utf-8")).hexdigest()
    return hashed


def gensnowflake() -> int:
    """
    Generates an ID based on the timestamp.
    """
    global token_count
    flake = time.time_ns().to_bytes(56, byteorder="big")
    flake += token_count.to_bytes(8, byteorder="big")
    token_count += 1
    token_count %= 256
    return int.from_bytes(flake, byteorder="big")

def generatetoken(uid: str, password: str) -> str:
    """
    Generates a user token.

    :param uid: The ID of the user.
    :param password: The password of the user.
    """
    token = jwt.encode({"uid": uid, "password": password}, getenv("TOKEN_SECRET"), algorithm="HS256")
    return token

def decodetoken(token: str) -> dict:
    """
    Decodes a users token.

    :param token: The user's token to decode.
    """
    decoded = jwt.decode(token, getenv("TOKEN_SECRET"), algorithms=["HS256"])
    return decoded
    
