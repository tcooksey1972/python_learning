#Why use if statements when you want to execute a block of code only if a certain condition is met
#when We want to match conditions to being true not.
#How if true run code.  if-else and if elif-else are also opitons

is_male = False  #change these booleen values to test the function
is_tall= True
if is_male and is_tall:                #Using or and and keyword to evaluate two condions, if one is true execute code
    print("You are a tall male!")
elif is_male and not(is_tall):   #Using not keyword to check condiitons of a specific parameter
    print("You are a short male!")
elif is_male or is_tall:
    print("You are male or you are tall or both!")
else:
    print("You are neither male or tall")