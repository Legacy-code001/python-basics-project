What type of workload are you executing?
├── CPU-bound (heavy calculations, decryption, image resizing)
│   └── Use MULTIPROCESSING
│       • Bypasses the GIL
│       • Parallel execution on multi-core systems
│
└── I/O-bound (waiting on network responses, files, database writes)
    │
    ├── Thousands of concurrent connections
    │   └── Use ASYNCIO
    │       • Single-threaded, ultra-low memory usage
    │
    └── Synchronous libraries only (e.g., requests, sqlite3)
        └── Use THREADING
            • Releases the GIL during system calls