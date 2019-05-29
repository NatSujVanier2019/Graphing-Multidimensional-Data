skip=True                                   #Set the boolean variable skip equal to true.
data=[]                                     #Set data to an empty list
dat2=[]                                     #Set dat2 to an empty list
import csv                                                                         #Importing important modules
from random import uniform, randint                                                #uniform is a random float generator. Randint is a random integer generator.
#------------------------------Getting Data Values and Indexing It---------------------------------------------------------------------------------------------------------------------
user_file_name=input("Please enter the filename: ")  
with open (user_file_name) as txtfile:                                              #Assigning a variable to the file name    
    readtxtfile = csv.reader(txtfile, delimiter = ',')                              #Opeing the file and simplifing its name to txtfile
                                                                                    #Changing file to read type
    for line in readtxtfile:                                                        #For loop to read each line in the file
        if skip == False:                                                           #Checking if skip variable meets boolean condition
           for j in range (len(line)):                                              #For loop to go through each value in a row of the file
               try:                                                                 #Try condition to check if the code below can run
                   data.append(float(line[j]))                                      #Converts value of index to float and adds it to list(data)
               except ValueError:                                                   #If 'try' command fails, it passes through the except(Pass for now. We'll add code later)
                    pass
           
           dat2.append(data)                                                    #Adds the values inside the list data into the list dataperson 
           data=[]                                                              #Neutrilizing data list and emptying it
        skip = False                                                            #Setting skip to boolean type False to fulfill skipping the first line
##number = len(dat2[0])
##for num in range (0,number):
##    dat = []
##    for person in dat2:
##        dat.append(person[num])
##    dataperson.append(dat)
###print (dat2)
#--------------------K-Means Begins------------------------------------------------------------------------------------------------------------------------------
#dat2 = dataperson

ilen_dat2 = len(dat2)                                               #dat2 is a list of rows from the original dataset. Thus when we ge the lenght of dat2(current line)
                                                                    #we get the total number of rows there are.

ilen_row = len(dat2[0])                                             #Getting the lenght of a row to see how many indexs (columns) there are.
print ('Lenght: %i' %(ilen_dat2))                                   #Printing the lenght for confirmation

centroid_list = []                                                  #make an empty list that will store all the centroid coordinates. Each centroid will have a list of
                                                                    #coordinates for each dimension.

centroid_point_assignment = []                                      #make an empty list that will store what points are assigned to what centroid. This will change each iteration.
taken = []                                                          #Make an empty list that will store what rows have been taken so to say. This is a list to check
                                                                    #which datapoints have already been chosen as the starting centroid.

Cluster_2 = []                                                      #Making an empty list that will contain all the original data seperated by columns, not rows.
                                                                    #Columns are required to make the graphs.

Cluster = []                                                        #This will be a list of clusters. Inside each cluster will be a list of rows assigned to it.
pl_colorscale = []                                                  #This is a list that will float values between (0,1) and what color they represent(aka the color of the cluster.

color_list = []                                                     #This is a list that will store float values in range (0,1) for each row in the dataset. Each value
                                                                    #corresponds to a certain color in pl_colorscale. This color will be used to identify clusters when
                                                                    #graphed.

color_list2 = []                                                    #This is a second list that will contain colors for each cluster. This is more specifically for
                                                                    #scatterplots.
k = 2                                                               #This variable determines the number of centroid we will use. It will be a constant.
#-----------Assign K Centroid Coordinates-------------------------------------------------------------------------------------------------------------------------
for a in range (0,ilen_row+1):                                          
    Cluster_2.append([])                                                    #Append as many empty lists as there are columns into Cluster_2. Add one more list(column)
                                                                            #for color
    
for c in range (0,k):                                                       #Run a for loop for one to the # of centroids (k)                                   
    centroid_point_assignment.append([])                                    #Append an empty list in centroid_point_assignment. Each empty list will contain row numbers
                                                                            #(data points) depending on which centroid it is assigned to. Hence the name centroid_point_assignment.
    icheck = False                                                          #Make icheck equal to false. This will be a check for picking starting positions for the centroids.
    while icheck == False:                                                  
        num = randint(0,(ilen_dat2 - 1))                                    #Get a random integer between 0 and the lenght of dat2. This value will be the datapoint we pick
                                                                            #from dat2.
        if (num in taken) == False:                                         #We check to see if this point has already been picked.
            copy = list(dat2[num])
            centroid_list.append(copy)                                 #If it hasn't been picked already, we append that point into the centroid list.
            centroid_point_assignment[c].append(num)                        #Add this point to the current cluster.
            taken.append(num)                                               #Add this point to the list taken to know it's been picked
            icheck = True                                                   #Set icheckt to True, move on to the next centroid.
            
    Cluster.append([])                                                      #Append k number of empty lists into Cluster. These lists will also store columns. However
                                                                            #unlike Cluster_2, each list is for an individual cluster.
#----------------End Assignment-----------------------------------------------------------------------------------------------------------------------------------
print ("Centroids: ")
for icounter in range (0,k):
    print (centroid_list[icounter])
print ("")
move = True                                                             #Set move to True to run the while loop. Move represents that if a centroid has move since
                                                                        #it's last assignment. If it has, then continue finding the center, else, that centroid has
                                                                        #found it's cluster and center thus, end centroid reassignment loop.
#print ("\n Loading...\n")
#-----------------Start the K-Means Assignment and Reassignment---------------------------------------
while move == True:
    movelist = []                                                   #Make movelist an empty list. This list will contain 1s and 0s. 0 represents a centroid has moved.
                                                                    #1 represents no centroid has not moved (coordinates did not change). If all the values in movelist
                                                                    #are 1s, then that means that all the centroids have found their cluster centers and thus, we end
                                                                    #this loop. Else we reset it every iteration.
    
    for x in range (0,ilen_dat2):                                   #Run a for loop that will go through every datapoint in the dataset. With this, we will calculate
                                                                    #the euclidean distance between each point and each centroid.
        min_dist = 0                                                #Reset mininum distance (min_dist) to 0. min_dist stores the minimum distance between a point and
                                                                    #a centroid. The smallest distance means the closest centroid.
        
        for z in range (0,k):                                       #Run a loop for to check each centroid.
            dist = 0                                                #Set dist(distance) as 0.
            #Euclidean Distance Formula: Underneath we calculate the euclidean distance of each point for each centroid.
            for y in range (0,ilen_row):                            
                dist += (dat2[x][y] - centroid_list[z][y]) ** 2       #Going through each coordinate. Substracting the coordinate of the datapoint from the centroid coordinate.
                                                                      #Square it.
            if z == 0:      
                min_dist = (dist ** 0.5)                            #If this is the first centroid(first check), the square root of dist is the min_dist. We are setting
                                                                    #this distance as the minimum distance. We need something to compare to in the future.
                z_tracker = z                                       #We use z_tracker to know which centroid does this point have the shortest distance with.
            else:
                if min_dist > (dist ** 0.5):                        #If this is not the first check(first centroid). We check to see if the previous min_dist is greater
                                                                    #than the current min_dist.
                    min_dist = (dist ** 0.5)                        #If it is, this distance is the new min_dist(minimum distance).
                    z_tracker = z                                   #Track which centroid has the shortest distance with this data point(closest centroid).
        centroid_point_assignment[z_tracker].append(x)              #Assign this point to the centroid that is closest to it.
           
    for d in range (0,k):                                           #Run a loop to go through every centroid.
        #print ("CENT: ", centroid)
        for e in range (0,ilen_row):                                #Make a loop go through every column
            mean = 0                                                #Set the mean value to be 0
            for f in range (0,ilen_dat2):                           #Make a loop that go through every row/datapoint
                
                if (f in centroid_point_assignment[d]) == True:     #Check to see if the current datapoint is assigned to the current centroid we are checking.
                    mean += dat2[f][e]                              #Add the current coordinate/column from the current datapoint to the mean for the current coordinate.
            mean = mean /(len(centroid_point_assignment[d]))        #Calculate the mean average.
            if mean != centroid_list[d][e]:                                 #If the current mean is not equal to the current centroid coordinate
                centroid_list[d][e] = mean                                  #Assign this new mean value as the new coordinate for the centroid.
                #print (centroid [e])
                movelist.append(0)                                  #Append 0 into movelist(has moved)
            else:   
                movelist.append(1)                                  #If the current mean is equal to the coordinate, append 1 into movelist(hasn't moved)
                
    if (0 in movelist) == True:                                     #If there are any 0s in movelist
        for h in range (0,k):                                       #Empty every centroid_point_assignment list. We are starting over until we find our center.
            centroid_point_assignment[h] = []
        move = True                                         
    else:
        move = False                                                #If there are no 0s(nothing has moved since last iteration), set move to False (end the loop).
        
#print ("Points Assigned:")
for icounter in range (0,k):                                        #Run a loop for every centroid (again)
    #Underneath I decided to make a string that contains rgba values based on plotly syntax for graphing. We start with the string and run a loop.
    #I basically run a for loop and concatonate values into the strings. Random values for r,g and b.
    color_string = "rgba("
    for w in range (0,4):
        if w != 3:
            color_string +=((str(randint(0,255)) + ","))
        else:
            color_string+=("1)")                                                                                       
    color_list2.append(color_string)                #Append that string into color_list2(for scatterplots)

    #In plotly to use colorscaling(assign colors to each individual point), each point needs to have a value related to it that is between 0 and 1. The first value has
    #to be 0, the last has to be 1. Every other value has to be a float value in between the two.
    icheck = False                                  #Here we run another check to select color values.
    while icheck == False:                          
        if icounter == 0:                           #If this is the first centroid(first cluster), it will receive color value of 0
            colr_val = 0
        elif icounter == 1:                         #If its the second centroid(second cluster), it will receive a color value of 1
            colr_val = 1
        else:                                   
            colr_val = uniform(0,1)                 #If it's neither the first or the second centroid, make a random float value between (0,1).
            
        if (colr_val in pl_colorscale) == False:    #If the current color value hasn't been selected already....
            for p in range (0,len(centroid_point_assignment[icounter])):                #Run a loop that goes through every value in the current centroid_point_assignment list
                
                dat2[(centroid_point_assignment[icounter][p])].append(colr_val)  #Append the color value at the end of the row. This will be done for every value in
                                                                                 #that list.
                icheck = True                                                   #Set icheck to true, end loop
            pl_colorscale.append([colr_val,color_string])                   #Append the color value and then the colorstring to pl_colorscale. pl_colorscale stores
                                                                            #a color value and what color that value represents in a list of lists. Done according to
                                                                            #plotly syntax.
    #Underneath, I start to turn all the rows I have been working with so far into columns for graphing purposes.
    for n in range (0,ilen_row+1):                                  #Run a for loop going through every column.        
        column = []                                                 #Make an empty list called column
        for v in range (0,ilen_dat2):                                       #Run a loop that goes through every row
            if (v in centroid_point_assignment[icounter]) == True:          #if the current row is in the current cluster, append the value in the current column into
                                                                            #the column list.
                column.append(dat2[v][n])
        Cluster[icounter].append(column)                                    #Add this column into Cluster.
        Cluster_2[n].extend(column)                                         #Add this column into Cluster_2. The extend function instead of just adding another element,
                                                                            #combines two lists, which is what we are doing to make one big list of columns.
    #print (centroid_point_assignment[icounter])
color_list = Cluster_2[len(Cluster_2) - 1]                      #Assign the last column to color_list
Cluster_2.pop()                                                 #Destroy the last column so we only have to original values.
#Print stuff for output.
print (pl_colorscale)
print ("Centroids")
for icounter in range (0,k):
    print (centroid_list[icounter])
    print (centroid_point_assignment[icounter])
print ("")

print (Cluster[0])
print (Cluster[1])
print ("")
print (Cluster_2)
