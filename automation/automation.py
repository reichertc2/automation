import re

with open('./assets/potential-contact.txt') as pcl:
    text_from_file = pcl.read()

def find_phone_numbers():
    phone_numbers = []
    numbers_a = phone_pattern_a()
    numbers_b = phone_pattern_b()
    numbers_c = phone_pattern_c()
    numbers_d = phone_pattern_d()

    # print(numbers_a)
    for number in numbers_a:
        phone_numbers.append(number)
    
    for number in numbers_b:
        phone_numbers.append(number)
    
    for number in numbers_c:
        phone_numbers.append(number)
    
    for number in numbers_d:
        phone_numbers.append(number)
    
    # print(phone_numbers.sort())
    phone_numbers.sort()

    phone_numbers_clean = []
    [phone_numbers_clean.append(x) for x in phone_numbers if x not in phone_numbers_clean]

    with open('./assets/phone_numbers.txt','w') as phone_file:
        for num in phone_numbers_clean:
            # print(num)
            phone_file.write(num)
            phone_file.write('\n')    
    # print(len(phone_numbers_clean))


def find_emails():
    pattern_email = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    emails = re.findall(pattern_email,text_from_file)
    # print(emails)
    emails_clean = []
    [emails_clean.append(x) for x in emails if x not in emails_clean]
    # print(emails_clean)
    emails_clean.sort()
    with open('./assets/emails.txt','w') as email_file:
        for email in emails_clean:
            # print(email)
            email_file.write((email))
            email_file.write('\n')
    # print(len(emails))



def phone_pattern_a():
    pattern_phone_a = r"\d{3}\d{3}\d{4}"
    phone_numbers = re.findall(pattern_phone_a,text_from_file)
    modified_numbers = []
    for number in phone_numbers:
        # mod = ' '
        seg0 = number[0:3].split() 
        seg1 = number[3:6].split()
        seg2 = number[6:10].split()
        # print(area)
        mod = f'{seg0[0]}-{seg1[0]}-{seg2[0]}'
        modified_numbers.append(mod)
        # print(mod)
    return modified_numbers

def phone_pattern_b():
    pattern_phone_a = r"\d{3}\d{4}"
    phone_numbers = re.findall(pattern_phone_a,text_from_file)
    modified_numbers = []
    for number in phone_numbers:
        seg0 = number[0:3].split() 
        seg1 = number[3:7].split()
        # print(area)
        mod = f'206-{seg0[0]}-{seg1[0]}'
        modified_numbers.append(mod)
        # print(mod)
    return modified_numbers

def phone_pattern_c():
    pattern_phone_a = r"\d{3}-\d{3}-\d{4}"
    phone_numbers = re.findall(pattern_phone_a,text_from_file)
    modified_numbers = []
    for number in phone_numbers:
        # print(area)
        mod = number
        modified_numbers.append(mod)
        # print(mod)
    return modified_numbers

def phone_pattern_d():
    pattern_phone_a = r"[(]\d{3}[)]\d{3}.\d{4}"
    phone_numbers = re.findall(pattern_phone_a,text_from_file)
    modified_numbers = []
    for number in phone_numbers:
        seg0 = number[1:4].split() 
        seg1 = number[5:8].split()
        seg2 = number[9:13].split()
        mod = f'{seg0[0]}-{seg1[0]}-{seg2[0]}'
        modified_numbers.append(mod)
        # print(mod)
    return modified_numbers


find_phone_numbers()
find_emails()