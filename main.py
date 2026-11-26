#!/usr/bin/env python3
"""Write one funny smart-speaker apology to /output/entry.txt.

The speaker misheard "order pizza" as "call your ex". The joke works
because the device reports the disaster it caused in a calm, helpful
tone, then undercuts it with a parallel punchline: both the ex and
the pizza are now on their way, and it is proud of the one it got right.
"""

import os

ENTRY = (
    "Sorry \u2014 you said 'order pizza,' I heard 'call your ex.' "
    "She's on her way. The pizza is too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
