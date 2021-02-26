#! /usr/bin/env python3

import re, pyperclip



# Create a regex for phone numbers

phoneRegex = re.compile(r"""
# 315-250-1111, 250-1111, (315) 250-1111, 250-1111 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?           # area code (optional)
(\s|-)?            # first separator
\d\d\d           # first 3 digits
-            # separator
\d\d\d\d            # last 4 digitsex
(((ext(\.)?\s)|x)          # extension word part (optional)
(\d{2,5}))?    # extension number-part (optional))
)

# recompile(r"((\d\d\d)|(\(\d\d\d\)))?(\s|-)?\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))?

""", re.VERBOSE)



# Create a regex for email addresses

emailRegex = re.compile(r"""
# some.+_thing@something.com

[a-zA-Z0-9.+_]+            # name part, \w symbol only includes letter, number and the underscore 
@                          # @ symbol
[a-zA-Z0-9.+_]+            # domain name part


""", re.VERBOSE)


# Get the text off the clipboard (pastes text that is currently on the clipboard)

text = pyperclip.paste()


# Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
print(extractedPhone)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])



print(allPhoneNumbers)
print(extractedEmail)

# TODO: Copy the extracted email/phone to the clipboard

results = "\n".join(allPhoneNumbers) + "\n".join(extractedEmail)
pyperclip.copy(results)

file = open("email_phone.txt", "w")

file.write(pyperclip.paste())

file.close()




