import hashlib
import json

DIFFICULTY = 3

def encode(obj):
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")

# CONTOH KELIRU: hash tidak memasukkan isi transaksi
def block_hash(block):
    return hashlib.sha256(
        str(block["height"]).encode("utf-8")
    ).hexdigest()

# CONTOH KELIRU: tidak memeriksa syarat proof-of-work
def mine(height, txs, previous_hash):
    return {
        "height": height,
        "txs": txs,
        "previous_hash": previous_hash,
        "nonce": 0,
        "hash": block_hash({"height": height})
    }

block = mine(
    0,
    [{"from": "Andi", "to": "Bima", "amount": 10}],
    "0" * 64
)

print("Hasil simulasi:")
print(json.dumps(block, indent=2))
print("Hash memenuhi difficulty:",
      block["hash"].startswith("0" * DIFFICULTY))