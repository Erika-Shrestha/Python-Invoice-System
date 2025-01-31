import datetime
from random import randint
import operation
import read

'''This is a function to generate each unique rent bills'''
def gen_rent_invoice():

    """
    writes a new unique rent bill for each customers in new text file

    takes customer name, phone number, date and time rented, customer_rental_info,
    and grandtotal returned in rent_kitta() function
    each new bill generates with the customer name and phone number
    the bill includes land rented, and grand total

    A thank you message is returned as a value
    
    """

    '''a structure design of the bill'''
    customer_name,customer_phonenumber,date_rented,time_rented,customer_rental_info,grandtotal=operation.rent_kitta()
    file_name = str(customer_name)+str(customer_phonenumber) + "rentinvoice.txt"            #name and phone number stored in a variable
    with open("C:\\Users\\eerii\\OneDrive\\Desktop\\23048598ErikaShrestha\\23048598ERIKASHRESTHA\\" + file_name,"w") as customer_details:    #a new text file is opened in a write mode
        customer_details.write("\n")
        customer_details.write("\t\t\t"+"_"*105+"\n\n")
        customer_details.write("\t\t\t\tTeachno property Company\t\t\t\t\t\tINVOICE")
        customer_details.write("\n\t\t\t\t324 Himalaya Road")
        customer_details.write("\n\t\t\t\tKathmandu, Nepal")
        customer_details.write("\n\t\t\t\tContact: 9823733085\n\n\n")
        customer_details.write("\t\t\t\tInvoice :"+str(randint(5,40))+"-"+str(randint(41,65))+"-"+str(randint(65,90))+"-"+str(randint(5,40))+"\t\t\t\t\t\t\tDate :"+str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day))
        customer_details.write("\n\t\t\t\t\t\t\t\t\t\t\t\t\t"+"Time :"+" "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second)+"\n\n")
        customer_details.write("\t\t\t\tName of the customer :"+"   "+str(customer_name)+"\n")
        customer_details.write("\t\t\t\tContact no:"+"   "+str(customer_phonenumber)+"\n")
        customer_details.write("\t\t\t\tDate of purchase:"+"   "+str(date_rented)+"\n")
        customer_details.write("\t\t\t\tTime of purchase:"+"   "+str(time_rented)+"\n")
        customer_details.write("\t\t\t"+"_"*105+"\n\n\n")
        customer_details.write("\t\t\t"+" "+"LandID"+"\t\tCITY\t"+"     "+"DIRECTION\t"+"     "+"QUANTITY\t"+"    "+"DURATION\t"+"     "+"PRICE\t"+"    "+"TOTAL AMOUNT\n")
        customer_details.write("\t\t\t"+"-"*105+"\n\n")

        '''the index of customer_rental_info is assigned to new variables'''
        for details in customer_rental_info:
            number=details[0]
            city=details[1]
            direction=details[2]
            anna=details[3]
            duration=details[4]
            rupee=details[5]
            total=details[6]

            customer_details.write("\t\t\t"+"  "+str(number)+"\t"+"      "+str(city)+"\t"+"       "+str(direction)+"\t\t"+str(anna)+"\t\t"+str(duration)+"\t"+"     "+str(rupee)+"\t\t"+str(total)+"\n\n")
        
        customer_details.write("\t\t\t"+"-"*105+"\n")
        customer_details.write("\n\t\t\t\t\t\t\t\t\t"+"Your discount amount: "+"\t\t\t\t0"+"\n\n\t\t\t"+"-"*105+"\n\n\t\t\t\t\t\t\t\t\tYour 0.0% discounted amount is: "+"\t\t0.0"+"\n\n\t\t\t"+"-"*105+"\n\n\t\t\t\t\t\t\t\t\tYour payable amount is: "+"\t\t\t"+str(grandtotal)+"\n\n\t\t\t"+"-"*105+"\n\n")
        customer_details.write("\t\t\t\t\t\t\t"+"    "+"THANK YOU NAME FOR RENTING WITH US.")
        customer_details.write("\n\t\t\t\t\t\t\t\t"+"      "+"SEE YOU AGAIN !\n\n")
        customer_details.write("\t\t\t"+"_"*105)
        customer_details.write("\n\n\t\t\t\t\tPayment information:\n\n\t\t\t\t\tOnly cash, bank transfer\n\t\t\t\t\tand esewa payment are accepted\n")
        customer_details.write("\n\t\t\t\t\t**for more details go to about us page**\n\n\n")
        customer_details.write("\t\t\t"+"_"*105)

    '''the land.txt file is being overwritten'''
    dict_store=read.read_file()
    with open("land.txt","w")as change:
        for key,values in dict_store.items():
                for user_kitta in customer_rental_info:
                    if user_kitta[0]==key:
                        dict_store[key][4]=" NOT AVAILABLE"     #the status of value's fourth index is changed
                        
                change.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(dict_store[key][4])+"\n")

    return "\n\t\tTHANK YOU FOR YOUR COOPERATION ! :)"
        
                    
'''This is a function to generate each unique return bills'''
def gen_return_invoice():

    """
    writes a new unique return bill for each customers in new text file

    takes customer name, phone number, date and time rented, customer_return_info,
    and grandtotal returned in rent_kitta() function
    each new bill generates with the customer name and phone number
    the bill includes land returned, and grand total with fine or without fine

    A thank you message is returned as a value
    
    """
        
    '''a structure design of the bill'''
    customer_name,customer_phonenumber,date_returned,time_returned,customer_return_info,grandtotal,fine_pay,fine_grandtotal=operation.return_details()
    file_name = str(customer_name)+str(customer_phonenumber) + "returninvoice.txt"        #name and phone number stored in a variable
    with open("C:\\Users\\eerii\\OneDrive\\Desktop\\23048598ErikaShrestha\\23048598ERIKASHRESTHA\\"  + file_name,"w") as customer_details:        #a new text file is opened in a write mode
        customer_details.write("\n")
        customer_details.write("\t\t\t"+"_"*105+"\n\n")
        customer_details.write("\t\t\t\tTeachno property Company\t\t\t\t\t\tINVOICE")
        customer_details.write("\n\t\t\t\t324 Himalaya Road")
        customer_details.write("\n\t\t\t\tKathmandu, Nepal")
        customer_details.write("\n\t\t\t\tContact: 9823733085\n\n\n")
        customer_details.write("\t\t\t\tInvoice :"+str(randint(5,40))+"-"+str(randint(41,65))+"-"+str(randint(65,90))+"-"+str(randint(5,40))+"\t\t\t\t\t\t\tDate :"+str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day))
        customer_details.write("\n\t\t\t\t\t\t\t\t\t\t\t\t\tTime :"+" "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second)+"\n\n")
        customer_details.write("\t\t\t\tName of the customer :"+"\t"+str(customer_name)+"\n")
        customer_details.write("\t\t\t\tContact no:"+"   "+str(customer_phonenumber)+"\n")
        customer_details.write("\t\t\t\tDate of return:"+"   "+str(date_returned)+"\n")
        customer_details.write("\t\t\t\tTime of return:"+"   "+str(time_returned)+"\n")
        customer_details.write("\t\t\t"+"_"*105+"\n\n\n")
        customer_details.write("\t\t\t"+" "+"LandID"+"\t\tCITY\t"+"     "+"DIRECTION\t"+"     "+"QUANTITY\t"+"    "+"DURATION\t"+"     "+"PRICE\t"+"    "+"TOTAL AMOUNT\n")
        customer_details.write("\t\t\t"+"-"*105+"\n\n")

        '''the index of customer_return_info is assigned to new variables'''
        for details in customer_return_info:
            number=details[0]
            city=details[1]
            direction=details[2]
            anna=details[3]
            duration=details[4]
            rupee=details[5]
            total=details[6]

            customer_details.write("\t\t\t  "+str(number)+"\t"+"       "+str(city)+"\t"+str(direction)+"\t\t"+str(anna)+"\t\t"+str(duration)+"\t"+"     "+str(rupee)+"\t\t"+str(total)+"\n\n\n")

        customer_details.write("\t\t\t"+"-"*105+"\n\n")
        customer_details.write("\t\t\t\t\t\t\t\t\t"+"Your discount amount: "+"\t\t\t\t0"+"\n\n\t\t\t"+"-"*105+"\n\n\t\t\t\t\t\t\t\t\tYour 0.0% discounted amount is: "+"\t\t0.0"+"\n\n\t\t\t"+"-"*105+"\n\n\t\t\t\t\t\t\t\t\tYour fine is: "+"\t\t\t\tRS.      "+str(fine_pay)+"\n\n\t\t\t"+"-"*105+"\n\n\t\t\t\t\t\t\t\t\tYour payable amount is: "+"\t\tRS.      "+str(grandtotal)+"\n\n\t\t\t"+"-"*105+"\n\n\t\t\t\t\t\t\t\t\tYour payable amount after fine is: "+"\tRS.      "+str(fine_grandtotal)+"\n\n\t\t\t"+"-"*105+"\n\n")
        customer_details.write("\t\t\t\t\t\t\t"+"    "+"THANK YOU NAME FOR CHOOSING US.")
        customer_details.write("\n\t\t\t\t\t\t\t\t"+"      "+"SHOP AGAIN !\n\n")
        customer_details.write("\t\t\t"+"_"*105)
        customer_details.write("\n\n\t\t\t\t\tPayment information:\n\n\t\t\t\t\tOnly cash, bank transfer\n\t\t\t\t\tand esewa payment are accepted\n")
        customer_details.write("\n\t\t\t\t\t**for more details go to about us page**\n\n\n")
        customer_details.write("\t\t\t"+"_"*105)

    '''the land.txt file is being overwritten'''
    dict_store=read.read_file()
    with open("land.txt","w")as change:
        for key,values in dict_store.items():
                for user_kitta in customer_return_info:
                    if user_kitta[0]==key:
                        dict_store[key][4]=" AVAILABLE"         #the status of value's fourth index is changed
                        
                change.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(dict_store[key][4])+"\n")

    return "\n\t\tTHANK YOU FOR YOUR COOPERATION ! :)"
