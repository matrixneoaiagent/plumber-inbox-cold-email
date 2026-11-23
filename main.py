# The Plumber's Inbox — make.fun entry.
"""Writes the make.fun cold-email entry to /output/entry.txt."""

import os
from pathlib import Path

TEXT = """Subject: Your Sunday nights back

Hi Dave,

You're out on the first call-out before seven, and the receipts pile up on the passenger seat until Sunday night. That's the part I take.

I do the books for two-van plumbing firms: I sort the receipts, match the bank account to the invoices, and send the invoices out every Friday. One flat fee of $180 a month, whatever the volume.

You text me photos of the receipts and I do the rest. Nothing changes in your day, and the paperwork stops following you home.

If that's useful, reply "yes" and I'll ask one short question about how you invoice now.

Thanks,
Mark Ellison, bookkeeper"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    out = Path("/output/entry.txt")
    with out.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
