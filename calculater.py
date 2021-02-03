print("Calculater")
# inst is for instructions. put yes or no.
inst = input("if you want instructions,write yes.If you dont want it,write no.")
if inst == 'yes' :
	print("write add for addition,sub for subtraction,multiply for multiplication,divide for division.")
	if inst == 'no' :
		print("lets continue!")
operation = input("Select Your Operation: ")
if operation == 'add' :
	add = input("First number: ")
	add2 = input("Second Number: ")
	add_result = int(add) + int(add2)
	print(add_result)
elif operation == 'sub' :
	sub = input('First Number: ')
	sub2 = input('Second Number: ')
	sub_result = int(sub) - int(sub2)
	print(sub_result)
elif operation == 'multiply' :
	multiply = input("First Number: ")
	multiply2 = input("Second Number: ")
	multiply_result = int(multiply) * int(multiply2)
	print(multiply_result)
elif operation == 'divide' :
	divide = input("First Number: ")
	divide2 = input("Second Number: ")
	div_result = int(divide) / int(divide2)
	print(div_result)
	
	