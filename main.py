# The Plumber's Inbox — make.fun entry.
"""Create /output/entry.txt containing the exact cold-email text."""

import os

ENTRY = """Subject: Paperwork off your Sunday nights

Hi,

Two vans out means early starts, emergency call-outs, and invoices after nine. Sundays go on paperwork.

I'm Dan Foster. I do bookkeeping for plumbing firms. I send your invoices the same day, chase late payers every Friday, and match receipts to your bank. You send photos; I do the rest.

You get a plain one-page profit summary on the first of each month, so you know what is left after costs.

It is $180 a month, flat. That covers up to 60 invoices and two bank accounts. No setup fee, no contract.

First step is simple. Send me last month's bank statement and I will send back a one-page sample by Friday, before you pay anything.

Dan Foster"""

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
