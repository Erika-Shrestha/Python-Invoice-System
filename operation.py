
'''read module is import and datetime library is import'''
import read
import datetime
dictionary=read.read_file() #calling the read_file function from read module and assign to variable dictionary


'''A function to display all the lands from the company'''
def display_lands():
        """
        takes dictionary to iterate over pairs

        The iteration over pairs is performed and stored into variable display
        display is added to variable display_all one by one as a single string

        returns:
        The return value is display_all

        """
        display_all=""                  #an empty single string is initialized
        for keys,values in dictionary.items():          #iterates key,values from the dictionary
                display="\t\t\t"+str(keys)+"\t\t"+str(values[0])+"\t\t"+str(values[1])+"\t\t"+str(values[2])+"\t\t"+str(values[3])+"\t\t"+str(values[4])
                display_all +=display+"\n\n"            #Each pairs is stored in display_all variable as a single string
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        return display_all

'''A function to display only the available lands from the company'''
def display_available():
        """
        takes dictionary to display only available lands
        
        an empty dictionary dict2 and empty string display_available is initialized
        the iteration over pairs of dictionary is performed and when the iterated values fourth index is available
        the pairs is added to the new dictionary dict2
        takes pairs of dict2 for iteration
        the pairs are assigned to variable display
        display is added to variable display_all one by one as a single string
        
        returns:
        The return value is display_available

        """
        dict2={}                #an empty dictionary is initialized
        display_available=""            #an empty single string is initialized
        for key,values in dictionary.items():           #iterates key,values from the dictionary
                if values[4]==' AVAILABLE':
                    dict2[key]=values           #values are assigned to the key of dict2
        for key,values in dict2.items():
                display=("\t\t\t"+str(key)+"\t\t"+str(values[0])+"\t\t"+str(values[1])+"\t\t"+str(values[2])+"\t\t"+str(values[3])+"\t\t"+str(values[4]))
                display_available+=display+"\n\n"       #Each pairs of dict2 is stored in display_available variable as a single string

        return display_available

'''A function to display only the unavailable lands from the company'''
def display_not_available():
        """
        takes dictionary to display only unavailable lands
        
        an empty dictionary dict3 and empty string display_unavailable is initialized
        the iteration over pairs of dictionary is performed and when the iterated values fourth index is not available
        the pairs is added to the new dictionary dict3
        takes pairs of dict3 for iteration
        the pairs are assigned to variable display
        display is added to variable display_all one by one as a single string
        
        returns:
        The return value is display_unavailable

        """
        dict3={}                #an empty dictionary is initialized
        display_unavailable=""          #an empty single string is initialized
        for key,values in dictionary.items():           #iterates key,values from the dictionary
                if values[4]==' NOT AVAILABLE':
                    dict3[key]=values           #values are assigned to the key of dict3
        for key,values in dict3.items():        
                display=("\t\t\t"+str(key)+"\t\t"+str(values[0])+"\t\t"+str(values[1])+"\t\t"+str(values[2])+"\t\t"+str(values[3])+"\t\t"+str(values[4]))
                display_unavailable+=display+"\n\n"     #Each pairs of dict3 is stored in display_unavailable variable as a single string
                
                    
        return display_unavailable

'''A function to ask the customer for necessary details to rent land'''
def rent_kitta():

        """
        takes necessary details from the customer to prepare each unique rent bill

        this function ask valid customer name, customer phone number, kitta number, anna number, duration of rent
        if any of the input is not valid such as non-numeric for kitta number and duration of rent, an error message
        is displayed

        takes one or more rented land if the customer inputs yes to want to rent more
        but all the input is erased if no is entered for the confirmation message

        returns:
        A customer name, customer phone number, date and time rented and grandtotal
        A 2d list with variable customer_rental_info is also returned
        
        """

        customer_rental_info=[]         #empty list is initialized

        print("\t<<CUSTOMER DETAILS>>\n")

        '''name_valid loop continues until the condition is fulfilled'''
        name_valid=True
        while name_valid:
                customer_name=input("\n\t\tDear customer, Please provide your full name ~ ").upper()
                if len(customer_name)>2 and customer_name.isalpha():    # isalpha() ensures that the input is only in alphabets
                        name_valid=False
                else:
                        print("\n\t\t\t XX   Dear customer, please provide a genuine full name   XX\n")
        
        '''phone_valid loop continues until the condition is fulfilled'''                
        phone_valid= True
        while phone_valid:
                customer_phonenumber=input("\n\t\tDear "+customer_name+","+" Please provide your personal phone number ~ ")
                if len(customer_phonenumber)==10 and (customer_phonenumber[0]=="9" and customer_phonenumber[1]=="8" or customer_phonenumber[1]=="7"): #the first 2 index should be 98 or 97 with a total of 10 digits
                        phone_valid=False
                else:
                        print("\n\t\t\tXX     Dear "+customer_name+", provide a valid phone number    XX\n")
                
        print("\n\n\t<<LAND DETAILS>>\n")

        '''a whole loop continues until all the input values is correct'''
        entire_loop=True
        while entire_loop:

                '''first loop continues until the valid kitta number is entered'''
                first_loop=True
                while first_loop:

                        '''exceptional handling for ValueError'''
                        try: 
                                kitta_number=int(input("\n\t\tKindly include the kitta number of the land you wish to rent ~ "))
                                for i in customer_rental_info:  #iterates over customer_rental_info
                                        already_land=i[0]       

                                if not customer_rental_info or kitta_number!=already_land:      #if customer_rental_info is empty or the kitta number is different
                                        if kitta_number in dictionary:
                                                if dictionary[kitta_number][4]==" NOT AVAILABLE":
                                                        print("\n\t\tXX   Dear "+customer_name+" ,the kitta number does not belong to any available lands   XX\n")
                                                        
                                                elif dictionary[kitta_number][4]==" AVAILABLE":
                                                        break
                                        
                                                else:
                                                        print("\n\t\t\tXX   Dear "+customer_name+", please provide a genuine kitta number   XX\n")
                                                        continue
                                        else:
                                                print("\n\t\t\tXX   Dear "+customer_name+", please provide a genuine kitta number   XX\n")

                                else:
                                        print("\n\t\tXX   Dear "+customer_name+", you're previously rented the property with this kitta number   XX\n")
                                        continue
                                
                        except:

                                print("\n\t\t\tXX   Dear "+customer_name+", please provide a genuine kitta number   XX\n")
                                continue
                                
                '''next loop continues until valid anna number is entered'''
                next_loop=True
                while next_loop:
                        '''exceptional handling for ValueError'''
                        try:
                                anna_num=int(input("\n\t\tKindly include the number of anna of the land you want to rent ~ "))
                                if kitta_number in dictionary:  
                                        if dictionary[kitta_number][2]==str(anna_num) or dictionary[kitta_number][2]==" "+str(anna_num):
                                                break
                                        else:
                                                print("\n\t\t\txx Dear "+customer_name+", kitta number "+str(kitta_number)+" has "+str(dictionary[kitta_number][2])+" "+"anna of land"+"xx\n")
                                                continue

                        except:
                                print("\n\t\t\tXX      Dear "+customer_name+", the quantity of anna you are looking for is not available       XX\n")
                                continue

                '''continued loop continues until valid duration for rent is entered'''
                continued_loop=True
                while continued_loop:
                        '''exceptional handling for ValueError'''
                        try:
                                duration_rent_rent=int(input("\n\t\tKindly specify how long the land will be rented~ "))
                                if duration_rent_rent<=0:       #input negative value continues the loop
                                        print("\n\t\t\tXX        Dear "+customer_name+", the duration you are looking for is not available       XX\n")
                                        continue
                                else:
                                        break
                        except:
                                print("\n\t\t\tXX      Dear "+customer_name+", please provide a valid month       XX\n")
                                continue
                
                '''all the valid input values of asked details is assigned each to a new variable'''
                kitta_number_bill=kitta_number
                rent_land=dictionary[kitta_number][0]
                rented_land_direction=dictionary[kitta_number][1]
                anna_rent=anna_num
                rent_month=duration_rent_rent
                per_month_price=int(dictionary[kitta_number][3])
                total_rent_price=rent_month*per_month_price
                date_rented=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)
                time_rented=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second)

                '''the custoner_rental_info add the newly assigned variable'''
                customer_rental_info.append([kitta_number_bill,rent_land,rented_land_direction,anna_rent,rent_month,per_month_price,total_rent_price])      


                '''last loop repeats until any one from two options is entered'''
                last_loop=True
                while last_loop:
                        more_rent=input("\n\t\tDear "+customer_name+", Do you want to rent more lands? ~ ").lower()
                        if(more_rent=="no"):
                                entire_loop=False
                                break
                                
                        elif(more_rent=="yes"):
                                entire_loop=True
                                break
                        else:
                                print("\n\t\t\tXX      Dear "+customer_name+", please enter either yes or no       XX\n")
                                continue
                        
        '''outside loop is outside the entire loop and continues until any one from two options is entered '''
        outside_loop=True
        while outside_loop:
                confirmation_answer=input("\n\t\tDear "+customer_name+", Are you sure you want to rent the lands? ~ ").lower()
                if confirmation_answer=="yes":
                        print("\n\t\t\t\tPROCEEDING BILL....\n\n")      #exits the loop and prepares the bill
                        break
                                
                elif confirmation_answer=="no":
                        import main
                        main.home_page()        #calling the home_page() function from main module
                        main.operation_page()  #calling the operation_page() function from main module
                                 

                else:
                        print("\n\t\t\tXX      Dear "+customer_name+", please enter either yes or no       XX\n")
                        continue
                
        '''The total of all the rented lands is calculated'''             
        grandtotal=0
        for price in customer_rental_info:
                grandtotal+=price[6]  

        return customer_name,customer_phonenumber,date_rented,time_rented,customer_rental_info,grandtotal


'''A function to ask the customer for necessary details to return land'''
def return_details():
        
        """
        takes necessary details from the customer to prepare each unique return bill

        this function ask valid customer name, customer phone number, kitta number, anna number, duration of rent and return
        if any of the input is not valid such as non-numeric for kitta number and duration of rent and return, an error message
        is displayed
        A fine is added if the land is returned late

        takes one or more returned land if the customer inputs yes to want to return more
        but all the input is erased if no is entered for the confirmation message

        returns:
        A customer name, customer phone number, date and time returned and grandtotal after fine
        A 2d list with variable customer_return_info is also returned
        
        """

        customer_return_info=[]                 #empty list is initialized
        
        print("\t<<CUSTOMER DETAILS>>\n")

        '''name_valid loop continues until a valid name is entered'''
        name_valid=True
        while name_valid:
                customer_name=input("\n\t\tDear customer, Please provide your full name ~ ").upper() 
                if len(customer_name)>2 and customer_name.isalpha():            # isalpha() ensures that the input is only in alphabets
                        name_valid=False
                else:
                        print("\n\t\t\t XX   Dear customer, please provide a genuine full name   XX\n")

        '''phone_valid loop continues until the conditions are fulfilled'''
        phone_valid=True
        while phone_valid:
                customer_phonenumber=input("\n\t\tDear "+customer_name+","+" Please provide your personal phone number ~ ")
                if len(customer_phonenumber)==10 and (customer_phonenumber[0]=="9" and customer_phonenumber[1]=="8" or customer_phonenumber[1]=="7"): #the first 2 index should be 98 or 97 with a total of 10 digits
                        phone_valid=False
                
                else:
                        print("\n\t\t\tXX     Dear "+customer_name+", provide a valid phone number    XX\n")
                        continue
                        
        print("\n\n\t<<LAND DETAILS>>\n")
        grandtotal=0            #grandtotal initialized to zero
        fine_pay=0              #fine_pay initialized to zero

        '''entire loop continues until all the necessary details is entered'''
        entire_loop=True
        while entire_loop:

                '''first loop continues until the valid kitta number is entered'''
                first_loop=True
                while first_loop:
                        '''exceptional handling for ValueError'''
                        try:
                                kitta_number=int(input("\n\t\tKindly include the kitta number of the land you wish to rent ~ "))
                                for i in customer_return_info:  #iterates over customer_return_info
                                        already=i[0]
                                
                                if not customer_return_info or kitta_number!=already:   #if customer_return_info is empty or the kitta number is different
                                        if kitta_number in dictionary:
                                                if dictionary[kitta_number][4]==" NOT AVAILABLE":
                                                        break
                                                        
                                                elif dictionary[kitta_number][4]==" AVAILABLE":
                                                        print("\n\t\tXX   Dear "+customer_name+" ,the kitta number does not belong to any unavailable lands   XX\n")
                                                        continue
                                                else:
                                                        print("\n\t\t\tXX   Dear "+customer_name+", please provide a genuine kitta number   XX\n")
                                                        continue

                                                        
                                        else:
                                                print("\n\t\t\tXX   Dear "+customer_name+", please provide a genuine kitta number   XX\n")
                                                continue
                                else:
                                        print("\n\t\tXX   Dear "+customer_name+", you're previously returned the property with this kitta number   XX\n")
                        except:
                                print("\n\t\t\tXX   Dear "+customer_name+", please provide a genuine kitta number   XX\n")
                                continue

                '''next loop continues until valid anna number is entered'''
                next_loop=True
                while next_loop:
                        '''exceptional handling for ValueError'''
                        try:
                                anna_num=int(input("\n\t\tKindly include the number of anna of the land you want to rent ~ "))
                                if kitta_number in dictionary:
                                        if dictionary[kitta_number][2]==" "+str(anna_num):
                                                break
                                        else:
                                                print("\n\t\t\txx Dear "+customer_name+", kitta number "+str(kitta_number)+" has "+str(dictionary[kitta_number][2])+" "+"anna of land"+"xx\n")
                                                continue
                        except:
                                print("\n\t\t\tXX      Dear "+customer_name+", the quantity of anna you are looking for is not available       XX\n")
                                continue

                '''continued loop continues until valid duration for rent is entered'''
                continued_loop=True
                while continued_loop:
                        try:
                                duration_rent_return=int(input("\n\t\tKindly specify how long the land was rented~ "))
                                if duration_rent_return<=0:             #input negative value continues the loop
                                       
                                       print("\n\t\t\tXX        Dear "+customer_name+", the duration you are looking for is not available       XX\n")
                                       continue
                                else:
                                        break
                        except:
                                print("\n\t\t\tXX      Dear "+customer_name+", please provide a valid month       XX\n")
                                continue

                
                '''again loop continues until valid duration for return is entered'''
                again_loop=True
                while again_loop:
                        '''exceptional handling for ValueError'''
                        try:
                                duration_return_return=int(input("\n\t\tKindly specify when the land was returned~ "))
                                if duration_return_return<=0:           #input negative value continues the loop
                                        print("\n\t\t\tXX        Dear "+customer_name+", the duration you are looking for is not available       XX\n")
                                        continue
                                else:
                                        break
                        except:
                                print("\n\t\t\tXX      Dear "+customer_name+", please provide a valid month       XX\n")
                                continue

                '''all the valid input values of asked details is assigned each to a new variable'''
                kitta_number_bill=kitta_number
                return_land=dictionary[kitta_number][0]
                return_land_direction=dictionary[kitta_number][1]
                anna_return=anna_num
                rent_month=duration_rent_return
                return_month=duration_return_return
                per_month_price=int(dictionary[kitta_number][3])

                '''conditions to apply fine'''
                if rent_month<return_month:
                        difference_duration= return_month-rent_month
                        total_return_price=return_month*per_month_price
                        fine_pay+=10/100*(difference_duration*per_month_price)
                        grandtotal+=total_return_price
                else:
                        total_return_price=rent_month*per_month_price
                        grandtotal+=total_return_price

                '''second_last loop repeats until any one from two options is entered'''
                second_last_loop=True
                while second_last_loop:
                        more_return=input("\n\t\tDear "+customer_name+", Do you want to return more lands? ~ ").lower()
                        if more_return=="yes":
                                entire_loop=True
                                break
                        elif more_return=="no":
                                entire_loop=False
                                break
                        else:
                                print("\n\t\t\tXX      Dear "+customer_name+", please enter either yes or no       XX\n")
                                entire_loop=False
                                continue

                date_returned=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)
                time_returned=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second)

                customer_return_info.append([kitta_number_bill,return_land,return_land_direction,anna_return,rent_month,per_month_price,total_return_price])



        '''last loop repeats until any one from two options is entered'''
        last_loop=True
        while last_loop:
                confirmation_answer=input("\n\t\tDear "+customer_name+", Are you sure you want to return the lands? ~ ").lower()
                if confirmation_answer=="yes":
                        print("\n\t\tPROCEEDING BILL....\n")
                        break
                        
                elif confirmation_answer=="no":
                        import main
                        main.home_page()                #calling the home_page() function from main module
                        main.operation_page()           #calling the operation_page()function from main module
                         

                else:
                        print("\n\t\t\tXX      Dear "+customer_name+", please enter either yes or no       XX\n")
                        continue

        fine_grandtotal=grandtotal+fine_pay     #adding the grandtotal after fine
                
        return customer_name,customer_phonenumber,date_returned,time_returned,customer_return_info,grandtotal,fine_pay,fine_grandtotal

'''A function for option 4 which displays extra details of the company'''
def about_us():

        """
        display all the extra but needed details about the company

        takes input value as only two options yes or no to further display the Question and answer section, and the payment details
        if value is invalid an error message is displayed

        returns:
        A Thank you message is returned as a value
        
        """
        print("_"*153)
        print("\n\n\t\t\tTECHNO PROPERTY COMPANY\t\t\t\t\t\t\t\t")
        print("\t\t\t"," ","324 Himalaya Road",  "\t\t\t\t\t\t\t\t")
        print("\t\t\t"," ","","Kathmandu,Nepal\t\t\t\t\t\t\t\t")
        print("\t\t\t","","Phone no: 9823733085\t\t\t\t\t\t\t\t")
        print("\n\n\t\t\t<<<ABOUT US>>>\t\t\t\n")
        print("-"*153,"\n")
        print("\t\t\t\t\t\t\t\t\tOUR GOAL\n")
        print("\t\tTechno Property company is a newly established company which manages different lands based on different cities.\n\t\t\tThe major cities include Kathmandu, Pokhara, Lalitpur, Chitwan, itahari and many more.")
        print("\tThe goal of Techno Property Company is to provide all citizen with proper shelter and to maintain the land management system in nepal.\n")
        print("-"*153,"\n")

        '''first loop repeats until any one from two options is entered'''
        first_loop=True
        while first_loop:
                print("\n")
                inquery_info=input("\n\t\tDear customer, would you like to explore the Q&A section of our company? ~ ").lower()
                if inquery_info=="yes":
                        print("\n\n\t\t\t\t\t\t\t\tFREQUENTLY ASKED QUESTIONS\n")
                        print("\t\t * CAN WE RENT MORE THAN ONE LAND?\n")
                        print("\t\t>> Yes, customers can rent more than one land or infact as many as you like. \n\t\tHowever, customers cannot rent the land which are not present on the displayed available lands\n\n")
                        print("\t\t * CAN WE RETURN MORE THAN ONE LAND?\n")
                        print("\t\t>> Yes, customers can return more than one land or infact as many as you like. \n\t\tHowever, customers cannot return the land which are not present on the displayed unavailable lands\n\n")
                        print("\t\t * CAN WE RENT HALF ANNA OF LAND?\n")
                        print("\t\t>> No, customers are not allowed to take half anna of land but consider anna as a whole.\n\n")
                        print("\t\t * CAN WE RETURN HALF ANNA OF LAND?\n")
                        print("\t\t>> No, customers are not allowed to take half anna of land but consider anna as a whole.\n\n")
                        print("\t\t * WHAT WILL HAPPEN IF WE RETURN THE RENTED LAND LATE?\n")
                        print("\t\t>> If customers happen to exceed the time they rented the land for, an additional fine will be added to the final sum.\n\n\n\n")
                        print("-"*153,"\n\n")
                        break
                elif inquery_info=="no":
                        break
                else:
                        print("\n\t\t\tXX        Dear customer, please enter either yes or no        XX\n")

        '''second loop repeats until any one from two options is entered'''
        second_loop=True
        while second_loop:
                print("\n")
                bank_details_info=input("\n\t\tDear customer, would you like to know the payment details? ~ ").lower()
                if bank_details_info=="yes":
                        print("\n\n\t\t\t\t\t\t\t\t\tBANK DETAILS\n\n")
                        print("\t\t\tPAYMENT TO:\n")
                        print("\t\t\tBank name ~    NEPAL BIKASH BANK\n")
                        print("\t\t\tBranch name ~    KAMALPOKHARI\n")
                        print("\t\t\tAccount number ~    829383858392\n\n\n")
                        print("-"*153,"\n")
                        print("\t\t\t\t\t\t\t\t\tONLINE PAYMENT\n\n")
                        print("\t\t\tPAYMENT TO:\n")
                        print("\t\t\tEsewa id ~    +977 9818085827\n")
                        print("\t\t\tAccount Holder Name ~    BIKRAM SHRESTHA\n")
                        print("_"*153,"\n\n")
                        break
                elif bank_details_info=="no":
                        break
                else:
                        print("\n\t\t\tXX      Dear customer, please enter either yes or no       XX\n\n")
        
        return "\n\n\t\t\tWE APPRECIATE YOUR VISIT ! :)\n\n"  #returning a simple message



        
        

       



                        


            


            
   


    

    

        
        
    



    






