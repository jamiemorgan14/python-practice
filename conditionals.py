is_male = False
is_tall = True

if is_male and is_tall:
    print("You are tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("You are either not male or not tall or neither")
