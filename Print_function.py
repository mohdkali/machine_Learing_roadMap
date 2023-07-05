print("La illaha illallah, muhammadur rasulullah")

# we can also print nultiple data types by seprating them with the comma like below.

print('Allah','Muhammad')

# if we want the sepration between the data in the output should not be the space but we want it to be a - so we can use the sep parameter like below
# 

print('Allah','Muhammad', sep='-')

print('Ällah')
print('huakbar')
# if we we run the just above code we will get the output in two diffrent lines
# Output  = Allah
# Output = huuakbar
# 
# BUt if we want both output in the same line or wants to change the end parameter of the print fuction
# In print fuction there is a default parameter called end function in the end of the fuction the end paramter
# passes a escape sequence charater '\n' by which the next statement prints in a next line but if we wantit to be printed in the same line or we want to change the end charateer like below code


print('Ällah',end=' ') # Now this will change the end parameter and we will get the both output in the same line, like such
print('huakbar')

# Or we can also do this

print('Ällah',end='') 
print('huakbar')