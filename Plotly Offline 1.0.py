#--------------Importing Modules-------------------------------
import plotly
import plotly.graph_objs as graph
import csv
#-----------Functions----------------------------------------------------
"""
make_dimension is a function that allows us to make an infinite number of dimensions based on the current dataset being graphed, be it the original or the edited version.
make_dimensions takes a column in a dataset and sorts it to get the maximum and minimum value. It then makes a directory for that column. This directory contains the
range of the data, it's label and the values that will be graphed. It then appends that directory into a pre-made list named axis. The range, label and values are all
required so that we can graph this column in our parallel coordinates graph.
"""
def make_dimension(ilen,dat2,axis):                                                 #Creating the function make_dimensions with the parameters ilen, dat2 and axis.
    for x in range (0,ilen):                                                        #Running a for loop that will go through every index value of the list dat2.
                                                                                    #dat2 is a list that contains all the columns and values from the original data list.
                                                                                    #It is basically a list of lists.
        
        icolumn = dat2[x]                                                           #Making a temporary list, icolumn to store the current list in dat2.
        ilen2 = len(icolumn)                                                        #Getting the lenght of icolumn and storing it in the variable ilen2. The i is a prefix
                                                                                    #that indicates the variable type is an integer and the len signifies that it is a
                                                                                    #lenght of a list, in this case, the lenght of icolumn.
                                                                            
        for y in range (0,ilen2):                                                   #Running a for loop that goes through every value in icolumn
            isort = list.sort(icolumn)                                              #Sorting list icolumn and storing it in isort.
            imin = icolumn[0]                                                       #Get the minimum value from the sorted icolumn
            imax = icolumn[(ilen2 - 1)]                                             #Get the maximum value from the sorted icolumn
        axis.append(                                                                #Append into the list axis
            dict(                                                                   #Create a directory
                range = [imin,imax],                                                #Set the range of the dimension using the minimum and maximum value.
                label = chr(65 + x),                                                #Setting a label on the dimension based on it's place(index value) in dat2.
                values = dat2[x]                                                    #Setting which values to plot on this dimension/axis.
                )                                                                   #Ending the directory
        )                                                                           #Ending the append bracket.
                                                                                    #End of function.
#--------------Getting Data Values and Indexing It------------------------
skip=True                                                                           #Set the boolean variable skip equal to true.
data=[]                                                                             #Set data to an empty list
dat2=[]                                                                             #Set dat2 to an empty list
dataperson=[]                                                                       #Set dataperson to an empty list
user_file_name='heart.csv'# input('Please enter file name\n')                       #Assigning a variable to the file name
with open (user_file_name) as txtfile:                                              #Opeing the file and simplifing its name to txtfile
    readtxtfile = csv.reader(txtfile, delimiter = ',')                              #Changing file to read type
    for line in readtxtfile:                                                        #For loop to read each line in the file
        if skip == False:                                                           #Checking if skip variable meets boolean condition
           for j in range (len(line)):                                              #For loop to go through each value in a row of the file
               try:                                                                 #Try condition to check if the code below can run
                   data.append(float(line[j]))                                      #Converts value of index to float and adds it to list(data)
               except ValueError:                                                   #If 'try' command fails, it passes through the except(Pass for now. We'll add code later)
                    pass                                                            #
           
           dataperson.append(data)                                                  #Adds the values inside the list data into the list dataperson 
           data=[]                                                                  #Neutrilizing data list and emptying it
        skip = False                                                                #Setting skip to boolean type False to fulfill skipping the first line
        
number = len(dataperson[0])                                                         #Setting a variable to the length of the list of rows in the file
for num in range (0,number):                                                        #For loop to index each list in the big list
    dat = []                                                                        #assigning dat to and empty list and also neutrilizing it after it reaches the top of the for loop again
    for person in dataperson:                                                       #For loop to go through eachlist in the big list
        dat.append(person[num])                                                     #adding the values of the same index in each list to dat
    dat2.append(dat)                                                                #addind the values in dat to dat2
#----------------Setting the parameters for the dimensions and plotting-----------
ilen = len(dat2)                                                                    #Get the lenght of the list dat2
axis = list([])                                                                     #Make an empty list for all the axis/dimensions to go into.
make_dimension(ilen,dat2,axis)                                                      #Run the make_dimension function
#------------Plotting time--------------------------------------------------------

#This is where we graph all the data we got from the dataset. For plotly to graph, you require 3 parameters. First is the data a.k.a the actual graph, a file name and
#a boolean value that determines to automatically open the figure or not. Plotly offline mode stores the graph as a local HTML file and opens it on your web browser.

data = [                                                                            #Making a list named data for the actual graph
            graph.Parcoords(                                                        #Running the function graph.Parcoords to make a graph. According to plotly syntax,
                                                                                    #You require a directory for the line and a list of directories to graph the actual
                                                                                    #dimensions/axis for the parallel coordinates graph.
                line = dict(color = "blue"), #setting the color range
                dimensions = axis
            )                                                                       #Ending the function
        ]                                                                           #Ending the list

plotly.offline.plot(data, filename = 'Parallel Coordinates Test',auto_open = True)  #Running the plotly graphing function that saves the file as a local HTML file.
                                                                                    #The auto_open boolean determines that we want to automatically open the html graph
