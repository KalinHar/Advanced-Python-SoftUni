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


ALL_DOMAINS = {'com': 1, 'bg': 1, 'org': 1, 'net': 1}
emails = []

entry_emails()


for em in emails:
    try:
        name, domain = em.split("@")
        len_name_check = name[4]
        check_domain = ALL_DOMAINS[domain.split(".")[-1]]
    except ValueError:
        print("Email must contain @")
        # raise MustContainAtSymbolError("Email must contain @")
    except IndexError:
        print("Name must be more than 4 characters")
        # raise NameTooShortError("Name must be more than 4 characters")
    except KeyError:
        print("Domain must be one of the following: .com, .bg, .org, .net")
        # raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
