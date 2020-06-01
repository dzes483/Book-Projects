#!/usr/bin/python3
# auto-unsubscriber.py - Scans through emails in the user's Gmail Inbox,
# searching for any "Unsubscribe" links. It then opens them in a web browser,
# allowing the user to unsubscribe. Due to the nature of unsubscribe links
# these days ("hiding" the link among other text, using a phrase such as "Don't
# want to receive these emails?", etc.), it likely will not catch everything.

import sys
import imaplib
import email
import bs4
from bs4 import BeautifulSoup
import lxml
import requests
import webbrowser

user_email = "user@example.com"
user_pass = 'user_pass'
folder = "INBOX"

# Login to the client with IMAP, and exit if the login failed.
client = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    rv, data = client.login(user_email, user_pass)
except imaplib.IMAP4.error:
    print ("LOGIN FAILED!!! ")
    sys.exit(1)
print(rv, data)

def process_mailbox(client):
    """
    Process the mailbox and decode the messages, searching for 'Unsubscribe'
    links.
    """

    # Make sure that there are messages.
    rv, data = client.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    # Make sure that the message ID can be fetched.
    for id in data[0].split():
        rv, data = client.fetch(id, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", id)
            return

        # Determine the type of message (HTML&text or just text) and handle
        # accordingly
        msg = email.message_from_bytes(data[0][1])
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # Skip plain text attachments.
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)  # decode
                    break
        # If the message is not multipart (just plaintext)
        else:
            body = msg.get_payload(decode=True)
        soup = bs4.BeautifulSoup(body, 'lxml')
        unsub_links = soup.find_all(href=True, string="Unsubscribe")
        for link in unsub_links:
            print('Link found.')
            webbrowser.open(link.get('href'))
            print('Link opened.')



rv, mailboxes = client.list()
if rv == 'OK':
    print("Mailboxes:")
    print(mailboxes)

rv, data = client.select(folder)
if rv == 'OK':
    print(f"Processing {folder}...\n")
    process_mailbox(client)
    client.close()
else:
    print("ERROR: Unable to open mailbox ", rv)

client.logout()
