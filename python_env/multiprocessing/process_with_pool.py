# dividend_calculator.py
from multiprocessing import Pool
'''We use Pool to automatically manage a set number of worker processes and distribute calculations across them using pool.map().'''

def decrypt_receipt_hash(receipt_id):
    """Simulate decrypting a transaction receipt key (CPU-bound)."""
    # A heavy mathematical operation representing decryption
    return sum(i * i for i in range(receipt_id))

if __name__ == "__main__":
    receipts = [100000, 200000, 300000, 400000]
    
    # Create a pool of 4 worker processes
    with Pool(processes=4) as pool:
        # Distribute the decryption tasks across all 4 CPU cores
        results = pool.map(decrypt_receipt_hash, receipts)
        print("Decrypted Receipt Keys:", results)