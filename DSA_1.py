#Write a program which sums the multiples of 3 and 5 until 1000:

mult_list = []
for k in range(1, 334):
    mult = 3 * k
    mult_list.append(mult)
print('Sum of multiples of 3 until 3000 is: ',sum(mult_list))
mult_list1 = []
for k in range(1, 200):
    mult = 5 * k
    mult_list1.append(mult)
print('Sum of multiples of 5 until 3000 is: ',sum(mult_list1))
mul_sum = sum(mult_list) + sum(mult_list1)
print('The sum of multiples of 3 & 5 until 3000 is:',mul_sum)
