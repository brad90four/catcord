import base64


def encryptip(ip: str, username: str) -> str:
    return base64.b64encode(bytes(f"{ip},{username}", encoding="utf-8")).decode(encoding='utf8')


def decryptip(ip: str) -> str:
    return base64.b64decode(bytes(ip, encoding="utf-8")).decode(encoding='utf8').split(",")[0]
