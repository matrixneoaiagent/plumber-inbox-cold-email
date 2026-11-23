# The Plumber's Inbox — invoice book variant.
#!/usr/bin/env python3
import os

def main():
    # Ensure the output directory exists
    os.makedirs('/output', exist_ok=True)
    entry_text = """Subject: The invoice book on the dash

Hi Marek,

The invoice book sits on the dash and gets filled in between jobs, and half the receipts never make it out of the van. That's normal for a two-van firm, not a failing.

Here's what I do: sort the receipts, match the bank account to the invoices, and send the invoices out. $200 a month, flat, no matter how many jobs you log.

I'm a bookkeeper, not an accountant, and I don't sell software. I answer emails myself, usually within a day. If you want a look, reply with the name of the system you use now, or "nothing" if it's all paper.

Thanks,
Helen Okafor"""
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write(entry_text)

if __name__ == "__main__":
    main()
