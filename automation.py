import re


# Take in a list of potential contacts and convert to email addresses and phone numbers

with open('potential-contacts.txt', 'r') as file:
    content = file.read()

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, content)

phone_pattern = r'((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}'
phone_numbers = re.findall(phone_pattern, content)
print('phone numbers', phone_numbers)

contact_list = []
for number in phone_numbers:
    formatted_numbers = re.sub(r'\D', '', number[0])
    print('phone number format', formatted_numbers)
    input()
    if len(formatted_numbers) == 7:
        formatted_numbers = '206-' + formatted_numbers
    elif len(formatted_numbers) == 10:
        formatted_numbers = f'{formatted_numbers[:3]}-{formatted_numbers[3:6]}-{formatted_numbers[6:]}'
    contact_list.append(formatted_numbers)

emails = sorted(list(set(emails)))
contact_list = sorted(list(set(contact_list)))

with open('emails.txt', 'w') as file:
    for email in emails:
        file.write(email + '\n')

with open('phone_numbers.txt', 'w') as file:
    for number in contact_list:
        file.write(number + '\n')

