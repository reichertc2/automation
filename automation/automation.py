import re

with open('./assets/potential-contact.txt') as pcl:
    text_from_file = pcl.read()

def find_phone_numbers():


    pattern_phone = r"\d\d{3}\d{3}\d{4}|\d{3}.\d{4}|\d{7}|\d{3}-\d{4}|\d-\d{3}-\d{3}-\d{4}|(?:(\d{3})\d{3}-\d{4})"

    phone_numbers = re.findall(pattern_phone,text_from_file)
    print(phone_numbers)
    with open('./assets/phone_numbers.txt','w') as phone_file:
        for num in phone_numbers:
            # print(num)
            phone_file.write(num)
            phone_file.write('\n')    
    print(len(phone_numbers))


def find_emails():
    pattern_email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    emails = re.findall(pattern_email,text_from_file)

    with open('./assets/emails.txt','w') as email_file:
        for email in emails:
            # print(email)
            email_file.write((email))
            email_file.write('\n')
    print(len(emails))



find_phone_numbers()
find_emails()