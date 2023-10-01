#What?  comparison operators are used to compare values and return a Boolean result (True or False) based on the evaluation of the condition
#When?  When we want to compare things in our code and return the results
#How?  equal to(==), not equal to(!=), greater than or equal to(>=),less than or equal to(<=), Less(<) Greater(>)
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:   #using comaparison operators to evalute true or false
        return num1
    elif num2 >= num2 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 4, 5))