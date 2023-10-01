#When? we run our functions we sometimes want it to return results
#Why?  We want info back from the function
#how?  Useing the return keyword to return a value from a function

def cube(num):   #define a fucntion called cube
    return num*num*num  #using return to return the value of the math to create the function
                        #no lines of code can follow the line that has return in our function

# cube(3)  #Calling our cube function and passing a number in the () to be cubed but nothing returned because no output

result = cube(3)  #storing our returned value in a variable called result
print(result)  #print the value of our cubed number as the variable 'result'