"""
Dea Roys
CP1404 Practicals week 5
emails
"""


def main():
    """Ask user their email address and check if it's their name."""
    user_email_name = {}
    email = input("Email:")
    while email != "":
        name = name_from_email(email)
        check = input("Is your name {} ? (Y/n):".format(name))
        if check.upper() != "Y" and check != " ":
            name = input("Name:")
        user_email_name[email] = name
        email = input("Email:")

    for email, name in user_email_name.items():
        print("{} ({})".format(name,email))


def name_from_email(email):
    """get name from email address."""
    name_only = email.split('@')[0]
    parts = name_only.split('.')
    name = " ".join(parts).title()
    return name


main()
