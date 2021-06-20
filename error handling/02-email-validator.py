import errors

emails = []
email = input()
while email != "End":
    emails.append(email)
    email = input()

for em in emails:
    if "@" not in em:
        raise errors.MustContainAtSymbolError("Email must contain @")
    elif len(em.split("@")[0]) < 5:
        raise errors.NameTooShortError("Name must be more than 4 characters")
    elif em.split("@")[-1].split(".")[-1] not in ('com', 'bg', 'org', 'net'):
        raise errors.InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

# dom_checker = {'com': 1, 'bg': 1, 'org': 1, 'net': 1}
# for em in emails:
#     try:
#         name, domain = em.split("@")
#         len_name_check = name[4]
#         check_dom = dom_checker[domain.split(".")[-1]]
#     except ValueError:
#         raise errors.MustContainAtSymbolError("Email must contain @")
#     except IndexError:
#         raise errors.NameTooShortError("Name must be more than 4 characters")
#     except KeyError:
#         raise errors.InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#     else:
#         print("Email is valid")
