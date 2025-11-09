# 🔑 Bitcoin Private Key to WIF Converter

A lightweight Python script that converts a **Bitcoin private key (in hex format)** into its corresponding **WIF (Wallet Import Format)** representation.

The script supports both **compressed** and **uncompressed** key formats and manually implements the Bitcoin **Base58Check** encoding algorithm.

---

## 🧩 Overview

Bitcoin private keys are 32 bytes (64 hexadecimal characters).  
To be used in most wallets, they must be encoded in **WIF**, which includes:

- a **network prefix** (e.g. `0x80` for Bitcoin mainnet),
- an **optional compression flag** (`0x01`),
- a **4-byte checksum** (first 4 bytes of double SHA-256),
- and **Base58Check encoding**.

This script reproduces that exact process step-by-step.

---

## ⚙️ How It Works

1. **Read the private key (hex string)**
2. **Add the version byte**
   - Mainnet prefix: `0x80`
   - Testnet prefix (optional): `0xEF`
3. **Optionally add compression flag (`0x01`)**  
   Used for wallets that generate compressed public keys.
4. **Compute the checksum**
   - Double SHA-256 of the payload
   - Take the first 4 bytes
5. **Concatenate and Base58Check encode**

6. Output:

Uncompressed WIF: 5Km2kuu7vtFDPpxywn4u3NLpbr5jKpTB3jsuDU2KYEqetd9ZKJ4
Compressed WIF:   L5oLkpV3aqBjhki6LmvChTCV6odsp4SXM6FfU2Gppt5kEqeonMfk

⚠️ Security Notice

⚠️ Never share or publish your real private keys.

This script is for educational and testing purposes only.

The example key shown above is not valid for real wallets.

Any private key exposed online should be treated as compromised.

Use testnet or offline environments for experiments.

🧠 What You’ll Learn

✅ How Bitcoin converts private keys to WIF format
✅ How Base58Check encoding and checksums work
✅ How to handle both compressed and uncompressed key types
✅ The importance of network prefixes in Bitcoin key encoding

BTC donation address: bc1q4nyq7kr4nwq6zw35pg0zl0k9jmdmtmadlfvqhr
