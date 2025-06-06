import sys
# Importing the sha512_crypt class from passlib to make the correct hashed password
from passlib.hash import sha512_crypt

#Hash from the shadow file
hash = "$6$xgLS35S6$2UjEq.dUhICPw9zgDVJXcQYQp/9ilLPQt/8Zgu0uwngI5mVvB1eKQG9SnVLjmOOfkB4Jjb5VSAXGXjY4Cf5k90"

#File where the list of passwords is kept
file = "passwords.txt"

try:
    #Open file in read mode
    with open(file, "r", encoding="utf-8") as f:
        #Loops through each line
        for line in f:
            #candidate ensures no whitespace
            candidate = line.strip()
            #Passlib's verify function to check if candidate matches hash
            try:
                if sha512_crypt.verify(candidate, hash):
                    print(f"Password found: {candidate}")
                    sys.exit(0)
            except ValueError:
                #Verify nethod throws an error if it isnt in the right format
                print("ValueError")
                sys.exit(1)

    sys.exit(1)

except FileNotFoundError:
    print(f"Error: Password file '{file}' not found.")
    sys.exit(1) 
