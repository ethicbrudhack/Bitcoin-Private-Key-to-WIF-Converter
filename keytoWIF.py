import hashlib

# Lokalna implementacja Base58 (żeby nie zależeć od zewnętrznych bibliotek)
B58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def b58encode(b: bytes) -> str:
    n_pad = 0
    for c in b:
        if c == 0:
            n_pad += 1
        else:
            break
    num = int.from_bytes(b, 'big')
    res = []
    while num > 0:
        num, rem = divmod(num, 58)
        res.append(B58_ALPHABET[rem])
    res = ''.join(reversed(res))
    return '1' * n_pad + res

def hex_to_wif(private_key_hex: str, compressed: bool = False) -> str:
    """
    Convert a 32-byte private key hex string to WIF.
    - private_key_hex: 64 hex chars (32 bytes)
    - compressed: if True, produce WIF that indicates compressed pubkey (append 0x01)
    """
    private_key_hex = private_key_hex.strip().lower()
    if private_key_hex.startswith("0x"):
        private_key_hex = private_key_hex[2:]
    if len(private_key_hex) != 64:
        raise ValueError("Private key hex must be exactly 64 hex characters (32 bytes).")
    try:
        key_bytes = bytes.fromhex(private_key_hex)
    except ValueError:
        raise ValueError("Invalid hex string for private key.")

    version_byte = b'\x80'  # mainnet
    extended = version_byte + key_bytes
    if compressed:
        extended += b'\x01'

    checksum = hashlib.sha256(hashlib.sha256(extended).digest()).digest()[:4]
    wif_bytes = extended + checksum
    return b58encode(wif_bytes)

# Przykład użycia:
private_key_hex = "fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd036413f"
print("Uncompressed WIF:", hex_to_wif(private_key_hex, compressed=False))
print("Compressed WIF:  ", hex_to_wif(private_key_hex, compressed=True))
