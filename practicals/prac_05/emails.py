def main():
    # Collect emails from user, extract names from emails,and allow user to confirm or correct the extracted names.
    email_to_name = {}
    email = input("Email: ").strip()
    while email:
        extracted_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()
        if confirmation in ('', 'y'):
            name = extracted_name
        else:
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ").strip()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    # Extract a name from an email address and return it to main function.
    name_part = email.split('@')[0]
    name = ' '.join(name_part.split('.')).title()
    return name

main()
