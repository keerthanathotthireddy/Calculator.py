# importing modules
import addition
import subtraction
import multiplication
import division
import modulusdivision

operations = (
    "1.Addition \n",
    "2. Subtraction \n",
    "3. Multiplication \n",
    "4. Division \n",
    "5. Modulusdivision \n"
)



# main function
if __name__ == "__main__":
    print(*operations)
    choice = int(input("Please select your operation: "))
    if choice == 1 :
        a,b = map(int,input("Please enter two values with spaces : ").split())
        res = addition.add(a,b)
        print("Sum of two numbers is:",res)
    elif choice == 2 :
        a,b = map(int,input("Please enter two values with spaces : ").split())
        res = subtraction.sub(a,b)
        print("Subtraction of two numbers is:",res)
    elif choice == 3 :
        a,b = map(int,input("Please enter two values with spaces : ").split())
        res = multiplication.mul(a,b)
        print("multiplication of two numbers is:",res)
    elif choice == 4 :
        a,b = map(int,input("Please enter two values with spaces : ").split())
        res = division.div(a,b)
        print("division of two numbers is:",res)
    elif choice == 5 :
        a,b = map(int,input("Please enter two values with spaces : ").split())
        res = modulusdivision.mod(a,b)
        print("modulusdivision of two numbers is:",res)
    else:
        print("Please select in betwwen 1-5")

