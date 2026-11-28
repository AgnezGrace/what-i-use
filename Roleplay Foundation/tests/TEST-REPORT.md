# Foundation test report — v0.2.0

Executed using Python standard library only.

- `python scripts/sync_catalog.py --check`: PASS — no drift in the shipped foundation.
- `python scripts/validate.py`: PASS — required files, metadata, registry paths and local Markdown links.
- `python -m unittest discover -s tests -v`: PASS — 22 test methods (11 original and 11 synchronization tests).

The synchronization tests use isolated temporary directories. They cover simultaneous category, manifestation and adapter registration, deterministic ordering, idempotence, draft exclusion, explicit removal protection and cleanup, missing guide rejection before writes, invalid adapter dates, ambiguous aliases, managed block preservation, symlink rejection and drift repair. The router remains unchanged in the extension fixture. No synthetic category or adapter is shipped as supported content.

The tool generates derived registries and managed README sections only. It is not a semantic quality reviewer; review status is asserted by the author. Each file replacement is atomic, but the entire batch is not a transaction. Concurrent writers and simulated filesystem failures were not tested. Sixteen behavioral evaluation scenarios remain unexecuted against an independent model. Actual platform compatibility, roleplay quality and token savings are not established by structural tests.
