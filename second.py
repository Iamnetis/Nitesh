def multiply(*numbers):
	multiply = 1
	for number in numbers:
		if number<0 :
			continue


		multiply *= number
	return multiply

print(multiply(1))
print(multiply(2,3))
print(multiply(5,6,7))