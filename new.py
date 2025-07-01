import regex
pat='(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&^#()_+=-]).{8,}'
pwrd=input("Enter your password: ")
if regex.match(pat,pwrd):
    print("Password is valid")
else:
    print("Password is not valid")