# Email Slicer with Python

email=input('enter your email:').strip()
username=email[:email.index("@")]
# a=email.index("@")
# print(a)
domain_name=email[email.index("@")+1:]

format_=(f"your user name '{username}' and domain name '{domain_name}'")
print(format_)