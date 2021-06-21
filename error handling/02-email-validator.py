class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def entry_emails():
    while True:
        email = input()
        if email == "End":
            break
        emails.append(email)


def valid_email(em):
    if "@" not in em:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(em.split("@")[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
    elif em.split("@")[-1].split(".")[-1] not in ALL_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")


ALL_DOMAINS = ('com', 'bg', 'org', 'net')
emails = []

entry_emails()

for email in emails:
    valid_email(email)
