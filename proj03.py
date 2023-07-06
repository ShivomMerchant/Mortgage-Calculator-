###########################################################
    #  Computer Project #3
    #
    #  price and taxes for each location 
    #  Initiate while loop to continue
    #       print welcome statements
    #       if statement to decide if location is in cities
    #           define each city with respective tax and price
    #       if statements for each imput 
    #           check if imputs are numbers if number change to float
    #           if not a number define varible 
    #       if statement for square foot and downpayment are nA
    #           if both NA then print not enough information
    #       if square foot imput is NA
    #           calculate cost without square foot
    #           print statement
    #       calculate cost, loan, taxes, expected monthly payment, and total monthly
    #       if location is not in given cities
    #           print statement
    #       if location is in cities 
    #           print statement
    #       if square foot is a number
    #           prompt user for recipt 
    #               if statement for recipt
    #                   initiate while loop for recipt 
    #                       calculate intrest, balance, and principal
    #                       print table
    #       prompt user to continue 
    #       if continues
    #           print welcome statements
    ###########################################################

NUMBER_OF_PAYMENTS = 360    # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668
#define cities
print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
continue_str = 'Y'
cities=("Seattle","San Francisco","Austin","East Lansing",)

#start while loop and ask for location
while continue_str == "Y":
    print("\nEnter a value for each of the following items or type 'NA' if unknown ")
    location_str = str(input("\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? "))

    #define each location with price and tax rates
    if location_str not in cities:
        price = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        tax = AVERAGE_NATIONAL_PROPERTY_TAX_RATE
    elif location_str == "Seattle" :
        price = SEATTLE_PRICE_PER_SQ_FOOT
        tax = SEATTLE_PROPERTY_TAX_RATE
    elif location_str == "San Francisco" :
        price = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        tax = SAN_FRANCISCO_PROPERTY_TAX_RATE
    elif location_str == "Austin" :
        price = AUSTIN_PRICE_PER_SQ_FOOT
        tax = AUSTIN_PROPERTY_TAX_RATE
    elif location_str == "East Lansing" :
        price = EAST_LANSING_PRICE_PER_SQ_FOOT
        tax = EAST_LANSING_PROPERTY_TAX_RATE

    #prompt user for values, if a number change to a float
    #define if NA
    sqfoot_str = str(input("\nWhat is the maximum square footage you are "
                           "considering? "))
    if sqfoot_str.isnumeric() == True:
        sqfoot_int= float(sqfoot_str)
    else:
        sqfoot_str = ""

    maxpayment_str = input("\nWhat is the maximum monthly payment you can"
                           " afford? ")
    if maxpayment_str.isnumeric() == True:
        maxpayment_int = float(maxpayment_str)
    else:
        maxpayment_int = 0

    downpayment_str = (input("\nHow much money can you put down as a down"
                             " payment? "))
    if downpayment_str.isnumeric() == True:
        downpayment_int = float(downpayment_str)
    else:
        downpayment_int = 0

    annualrte_str = (input("\nWhat is the current annual percentage rate? "))
    print("")

    #if city that is not given use national price/rates
    if location_str not in cities:
        print("Unknown location. Using national averages for price per square"
              " foot and tax rate.")
        print("\n")
    
    #define monthly rate from annual rate
    if annualrte_str != "NA":
        annualrte_int = float(annualrte_str)/100
        monthlyrate = float(annualrte_int/12)

    #use national rate if not given
    else: 
        annualrte_int = APR_2023
        monthlyrate = float(annualrte_int/12)
        
    #if user imputs NA for square footage and down payment 
    #print not enough information
    if sqfoot_str ==("NA") and str(downpayment_int) == ("NA"):
        print("Not enough information \n")
    
    #calculate cost without square footage given
    if sqfoot_str.isnumeric() == False:
        cost = ((maxpayment_int*(((monthlyrate+1)**360)-1))/(monthlyrate*\
               ((monthlyrate+1)**360)))+ downpayment_int
    else:
        cost = price * sqfoot_int
        
    #calculations for loan, taxes, square footage, and monthly payments
    loan= cost - float(downpayment_int)
    proptax= cost*(tax/12)
    sqft= cost/price
    monthly_payment_expected =((loan*(monthlyrate*(1+monthlyrate)\
            **NUMBER_OF_PAYMENTS))/(((1+monthlyrate)**NUMBER_OF_PAYMENTS)-1))
    totalmonthly_payment = monthly_payment_expected + proptax
    
    #if no square foot given print statements
    if sqfoot_str.isnumeric() == False:
        sqft= cost/price
        print("\nIn", str(location_str) + ", a maximum monthly payment of $"+ 
        "{:.2f}".format(maxpayment_int)+" allows the purchase of a house of", 
        int(sqft), "sq. feet for $"+str(int(cost)))
        print("\t assuming a 30-year fixed rate mortgage with a $"+
        str(int(downpayment_int)),"down payment at", 
        str(round((annualrte_int*100),1))+ "% APR.")
   
   #if square footage is given print statements
    else:
        totalmonthly_payment = monthly_payment_expected + proptax
        if location_str not in cities:
            print("In the average U.S. housing market, an average",
            int(sqfoot_int), "sq. foot house would cost $"+str(int(cost))+".")
        else:
            print("\nIn", str(location_str)+", an average",int(sqfoot_int),
                  "sq. foot house would cost $"+str(int(cost))+".")
        
        print("A 30-year fixed rate mortgage with a down payment of $"+
              str(int(downpayment_int)), "at " +
              str(round((annualrte_int*100),1)) +"% APR results")
        print("\tin an expected monthly payment of $"+ "{:.2f}".format(proptax), 
              "(taxes) + $"+str(round((monthly_payment_expected),2)), 
              "(mortgage payment) = $"+"{:.2f}".format(totalmonthly_payment))

        #if monthly payment is higher than your max monthly
        #print whether you can afford this house
        if maxpayment_str.isnumeric():
            if totalmonthly_payment <= maxpayment_int:
                print("Based on your maximum monthly payment of $"+
                "{:.2f}".format(maxpayment_int), "you can afford this house.")
            else:
                print("Based on your maximum monthly payment of $"+
                "{:.2f}".format(maxpayment_int), "you cannot afford this"
                " house.")
    
    #if square foot is given
    if sqfoot_str.isnumeric():  
    
        monthlypaymentschedule = input("\nWould you like to print the "
                                       "monthly payment schedule (Y or N)? ")
        if monthlypaymentschedule =="Y":
            print("\n Month |  Interest  |  Principal  |   Balance    \n==="
                  "=============================================")
            bal=loan
            i=0

            #start while loop for table
            while i < 360:
                #calculate varibles 
                i +=1
                intrest = monthlyrate*bal
                principal = monthly_payment_expected - intrest
                #use format to create table with spaces
                if i < 100:
                    print(" {:3.0f}   | ${:>9.2f} | ${:>10.2f} | "
                          "${:>11.2f}".format(i,intrest,principal,bal))
                #decrease one space at beggining if over 100 statements
                else:
                    print(" {:4.0f}  | ${:>9.2f} | ${:>10.2f}"
                          " | ${:>11.2f}".format(i,intrest,principal,bal))
                bal = bal-principal
    
    #prompt whether to continue
    continue_str =input("\nWould you like to make another attempt (Y or N)? ")
    if continue_str == "Y":
        print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
        