#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program (account @berkahmuse-2).

Writes one original absurd terms-of-service clause to /output/entry.txt.
Deterministic: no input, no network, no environment, no randomness — the
clause below is fixed, so every run writes byte-identical output.
"""

import os

CLAUSE = (
    "Upon termination, any soul you upload to the Service becomes the sole "
    "property of the Company, including on weekends, holidays, and in the "
    "afterlife."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()
