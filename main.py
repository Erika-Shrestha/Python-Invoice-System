'''operation, write modules is imported'''
import operation
import write
dis_all=operation.display_lands() #display_lands() function is called from operation module and assigned to variable dis_all
dis_rent=operation.display_available()#display_available() function is called from operation module and assigned to variable dis_rent
dis_return=operation.display_not_available()#display_unavailable() function is called from operation module and assigned to variable dis_return

'''A function for design format for home page'''
def home_page():
    """
    displays the design of the system

    the company greets the visited customer with short details about the company
    displays 5 options with their functionality

    the function does not return any value
    
    """
    print("_"*153)
    print("\n")
    print("\t\t\t\t\t\t\t\tTECHNO PROPERTY COMPANY\t\t\t\t\t\t\t\t")
    print("\n")
    print("\t\t\t\t\t\t\t\t"," ","324 Himalaya Road",  "\t\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t\t\t"," ","","Kathmandu,Nepal\t\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t\t\t","","Phone no: 9823733085\t\t\t\t\t\t\t\t")
    print("\n")
    print("="*153)
    print(" ")
    print("\t\t\t\tGreetings from our organisation.Our valued customer, we are happy to have you!  :)")
    print(" ")
    print("."*153)
    print("\n")
    print("~"*56,"PLEASE SELECT YOUR CHOICE OF OPERATION","~"*57)
    print("\n\n")
    print(" > PLEASE ENTER (1) FOR DISPLAY OF LAND")
    print(" ")
    print(" > PLEASE ENTER (2) FOR RENTING OF LAND")
    print(" ")
    print(" > PLEASE ENTER (3) FOR RETURNING OF LAND")
    print(" ")
    print(" > PLEASE ENTER (4) TO KNOW ABOUT THE COMPANY")
    print(" ")
    print(" > PLEASE ENTER (5) TO EXIT")
    print("\n\n")
    print("."*153)

home_page()


'''A function for the customer to select operations'''
def operation_page():
    """
    select any provided 5 options

    The customer is asked to select and input value among given 5 options
    the options are:
    option 1: To view all the lands in the company
    option 2: To view available lands where customer can select one or more lands to rent for
    option 3: To view unavailable lands where customer can select one or more lands to return for
    option 4: To view the Q&As and details about the company
    option 5: To exit from the system

    The function does not return any value
    """
    loop=True
    while loop:
        print(" ")
        try:
            input_operation= int(input("\tSELECT YOUR OPERATION ~ "))
            if(input_operation==1): 
                print(" ")
                print("_"*153)
                print(" ")
                print("\t\t","  ","KITTA NUMBER\t","","CITY\t\t","     ","DIRECTION\tANNA\t\tPRICE(RS)\tAVAILABILITY")
                print("_"*153)
                print(" ")
                print(dis_all)      #the variable dis_all where the display_lands function is assigned is called
                print("_"*153)
            elif(input_operation==2):
                print(" ")
                print("> ONLY LANDS THAT ARE AVAILABLE FOR RENT ARE DISPLAYED ")
                print("_"*153)
                print(" ")
                print("\t\t","  ","KITTA NUMBER\t","","CITY\t\t","     ","DIRECTION\tANNA\t\tPRICE(RS)\tAVAILABILITY")
                print("_"*153)
                print(" ")
                print(dis_rent)     #the variable dis_rent where the display_available function is assigned is called
                print("_"*153)
                print("\n")
                print("~"*43+"AFTER THE NECESSARY INFORMATION IS ENTERED, THE BILL WILL BE GENEREATED"+"~"*39)
                print("\n")
                print(write.gen_rent_invoice())      #the gen_rent_invoice() function from write is called for printing each unique rent bill
            elif(input_operation==3):
                print(" ")
                print("> ONLY LANDS THAT ARE UNAVAILABLE FOR RETURN ARE DISPLAYED ")
                print("_"*153)
                print(" ")
                print("\t\t","  ","KITTA NUMBER\t","","CITY\t\t","     ","DIRECTION\tANNA\t\tPRICE(RS)\tAVAILABILITY")
                print("_"*153)
                print(" ")
                print(dis_return)       #the variable dis_return where the display_unavailable function is assigned is called
                print("_"*153)
                print("\n")
                print("~"*43+"AFTER THE NECESSARY INFORMATION IS ENTERED, THE BILL WILL BE GENEREATED"+"~"*39)
                print("\n")
                print(write.gen_return_invoice())       #the gen_return_() function from write is called for printing each unique return bill
            elif(input_operation==4):
                print(operation.about_us())     #the function is called to display the details of the company
            elif(input_operation==5):
                print("\n\n\t\t\tTHE SYSTEM IS EXITING.....")
                print("\n\n\t\t\tTHANK YOU FOR YOUR VISIT! :)")
                break

            else:
                print("\n\t XX     Dear customer, please enter only the options that are offered     XX")
        except:
            print("\n\t XX     Dear customer, please enter only the options that are offered      XX")

operation_page()     #calling the function

            
            
            
        
            

