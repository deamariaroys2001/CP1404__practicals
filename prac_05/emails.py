
"""
Dea Roys
CP1404 Practicals week 5
emails
"""

#
# def main():
#     """Ask user their email address and check if it's their name."""
#     user_email_name = {}
#     email = input("Email:")
#     while email != "":
#         name = name_from_email(email)
#         check = input("Is your name {} ? (Y/n):".format(name))
#         if check.upper() != "Y" and check != " ":
#             name = input("Name:")
#         user_email_name[email] = name
#         email = input("Email:")
#
#     for email, name in user_email_name.items():
#         print("{} ({})".format(name,email))
#
#
# def name_from_email(email):
#     """get name from email address."""
#     name_only = email.split('@')[0]
#     parts = name_only.split('.')
#     name = " ".join(parts).title()
#     return name
#
#
# main()

# """
# Lee Crawford
# CP1404/CP5632 Practical
# emails
# """

USERS = {}


def main():
    email = input("Email: ")
    while email != "":
        name_and_email = email.split("@")
        USERS[email] = return_name_from_email(name_and_email)
        print("Is your name {}?".format(USERS[email]).title(), end="")
        answer = input(" (Y/n) ").lower()
        if answer == "n" or answer == "no":
            USERS[email] = input("Name: ")
        email = input("Email: ")
    for key, name in USERS.items():
        print("{} ({})".format(name, key))


def return_name_from_email(name_and_email):
    """check if names separated by '.' then return string"""
    if "." in name_and_email[0]:
        names = name_and_email[0].split(".")
        user_name = "{} {}".format(names[0], names[1])
    else:
        user_name = name_and_email[0]
    return user_name


main()
