#! python3
# chore_assignment.py - Takes a list of email addresses and a list of chores,
# and randomly assigns them to people. Sends an email to each individual
# stating their chore for the week.

import random
import smtplib

chores = ["doing the dishes", "vacuuming", "walking the dog", "doing laundry"]

# Create a temporary list in order to be able to remove values.
temp_chores = chores.copy()

# Read last week's chore file.
with open('chore_data.txt', 'r') as last_chore_data:
    last_chores = last_chore_data.readlines()
    last_chore_data.close()

# A dictionary containing the individual's name, email, and the chore they did
# last week.
data = {"Alice": ["alice@example.com", last_chores[1].strip()],
        "Bob": ["bob@example.com", last_chores[3].strip()],
        "Sandra": ["sandra@example.com", last_chores[5].strip()],
        "Thomas": ["thomas@example.com", last_chores[7].strip()]}

# Log in to the SMTP email service.
my_email = input('Enter your email address: ')
password = input('Enter your password: ')
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(my_email, password)


# Assign a chore to each individual.
with open('chore_data.txt', 'w') as f:
    for name, values in data.items():
        email = data[name][0]
        this_weeks_chore = random.choice(temp_chores)
        # If the chore is the same as last week's, choose again.
        while data[name][1] == this_weeks_chore:
            this_weeks_chore = random.choice(temp_chores)
        else:
            data[name][1] = this_weeks_chore
            # Remove the chore from the temporary list to avoid duplicates.
            temp_chores.remove(this_weeks_chore)
            # Send an email to the individual with their chore for the week.
            body = f"Subject: This Week's Chores\nDear {name},\n\nYour chore "\
                   f"for this week is: {data[name][1]}.\n\nPlease complete it"\
                   f" before the end of the week. Thanks and have a nice day!"
            print(f'Sending email to {email}...')
            # Check if the email sent successfully.
            send_mail_status = smtp_obj.sendmail(my_email, email, body)
            if send_mail_status != {}:
               print(f'There was a problem sending an email to {email}:\
                    {send_mail_status}')
            # Write the data and chores to a file, to keep record of who did
            # which chores that week.
            print(name, file=f)
            print(data[name][1], file=f)

smtp_obj.quit()
f.close()

# Reset the chore list for next time's use.
temp_chores = chores.copy()
print("This week's chores have been sent out.")
