#!usr/bin/python3
# bittorent_downloader.py - Checks a gmail account for any instructions sent
# by the user and executes these commands automatically. The program then
# deletes the email so that it does not re-run the command.

import sys
import imaplib
import email
import email.header
import subprocess

USER_EMAIL = "user_email"
USER_NAME = 'user_name' # name displayed before the email
USER_PASS = 'user_pass'
EMAIL_FOLDER = "INBOX"
COMMAND_PWD = 'command_pwd'


def process_mailbox(M):
    """
    Process the mailbox and look for a command (an email sent by the user
    containing a torrent magnet link). If found, open qbittorrent and start
    downloading the file.
    """

    # Check for messages in general.
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    # Check for specific messages according to the id.
    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        # Define the Subject and Sender fields
        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header\
                                      (msg['Subject']))
        hdr2 = email.header.make_header(email.header.decode_header
                                      (msg['From']))
        subject = str(hdr)
        sender = str(hdr2)
        print(subject)
        # If the sender is the user and the subject contains the "password":
        if sender == (USER_NAME + ' <' + USER_EMAIL + '>') and \
                     subject.startswith(command_pwd + ' '):
            print('Command found.')
            link = subject[10:]
            print('Downloading torrent...')
            args = ['/usr/bin/qbittorrent', link]
            subprocess.Popen(args)
            M.store(num, '+FLAGS', '\\Deleted')
            M.expunge()
            break

M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    rv, data = M.login(USER_EMAIL, USER_PASS)
except imaplib.IMAP4.error:
    print ("LOGIN FAILED!!! ")
    sys.exit(1)

rv, data = M.select(EMAIL_FOLDER)
if rv == 'OK':
    print("Processing mailbox...\n")
    process_mailbox(M)
    M.close()
else:
    print("ERROR: Unable to open mailbox ", rv)

M.logout()
