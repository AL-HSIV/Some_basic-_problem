first_num = int(input("Enter the first number of the fibonacci series... "))
second_num = int(input("Enter the second number of the fibonacci series... "))
num_of_terms = int(input("Enter the number of terms... "))
print(first_num,second_num)
print("The numbers in fibonacci series are : ")
while(num_of_terms-2):
   third_num = first_num + second_num
   first_num=second_num
   second_num=third_num
   print(third_num)
   num_of_terms=num_of_terms-1