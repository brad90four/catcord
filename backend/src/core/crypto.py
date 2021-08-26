import base64


def encryptip(ip: str, username: str) -> str:
    encrypted1 = base64.b32encode(bytes(ip, encoding="utf8"))
    encrypted2 = base64.b64encode(bytes(username, encoding="utf8"))
    equalcount = encrypted1.count(b"=")
    if equalcount == 0:
        encrypted1 += b"-"
        encrypted1 += encrypted2
        encrypted1 = encrypted1.upper()
        return encrypted1.decode(encoding="utf8")
    else:
        encrypted1 = encrypted1.replace(b"=", b"")
        encrypted1 += b"-"
        encrypted2 = encrypted2.replace(b"=", b"")
        encrypted1 += encrypted2
        encrypted1 = encrypted1.upper()
        encrypted1 += bytes(f"_{equalcount}", encoding="utf8")
        return encrypted1.decode(encoding="utf8")


def decryptip(encrypted: str) -> str:
    try:
        equalcount = int(encrypted[-1])
    except ValueError:
        # log no equal signs
        equalcount = None
    encrypted = list(encrypted)
    for i in range(2):
        encrypted.pop()
    encrypted = "".join(encrypted).split("-")
    if equalcount is not None:
        for i in range(equalcount):
            encrypted[0] += "="
    return base64.b32decode(bytes(encrypted[0], encoding="utf8")).decode(
        encoding="utf8"
    )
