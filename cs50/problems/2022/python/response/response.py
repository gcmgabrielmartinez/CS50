#pip install validators
#pip install validator-collection

import validators
# from validator_collection import validators, checkers, errors

e_mail = input("What's your e-mail?")

if validators.email(e_mail):
    print("Valid")
else:
    print("Invalid")