import re

with open("./potential-contacts.txt", "r") as f:
  text_from_file = f.read()
  # print(text_from_file)


# Phone number finder
pattern = r"(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}"

numbers = re.findall(pattern, text_from_file)

x = open("phone_numbers.txt" , "w")

for number in numbers:
  x.write(f"{number}\n")

#email finder
pattern2 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

emails = re.findall(pattern2, text_from_file)

z = open("emails.txt" , "w")

for email in emails:
  z.write(f"{email}\n")
