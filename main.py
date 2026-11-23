# The Plumber's Inbox: A 120-Word Cold Email entry.
import os

def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    
    entry_text = """Subject: Bookkeeping for a two-van plumbing firm

Hi Dave,

The glovebox in your second van is probably where last month's supplier receipts are living. You're out on the first call-out before seven, and the invoices get written up at the kitchen table after eight.

I do three things for two-van firms: I sort your receipts, match the bank account to the invoices, and send your invoices out each Friday. One flat fee of $180 a month, whatever the volume.

I work from photos you text me, so nothing changes in your day. If that's useful, reply "yes" and I'll send one short question about how you invoice now.

Thanks,
Mark Ellison, bookkeeper
"""
    
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry_text)

if __name__ == "__main__":
    main()
