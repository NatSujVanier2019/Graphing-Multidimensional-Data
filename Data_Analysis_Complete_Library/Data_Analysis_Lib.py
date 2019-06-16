from copy import deepcopy
from random import randint, uniform
from Ploty_Graph_Version_4 import Graph                                     #Importing the graphing function
from Indexing_Rev_31 import fileinput                           #Importing the file input function that allows the program to take in files and index them.
                
k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2 = None,None,None,None,None,None,None,None,None
#titles,dataperson,category_legend = fileinput()
def density_and_anomaly (dataperson,titles, iradius, plot, dim_option, dim_list):
    def clustering (dataperson):                                            #The whole code is in a function which will be used in the Columning_4_0.txt 
        Data = deepcopy(dataperson)
     

        """
            cluster is a function that uses two points (their coordinates) and a radius as parameters. It returns True if the two points are within the given
            radius of each other.
        """

        def cluster (iprime, inext, iradius):                               #This functions determines if 2 points (iprime and icheck) are within a radius (iradius).
            square_sum = 0                                                  #square_sum intialized to 0.
            for i in range (0, len(iprime)):                                #Loop runs for the number of coordinates in a data point (which is the same for each data point). 
                square_sum += ((float(iprime[i]))-(float(inext[i])))**2     #Uses the distance formula except the last step of square rooting.
            dist = square_sum**0.5                                          #Finds distance by square rooting square_sum.
            if dist <= iradius:                                             #If the distance is less than or equal to the radius....
                return True                                                 #....then returns True.

        Clusters = []                                                       #Creates a void list called Clusters
        Noise = [] 
        """
            density_cluster is a function that uses a data list, a radius and a void list (Clusters) as parameters. It iterates through the data list.
            It passes 2 points and the given radius as parameters for the cluster function to form density based clusters. These clusters are stored in the
            Clustsers list. 
        """

        def density_cluster(Data,iradius,Clusters):                        #This function classifies data points into clusters and noise points

            noise = False
            
            print ("Data: ",Data)
            print ("Data Points: ",len(Data))
            print ("Dimensions: ",len(Data[0]))
            print ("Radius: ",iradius)

            while (len(Data)>0):                                            #While Loop runs as long as the length of the list Data is more than 0.
                Clusters.append([Data[0]])                                  #Appends the first data point (element) in Data to Clusters.
                Data.remove(Data[0])                                        #Removes the first data point (element) in Data from Data.
                
                for icount in range (0,len(Data)):                          #For Loop runs for the number of data points in Data. 
                    icheck = Data[icount]                                   #icheck is always the icountth data point in Data.

                    for List in range (0, len(Clusters)):                   #For Loop runs for the number of lists (clusters) in Clusters.
                
                        for iprime in Clusters[List]:                       #For Loop runs for the number data points in the Listth list in Clusters.
                           
                            if cluster (iprime, icheck, iradius)==True:     #If iprime (data point in a list in Clusters) and icheck (data point in Data) are within iradius...
                                Clusters[List].append(icheck)               #...then appends that icheck in to the current list in Clusters.
                                Data[icount] = "Del"                        #Replaces the position of icheck in Data with the string "Del".
                                break                                       #breaks from the current loop
                                
                
                for icount in range (len(Data)-1,-1,-1):                    #For Loop runs in the descending order for the number of elements in Data.
                    if Data[icount]=="Del":                                 #If an element is "Del"...
                        Data.remove(Data[icount])                           #...that element is removed from Data.

                for C in Clusters:                                          #For Loop iterates the clusters in Clusters.
                    if len(C)==1:                                           #If a cluster only has one data point...
                        noise = True
                        Noise.append(C)                                     #...it is appended in a list called Noise...
                        Clusters.remove(C)                                  #...and is removed from Clusters.
                   

            All = list(Clusters)   
    ##        print (All[len(All)-1])

            if noise==True:
                All.append([])
                for c in Noise:
                    for n in c:
                        All[len(All)-1].append(n)

            print ()
            print ("Number of Clusters: ", len(Clusters))
            print ("Clusters: ", Clusters)
            print ()
            print ("Number of Anomalies: ", len(Noise))
            print ("Anomalies: ",Noise)                 
            print ()                
            print ("All: ",All)
            print ()
            return All, noise, Noise, Clusters
        All, noise, Noise, Clusters = density_cluster(Data, iradius, Clusters) 
        return All, noise, Noise, Clusters


    def colcol (All, noise):
        Columns = []
        Colours = []
        column = -1
        taken = []

        def colgen (All,Colours):
            for i in range(0,len(All)):
                if (i != (len(All) - 1)) or ((i == (len(All) - 1)) and (noise==False)):
                    color_string = "rgb("
                    for w in range (0,3):
                        if w != 2:
                            color_string += str(randint(10,255)) + ","
                        else:
                            color_string += str(randint(10,255)) + ")"
                    if i == 0:
                        color_val = 0
                        taken.append(color_val)
                    elif i == (len(All) - 1):
                        color_val = 1
                        taken.append(color_val)
                    else:
                        color_val = uniform(0.00000000000001,0.99999999999999999)
                        while (color_val in taken) == True:
                            color_val = uniform(0.00000000000001,0.99999999999999999)
                else:
                    color_val = 1
                    color_string = "rgb(0,0,0)"
                for j in (All[i]):
                    j.append(color_val)
                Colours.append([color_val,color_string])
            return Colours

        Colours = colgen(All,Colours)


        for corit in range (0,len(All[0][0])):
            column+=1
            Columns.append([])
            #print ("Columns: ",Columns)
            for cluster in range (0,len(All)):
                for row in All[cluster]:
                    for cor in range (0,len(row)):
                        Columns[column].append(row[cor])
                        row[cor] = "del"
                        break

            for icluster in range (len(All)-1,-1,-1):
                for icount in range (len(All[icluster])-1,-1,-1):
                    for icor in range (len(All[icluster][icount])-1,-1,-1):
                        if All[icluster][icount][icor]=="del":
                            All[icluster][icount].remove(All[icluster][icount][icor])

        color_list3 = list(Columns[(len(Columns) - 1)])
        del Columns[(len(Columns) - 1)]
        print ("Final Columns: ",Columns)
        print ()
        print ("Colour Identifier: ", color_list3)
        print ()
        print ("Colour Strings: ",Colours)
        return Columns,color_list3,Colours

    All,noise,Noise,Clusters = clustering (dataperson)
    d_cluster,color4,pl_colorscale2 = colcol(All,noise)
    option = 2
    if plot == True:
        Graph(option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles, dim_option, dim_list)
    return Clusters, Noise, d_cluster
"""
K_Means is an unsupervised, iterative clustering method. The point of it is to take a set of data and find groups(clusters) within that dataset. The number of groups
is user defined and is in my program and in general, represented by the variable k. The idea is that data points in a group share more similarities than data points
in another group(another cluster). This is done by making(or selecting) a random datapoint and setting it as a centroid. The job of centroids is to move around until
they have reached/found the center of a cluster. My implementation of K-Means is very closely based on Lloyd's K-Means, thus empty clusters(centroids that have no
points assigned to them) are possible. This K-Means graphing function works in the following order:
1. Select random points as centroids based on k
2. Calculate and find clusters within the dataset
3. Assign a color to each centroid and it's cluster
4. Turn the data into columns for graphing.
"""
def k_means_clustering(k,dataperson,titles,plot, dim_option, dim_list):
    dat2 = deepcopy(dataperson)                                         #Here we use the deepcopy function to clone the original list with all of it's dictionary values
                                                                        #floats, and integers. This is so when we make future calculations, we don't pass by reference,
                                                                        #rather we pass by value. Any future use of this will be for cloning values rather than referencing
                                                                        #them.
    def k_means (dat2,k):

        ilen_dat2 = len(dat2)                                               #dat2 is a list of rows from the original dataset. Thus when we ge the lenght of dat2(current line)
                                                                            #we get the total number of rows there are.

        ilen_row = len(dat2[0])                                             #Getting the lenght of a row to see how many indexs (columns) there are.
        print ('Length: %i' %(ilen_dat2))                                   #Printing the lenght for confirmation
        centroid_list = []                                                  #make an empty list that will store all the centroid coordinates. Each centroid will have a list of
        centroid_list2 = []                                                                    #coordinates for each dimension.

        centroid_point_assignment = []                                      #make an empty list that will store what points are assigned to what centroid. This will change each iteration.
        taken = []                                                          #Make an empty list that will store what rows have been taken so to say. This is a list to check
                                                                            #which datapoints have already been chosen as the starting centroid.

        Cluster_2 = []                                                      #Making an empty list that will contain all the original data seperated by columns, not rows.
                                                                            #Columns are required to make the graphs.

                                                                            #This will be a list of clusters. Inside each cluster will be a list of rows assigned to it.
        pl_colorscale = []                                                  #This is a list that will float values between (0,1) and what color they represent(aka the color of the cluster.

        color_list = []                                                     #This is a list that will store float values in range (0,1) for each row in the dataset. Each value
                                                                            #corresponds to a certain color in pl_colorscale. This color will be used to identify clusters when
                                                                            #graphed.

        color_list2 = []                                                    #This is a second list that will contain colors for each cluster. This is more specifically for
                                                                            #scatterplots.
        #-----------Assign K Centroid Coordinates-------------------------------------------------------------------------------------------------------------------------
        for a in range (0,ilen_row+1):                                          
            Cluster_2.append([])                                                    #Append as many empty lists as there are columns into Cluster_2. Add one more list(column)
            centroid_list2.append([])                                                #for color
            
        for c in range (0,k):                                                       #Run a for loop for one to the # of centroids (k)                                   
            centroid_point_assignment.append([])                                    #Append an empty list in centroid_point_assignment. Each empty list will contain row numbers
                                                                                    #(data points) depending on which centroid it is assigned to. Hence the name centroid_point_assignment.
            icheck = False                                                          #Make icheck equal to false. This will be a check for picking starting positions for the centroids.
            while icheck == False:                                                  
                num = randint(0,(ilen_dat2 - 1))                                    #Get a random integer between 0 and the lenght of dat2. This value will be the datapoint we pick
                                                                                    #from dat2.
                if (num in taken) == False:                                         #We check to see if this point has already been picked.
                    copy = deepcopy(dat2[num])
                    centroid_list.append(copy)                                 #If it hasn't been picked already, we append that point into the centroid list.
                    taken.append(num)                                               #Add this point to the list taken to know it's been picked
                    icheck = True                                                   #Set icheck to True, move on to the next centroid.
        #----------------End Assignment-----------------------------------------------------------------------------------------------------------------------------------
        print ("Centroids: ")
        for icounter in range (0,k):
            print (centroid_list[icounter])
        print ("")
        move = True                                                         #Set move to True to run the while loop. Move represents that if a centroid has move since
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
                    if (len(centroid_point_assignment[d])) != 0:
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
            color_string = "rgb("
            for w in range (0,3):
                if w != 2:
                    color_string +=((str(randint(0,255)) + ","))
                else:
                    color_string +=((str(randint(0,255)) + ")"))                                                                                       
                           

            #In plotly to use colorscaling(assign colors to each individual point), each point needs to have a value related to it that is between 0 and 1. The first value has
            #to be 0, the last has to be 1. Every other value has to be a float value in between the two.
            icheck = False                                  #Here we run another check to select color values.
            while icheck == False:                          
                if icounter == 0:                           #If this is the first centroid(first cluster), it will receive color value of 0
                    colr_val = 0
                elif icounter == (k-1):                         #If its the second centroid(second cluster), it will receive a color value of 1
                    colr_val = 1
                else:                                   
                    colr_val = uniform(0,1)                 #If it's neither the first or the second centroid, make a random float value between (0,1).
                    
                if (colr_val in pl_colorscale) == False:    #If the current color value hasn't been selected already....
                    for p in range (0,len(centroid_point_assignment[icounter])):                #Run a loop that goes through every value in the current centroid_point_assignment list
                        
                        dat2[(centroid_point_assignment[icounter][p])].append(colr_val)  #Append the color value at the end of the row. This will be done for every value in
                                                                                         #that list.
                        icheck = True                                                   #Set icheck to true, end loop
                    pl_colorscale.append([colr_val,color_string])                   #Append the color value and then the colorstring to pl_colorscale. pl_colorscale stores
                    centroid_list[icounter].append(colr_val)                                                                #a color value and what color that value represents in a list of lists. Done according to
                                                                                    #plotly syntax.
            #Underneath, I start to turn all the rows I have been working with so far into columns for graphing purposes.
            for n in range (0,ilen_row+1):                                  #Run a for loop going through every column.        
                column = []                                                 #Make an empty list called column
                for v in range (0,ilen_dat2):                                       #Run a loop that goes through every row
                    if (v in centroid_point_assignment[icounter]) == True:          #if the current row is in the current cluster, append the value in the current column into
                                                                                    #the column list.
                        column.append(dat2[v][n])
                #Cluster[icounter].append(column)                                    #Add this column into Cluster.
                Cluster_2[n].extend(column)                                         #Add this column into Cluster_2. The extend function instead of just adding another element,
                centroid_list2[n].append(centroid_list[icounter][n])                                                                    #combines two lists, which is what we are doing to make one big list of columns.
            #print (centroid_point_assignment[icounter])
        color_list = deepcopy(Cluster_2[len(Cluster_2) - 1])                      #Assign the last column to color_list
        color_list2 = deepcopy(centroid_list2[len(centroid_list2) - 1])
        del Cluster_2[ilen_row:len(Cluster_2)]                                                #Destroy the last column so we only have to original values.
        del centroid_list2[ilen_row:len(centroid_list2)]

        return k,Cluster_2,centroid_list2,pl_colorscale,color_list,color_list2    #Return the number of centroids, the coordinates of each centroid, the color scale/color
                                                                                 #legend, color identifiers for the data points and lastly, color identifiers for the
                                                                                #Centroids.
    option = 1
    k,k_cluster,k_centroid,pl_colorscale,color3,color2 = k_means (dat2,k)
    if plot == True:
        Graph(option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles, dim_option, dim_list)
    return k,k_cluster,k_centroid
    
    









