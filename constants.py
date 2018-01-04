# Definitions used
WORD_BYTES = 4  # bytes in word
DATASET_BYTES_INIT = 2**30  # bytes in dataset at genesis
DATASET_BYTES_GROWTH = 2**23  # dataset growth per epoch
CACHE_BYTES_INIT = 2**24  # bytes in cache at genesis
CACHE_BYTES_GROWTH = 2**17  # cache growth per epoch
CACHE_MULTIPLIER = 1024  # Size of the DAG relative to the cache
EPOCH_LENGTH = 30000  # blocks per epoch
MIX_BYTES = 128  # width of mix
HASH_BYTES = 64  # hash length in bytes
DATASET_PARENTS = 256  # number of parents of each dataset element
CACHE_ROUNDS = 3  # number of rounds in cache production
ACCESSES = 64  # number of accesses in hashimoto loop
EPOCH_LENGTH = 30000  # blocks per epoch
WORD_BYTES = 4  # bytes in word

FNV_PRIME = 0x01000193  # used in Data aggregation function

# exporting all constants
__all__ = [
    "WORD_BYTES", "DATASET_BYTES_INIT", "DATASET_BYTES_GROWTH",
    "CACHE_BYTES_INIT", "CACHE_BYTES_GROWTH", "CACHE_MULTIPLIER",
    "EPOCH_LENGTH", "MIX_BYTES", "HASH_BYTES", "DATASET_PARENTS",
    "CACHE_ROUNDS", "ACCESSES", "FNV_PRIME"
]
