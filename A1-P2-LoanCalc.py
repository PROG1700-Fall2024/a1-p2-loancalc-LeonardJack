#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Firstly we need to take in our 3 inputs of loan, interest rate and the amount of years
    #secondly we need to do some calculations first being the I in our equation
    #Then we do the more complex calculation which I cant explain exactly because math isnt my forte
    #however just know it uses our inputs and our previous calculation to calculate the weekly payment
    #Finally we format and print our weekly payment

    loanAmt = int(input("Enter your loan amount: "))
    interestPercent = float(input("Enter your interest percentage: ")) #INPUTS
    totalYears = int(input("Enter the amount of years: "))

    theI = interestPercent / 5200 #calculation for I
    weeklyPayment = theI / (1-((1+theI)**(-52 * totalYears))) * loanAmt     #equation for weekly payment


    print("Your weekly payment will be {0:.2f}".format(weeklyPayment))      #Properly formatted print statement

    # YOUR CODE ENDS HERE

main()