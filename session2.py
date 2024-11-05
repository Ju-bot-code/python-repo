# ===  EXPRESSION
# 1+1 or "hello"
# expression return a value


# === STATEMENT
# statemnt is a line of code that performs an action 
# statement is an operation on a value 
# data = 1+1
# print(data)


# Note
# we can have multiple statements in a single line using a semicolon
data=1+1 ; print(data)
print(type(data),'data type of data')

print("is data a instance of str",isinstance(data,str))
print("is data a instance of int",isinstance(data,int))
print("is data a instance of float",isinstance(data,float))


print(f"convting data into str:{str(data)}",isinstance(str(data),str))

print(f"convting data into str:{float(data)}",isinstance(float(data),float))