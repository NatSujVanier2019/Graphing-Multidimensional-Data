#-----------------------------------------------------------------------Inexing_Rev_3.0-----------------------------------------------------------------------#
'''
This program Indexing_Rev_3.1 to sum everything up, is basically a data organizer. Inputs a file and organizes it for graphing and clustering. File checks
for strings becasue these values won't be able to be graphed or clustered which then we start catagorizing. Catagorizing assigns float values to strings
without changing their index values and duplicated strings will have the same value. 
'''
#---------------------------------------------------------------------------Input-----------------------------------------------------------------------------#

def fileinput ():
    fileinput = True
    while fileinput == True:
        try:
            import csv
            skip=True                                                                                               #Skip variable help skip the first line a file which is usually the header.
            file_lst=[]                                                                                             #A temporary list of the file 
            dat2 = []                                                                                               #A list of columns in the file
            Data = []                                                                                               #A list of rows in the files
            dataperson=[]                                                                                           #A temporary list for converting rows to columns
            lst_of_dct = []                                                                                         #A dictionary list
            counter=0.0                                                                                             #Counter to replace values of strings
            heading = []                                                                                            #A list of the first line which is usually the heading of the data set
            user_file_name= input("Please Enter you csv data file name Ex:DataFile.csv/Datafile.txt\n")             #Prompts the user for the file name
            with open (user_file_name) as csvfile:
                readcsvfile = csv.reader(csvfile, delimiter = ',')                                                  #Opens the file in read format
                for line in readcsvfile:                                                                            #Loops through the whole file
                    if skip == False:                                                                               #Checks if the first line has been skipped yet
                       for j in range (len(line)):                                                                  #Goes through each value in a line
                           try:                                                                                     #try:
                               file_lst.append(float(line[j]))                                                      #Checks if it can be converted into a float value
                           except ValueError:                                                                       #If it can't, it means it's a string
                                file_lst.append(line[j])                                                            #Therefore it append it into 'file_lst' as a string instead
                       dataperson.append(file_lst)                                                                  #Appends the line into 'dataperson'
                       file_lst=[]                                                                                  #Neutrilizes file_lst in order to be used again to check the next line
                    else:                                                                                           #If skip is actualy True. This means the first line hasn't been skipped yet
                        heading.append(line)                                                                        #Since skip is true, the line it's reading is the heading of the file which is appended into a seperate list called 'heading'
                        skip = False                                                                                #Since now the first line has been read it will now run through the rest of the file
            row_lst = dataperson
            number  = len(dataperson[0])                                                                            #Find the length of the first line assuming the other lines will be the same(only makes sense for them to be)    
            for num in range(0,number):                                                                             #For loop to get the index of each value 
                dat = []                                                                                            #A temporary list for the first value of each line/neutrlizes after finishing with one line
                for person in dataperson:                                                                           #For loop to through each list in 'dataperson'
                    dat.append(person[num])                                                                         #Append the first value in the line to 'dat' (This is basically creating columns instead of rows of the data file in order to help with catagorizing for strings)                            
                dat2.append(dat)                                                                                    #Append that value into new list 'dat2'    
            ilen = len(dat2)                                                                                        #Checks for the length of the new list 'dat2'
            #------------------------------------------------------------------------Catagorizing--------------------------------------------------------------------------#
            for column in range (0,ilen):                                                                           #Gets the index value fo each list in 'dat2'
                   float_flag = False                                                                               #flag inorder for the program to know if a certain performance has occured or not
                   itest = -1                                                                                       #Thie variable contributs into exiting a while loop further in the code
                   end = False                                                                                      #Variable to run the while loop  
                   ilen2 = len(dat2[column])                                                                        #Gathers a list in 'dat2' according to the index value the for loop has achieved
                   while end == False:                                                                              #While loop to go through each value in list that was achieved
                          itest += 1                                                                                #Counter to exit loop if none of the conditions below are met
                          if itest == (ilen2-1):                                                                    #Checks basically if has went through each value in the list
                              end = True                                                                            #If it has went through each value in the list then it will exit the loop
                          else:                                                                                     #Else: If it hasn't yet
                                for value in range(0,ilen2):                                                        #For loop that gets the index value for each list from the big list aka:'dat2'
                                    try:                                                                            #Try:
                                        fvalue = float(dat2[column][value])                                         #Checks if the value achieved can be converted into a float
                                        catbol = False
                                        end = True                                                                  #if it can, exits the while loop and assignes a boolean condition False to know that a dictionary does not need to be made                          
                                        if float_flag == False:                                                     #Checks if the below code hasnt been run yet
                                            lst_of_dct.append(["none"])                                             #If it hasnt, it appends 'none' to the list of dictionaries thats going to be created simultaneusly knowing that there is no need for a dictoinary for this list since its in in floats and that we need mactching indexes 
                                            float_flag = True                                                       #Then changes the boolean condition inorder for the program not to run that set of code again until it goes back to the first for loop 
                                    except ValueError:                                                              #Except valueerror just in case it cant be converted to a float, exits the while loop then sets a True boolean condition for the code that creates dictionaries to run
                                        catbol = True
                                        end = True
                   if catbol == True:                                                                               #If there was a string, this if statement would run
                          catagory = {}                                                                             #Creating a dictionary and neutrilizing after it's created
                          for value2 in dat2[column]:                                                               #Goes through each value in the lists of of the big list aka:'dat2'
                                 if value2 not in catagory:                                                         #Checks if the string is not already in the dictionary to pevent duplicates
                                        counter +=1.0                                                               #A counter to change the key for each value
                                        catagory[value2] = counter                                                  #Adds the value in dictionary with it's key
                          lst_of_dct.append(catagory)                                                               #Appends the dictionary to the list of dictionaries
            #-----------------------------------------------------------------------------Replace---------------------------------------------------------------------------#
            for num in range (0,len(dat2)):                                                                         #For loop to get the index value for each list in 'dat2'
                temp_lst = dat2[num]                                                                                #Assigns a temporary list to the lists of in 'dat2'
                if type(temp_lst[0]) != float:                                                                      #Checks if the value in the temporary list is not a float
                    if lst_of_dct[num] != ["none"]:                                                                 #If it is not, then checks if the dictionary value is not 'none' since it will need a dictionary
                        temp_dct = lst_of_dct[num]                                                                  #Another temporary variable for the dictionary that would match the list that we are going replace it's strings with floats 
                        for sml_lst in range (0,len(temp_lst)):                                                     #A for loop to get the index value for each value in the small list 
                            replace = temp_dct[temp_lst[sml_lst]]                                                   #Here we are reading the dictionary and replacing the strings with there rightful loat values
                            temp_lst[sml_lst] = replace
            for conv_row in range(0,len(dat2[0])):                                                                  #For loop to change the list of columns back to rows for future use in graphing and clustering
                dat_change = []
                for columnvalue in dat2:
                    dat_change.append(columnvalue[conv_row])
                Data.append(dat_change)
            heading[0][0] = heading[0][0][3:len(heading[0][0])]
            return heading,Data,lst_of_dct
            fileinput = False
        except FileNotFoundError:
            print("No such file")
       
##head,strings,dictionary = fileinput()
##print(head)
##print(strings)
##print(dictionary)



