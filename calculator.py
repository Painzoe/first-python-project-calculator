while True:
     print("""
      Choose an operation you want to perform.
     1. Addition
     2. Subtraction
     3. Multiplication
     4. Division
     5. Exit
        """)
     operation = input("Enter an operation: ")
     if operation == "5" :
         break #exit()
     else:
         num1 = int(input("Enter an integer number: "))
         num2 = int(input("Enter an integer number: "))
         if operation == "1":
              print(num1,"+",num2,"=" ,num1+num2)
         elif operation == "2":
              print(num1,"-",num2,"=" ,num1-num2)
         elif operation == "3":
              print(num1,"*",num2,"=" ,num1*num2)
         elif operation == "4":
              if not num2 == 0:
                  print(num1,"/",num2,"=" ,num1/num2)
              else:
                  print("Any number cannot be divided by zero")
         else :
             print("Invalid input")