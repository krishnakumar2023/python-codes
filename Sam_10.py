# Write a Python program
# a. which takes email address as input (format : "username@domainname")
# b. write at least three email addresses into a text file emails.txt.
# c. print all the usernames excluding domain name

import re

# Function to extract the username from an email address
def get_username(email):
    pattern = re.compile(r'^(\w+)@[\w\.]+$')
    match = pattern.match(email)
    if match:
        return match.group(1)
    else:
        return None

# Take email address as input
email_input = input("Enter email address: ")

# Write at least three email addresses to a file
with open('emails.txt', 'w') as file:
    file.write('john@example.com\n')
    file.write('jane@example.com\n')
    file.write('bob@example.com\n')

# Read the email addresses from the file and extract the usernames
with open('emails.txt', 'r') as file:
    for line in file:
        email = line.strip()
        username = get_username(email)
        if username:
            print(username)
