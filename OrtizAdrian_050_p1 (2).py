# Filename: OrtizAdrian_050_p1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME:Adrian D Ortiz López
# STUDENT ID:802 22 0506
# SECTION:050
############      DEFINE CONSTANTS BELOW      ############
KILOMETERS_PER_MILE = 1.60934
MILES_PER_KILOMETER=0.6213712
POUNDS_PER_KILOGRAM=2.2046244



############       ADD YOUR CODE BELOW        ############


############ DO NOT MODIFY THE SECTION BELOW  ############


def print_program_menu(): #this function was created to print the menu
    print("\n--------")
    print( "Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Miles/hour to kilometers/hour")
    print("6. Exit")



def main():
    done = False
    while not done:
        print_program_menu() #this functio print the menu, you don't need to change it
        userOption = input("Enter option: ")
        if userOption.isdigit()== False or int(userOption) <=0 or int(userOption)>6:
          print()
          print("Option invalid")
        else:# This Verify that a number was input
         numericOption = int(userOption)
        

         if numericOption ==1:
          print()
          miles=(input("Enter the miles to be converted: "))
          if miles.isdigit()==True: 
             km=round((float(miles)/0.6213712),2)
             print(float(miles),'miles',"are equivalent to",km,'kilometers')
          else:
             print()
             print("Option invalid")
           

         if numericOption==2:
           print()
           kilometers=input("Enter the kilometers to be converted: ")
           if kilometers.isdigit()==True:
             mi=round((int(kilometers)/1.609344),2)
             print(float(kilometers) ,"kilometers","are equivalent to",mi,"miles")
           else:
             print("Option invalid")
         if numericOption==3:
           print()
           Pounds=(input("Enter the pounds to be converted: "))
           if Pounds.isdigit()==True:
             kg=round((int(Pounds)/2.2046),2)
             print(float(Pounds) ,"pounds","are equivalent to",kg,"kilograms")
           else:
             print()
             print("Option invalid")
         if numericOption==4:
           print()
           Kilograms=input("Enter the kilograms to be converted: ")
           if Kilograms.isdigit()==True:
             lbs=round((int(Kilograms)*2.2046),2)
             print(float(Kilograms) ,"kilograms","are equivalent to",lbs,"pounds")
           else:
             print()
             print("Option invalid")
         if numericOption ==5:
           print()
           milesh=(input("Enter the miles/hours to be converted: "))
           if milesh.isdigit()==True:
             km=round((int(milesh)/0.6213712),2)
             print(float(milesh),'mph',"are equivalent to",km,'kph')
           else:
             print()
             print("Option invalid")
         elif numericOption == 6:
           print("Thanks for using the unit conversion program!")
           done=True
        
            
# This line makes python start the program from the main function
if __name__ == "__main__":
    main()



