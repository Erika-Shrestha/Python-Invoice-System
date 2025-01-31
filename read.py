'''This is a read module'''
def read_file(kitta_Number=101):
    """
    The sturcture of data from text file is formatted
    
    The data is read from the land.txt file
    Then stored in dictionary dic_store where
    values is stored in list.

    parameters:
    A parameter kitta_number is initialized as 101
    which increase by 1 with each iteration

    returns:
    The dictionary dict_store is returned

    """
    with open("land.txt","r") as file:  # The land.txt file is opened in read mode
        dict_store={}
        for value in file:
            value=value.replace("\n","")    #\n is replaced by empty
            dict_store[kitta_Number]=value.split(",")        #the string is changed into list where each index is separated by ','
            value=value.replace(" ","") #again the whitespace is replaced by empty
            kitta_Number+=1
        return dict_store


