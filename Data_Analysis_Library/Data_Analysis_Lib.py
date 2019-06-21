from copy import deepcopy,copy
from random import randint, uniform
from Ploty_Graph_Version_4 import Graph                                     #Importing the graphing function
from Indexing_Rev_31 import fileinput                                       #Importing the file input function that allows the program to take in files and index them.
                
k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2 = None,None,None,None,None,None,None,None,None
#titles,dataperson,category_legend = fileinput()


def density_and_anomaly (dataperson,titles, iradius,plot = True, dim_option = None, dim_list = None):
    """
        density_and_anomaly is a function that inputs following parameters and outputs clusters, anomalies, 2D and 3D scatterplots and a parallel coordinates graph.
        Parameters:
              dataperson(list): The data list in rows.
              
              titles (List): The list containing the values (strings) of the first row of the csv file. Typically, the first row contains column headings,
              hence the name titles.
              
              iradius(float): The radius used to decide the density.
              
              plot: A boolean value what determines if the user wants to graph the results or not. Default value is True
              
              dim_option: Dimension Option, determines how many dimensions the user wants their scatterplot to be. Has to be either 2 or 3. This argument is optional
              thus if not called, will reset to it's default value as None.
              
              dim_list: Dimension list. A list of which dimensions you want to graph. Default is None, thus it is optional. For a more detailed explanation, visit
              k_means_clustering() documentation a few sections below.

        Returns:
              Clusters(list): List of all the clusters.
              Noise(list): List of all the noise points where each noise point is in its separate cluster.
              d_cluster(list): The list of clusters and noise points together but in columns.
    """



    def clustering (dataperson):                                            #The whole code is in a function which will be used in the Columning_4_0.txt 
        Data = deepcopy(dataperson)
        """
            clustering is a function that uses raw data as a parameter and returns cluster and anomalies.
            Parameters:
                  dataperson(list): The data list in rows.

            Returns:
                  All(list): List of clusters and noise points together where all the noise points are in one cluster.
                  noise(boolean): Variable that is True/False depending on whether there are any noise points. 
                  Noise(list): List of all the noise points where each noise point is in its separate cluster.
                  Clusters(list): List of all the clusters.
        """     


        def cluster (iprime, inext, iradius):                               #This functions determines if 2 points (iprime and icheck) are within a radius (iradius).
            """
                cluster is a function that uses two points (their coordinates) and a radius as parameters. It returns True if the two points are within the given
                radius of each other.
                Parameters:
                      iprime(list): A data point being iterated.
                      inext(list): Another data point being iterated that will be checked to see if it is in the radius of iprime.
                      iradius(float): The radius used to decide the density.

                Returns:
                      True: Only if iprime and inext are within radius of each other.
            """


            square_sum = 0                                                  #square_sum intialized to 0.
            for i in range (0, len(iprime)):                                #Loop runs for the number of coordinates in a data point (which is the same for each data point). 
                square_sum += ((float(iprime[i]))-(float(inext[i])))**2     #Uses the distance formula except the last step of square rooting.
            dist = square_sum**0.5                                          #Finds distance by square rooting square_sum.
            if dist <= iradius:                                             #If the distance is less than or equal to the radius....
                return True                                                 #....then returns True.

        Clusters = []                                                       #Creates a void list called Clusters.
        Noise = []                                                          #Creates a void list called Noise. 


        def density_cluster(Data,iradius,Clusters):                        #This function classifies data points into clusters and noise points

            """
                density_cluster is a function that uses a data list, a radius and a void list (Clusters) as parameters. It iterates through the data list.
                It passes 2 points and the given radius as parameters for the cluster function to form density based clusters. These clusters are stored in the
                Clustsers list.
                Parameters:
                      Data(List): A deepcopied version of dataperson.
                      iradius(float): The radius used to decide the density.
                      Clusters(list): List of all the clusters but for now, a void list.

                Returns:
                      All(list): List of clusters and noise points together where all the noise points are in one cluster.
                      noise(boolean): Variable that is True/False depending on whether there are any noise points. 
                      Noise(list): List of all the noise points where each noise point is in its separate cluster.
                      Clusters(list): List of all the clusters
            """

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
                   

            All = list(Clusters)                                            #All is a copy of the Clusters list.
    ##        print (All[len(All)-1])

            if noise==True:                                                 #If the boolean variable noise=True...
                All.append([])                                              #A void list is appended to All.
                for c in Noise:                                             #For Loop iterates the clusters in the Noise list.
                    for n in c:                                             #For Loop iterates the noise points in each cluster (there is only one).
                        All[len(All)-1].append(n)                           #The noise point currently being iterated is appended to the last list in All.
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

        """
            colcol is a function that uses an All list i.e. a list that contains all the clusters and noise point, and a boolean called noise which is True if any noise  
            points exist and False if not, as parameters. It assigns colours and colour identifiers to every cluster and converts all the clusters from rows to 
            columns.
            Parameters:
                  All(list): List of clusters and noise points together where all the noise points are in one cluster.
                  noise(boolean): Variable that is True/False depending on whether there are any noise points.

            Returns:
                  Columns(list): The list of clusters and noise points together but in columns.
                  color_list3(list): List of int values which will be used to identify the colours of every cluster while graphing. Uses plotly syntax
                  Colours(list): List of string and int values used to assign rgb colours to every cluster while graphing. Uses plotly syntax
        """

        
        Columns = []
        Colours = []
        column = -1
        taken = []                  #taken is a throw away list that will be used to check color_val which is defined underneath


        def colgen (All,Colours):

            """
                colgen is a function that uses All list and a void list called Colours as parameters, assigns colours to every cluster(including clusters of noise points).
                Parameters:
                      All(list): List of clusters and noise points together where all the noise points are in one cluster.
                      Colours(list): List of string and int values used to assign rgb colours to every cluster while graphing but for now, just a void list.

                Returns:
                      Colours(list): List of string and int values used to assign rgb colours to every cluster while graphing.
            """

            
            for i in range(0,len(All)):                                                     #Run a loop that goes through all of the data points in All.
                if (i != (len(All) - 1)) or ((i == (len(All) - 1)) and (noise==False)):     #If this is not the last cluster or the last cluster is not all noise points
                    
                    #Underneath I decided to make a string that contains rgba values based on plotly syntax for graphing. We start with the string and run a loop.
                    #I basically run a for loop and concatonate values into the strings. Random values for r,g and b.
                    color_string = "rgb("               #Start the rgb string
                    for w in range (0,3):           #Run the loop three times, once for each rgb value.
                        if w != 2:
                            color_string += str(randint(10,255)) + ","   #Concatenate the color string.
                        else:
                            color_string += str(randint(10,255)) + ")"
                    if i == 0:
                        color_val = 0               #if it's the first cluster, set the color_val to 0. This is because of plotly syntax.
                        taken.append(color_val)     #Append the color_val to taken, so we know which ones are used.
                    elif i == (len(All) - 1):  #If it's the last cluster and there are no noise points, set the color_val to 1. All because of plotly colorscale syntax.
                        color_val = 1       
                        taken.append(color_val)     #Set this into taken.
                    else:
                        color_val = uniform(0.00000000000001,0.99999999999999999)  #Make a random color_val that will be between 0 and 1 but never 0 and 1.
                        while (color_val in taken) == True:
                            color_val = uniform(0.00000000000001,0.99999999999999999) #If this value is already take, make a new one.
                else:       #if it is the last cluster and there are noise points, then set the color_val to 1 and set the rgb value to black.
                    color_val = 1
                    color_string = "rgb(0,0,0)"     #This is done so that the last cluster will be noise points only, thus they will all be black.
                for j in (All[i]):          
                    j.append(color_val)                     #Append the color_val at the end of every row in the current cluster.
                Colours.append([color_val,color_string])   #Append the color_val and the colorstring as a list in Colours. This is for Plotly colorscaling.
            return Colours              #Return only colors from this function.

        Colours = colgen(All,Colours)   #Run the colgen function.


        for corit in range (0,len(All[0][0])):                                          #For Loop runs for the number of coordinates (dimensions) of the dataset.
            column+=1                                                                   #column increments by 1 for every iteration of the above For Loop.
            Columns.append([])                                                          #The list called Columns appends 1 void list.
            #print ("Columns: ",Columns)
            for cluster in range (0,len(All)):                                          #For Loop iterates for the number of clusters in All.
                for row in All[cluster]:                                                #For Loop iterates through each data point in each cluster.
                    for cor in range (0,len(row)):                                      #For Loop iterates through each coordinate in each data point.
                        Columns[column].append(row[cor])                                #The coordinate being currently iterated is appended to the columnth place in the list Columns.
                        row[cor] = "del"                                                #The place of the coordinate in All is replaced by the string "del".
                        break                                                           #The loop breaks.

            for icluster in range (len(All)-1,-1,-1):                                   #For Loop iterates in the descending order for the number of clusters in All.
                for icount in range (len(All[icluster])-1,-1,-1):                       #For Loop iterates in the descending order for the number of data points in each cluster.
                    for icor in range (len(All[icluster][icount])-1,-1,-1):             #For Loop iterates in the descending order for the number of coordinates in each data point.
                        if All[icluster][icount][icor]=="del":                          #If the string "del" is spotted in the place of any coordinate...
                            All[icluster][icount].remove(All[icluster][icount][icor])   #...it is removed.

##            for icolumn in range (len(Colums)-1,-1,-1):
##                for icor in icolumn

        color_list3 = list(Columns[(len(Columns) - 1)])                                 #The last list (containing colour identifiers) is copied to color_list3 
        del Columns[(len(Columns) - 1)]                                                 #The last list (containing colour identifiers) is deleted from Columns.

        print ("Final Columns: ",Columns)
        print ()
        print ("Colour Identifier: ", color_list3)
        print ()
        print ("Colour Strings: ",Colours)
        return Columns,color_list3,Colours

    All,noise,Noise,Clusters = clustering (dataperson)
    d_cluster,color4,pl_colorscale2 = colcol(All,noise)
    option = 2
    if plot == True:                                                                #If plot is True (a.k.a the user wants us to graph the results)
        Graph(option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles, dim_option, dim_list) #Run Graph function
    return Clusters, Noise, d_cluster      #Return All the data points sorted into clusters using rows, all the noise(anomaly) points and density cluster columns.

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
def k_means_clustering(dataperson,titles,k,plot = True, dim_option = None, dim_list = None):
    '''
    k_means_clustering is the big method that encompasses both the actual k_means function that calculates the mean points and the graphing function. This is the
    method/function the user will launch/use when they want to use the K means clustering module.

    K Means in general is an unsupervised, iterative clustering method. The idea is to take a set of data points and find groups(clusters) within that dataset.
    The number of groups is defined by the user. This implementation of K Means is based on Lloyd's K Means algorithm. K Means finds clusters by using centroids.

    Parameters:
        dataperson (List): dataperson is a list of the values that were returned from fileinput(). These values were taken from the original csv file and put into
        a list of lists where each list in dataperson is a row in the original csv file. We use this list as our reference and make a clone of it stored in dat2.
        
        titles (List): The list containing the values (strings) of the first row of the csv file. Typically, the first row contains column headings,
        hence the name titles.
        
        k (int): The number of centroids to be made/used. This is a key argument essential to running the function.

        plot (boolean): A boolean value that the user sets as either True (plot the results of the k_means() ) or False (don't plot the results of k_means() ).
        Default value is True. This parameter is optional.
        
        dim_option (int): An integer that defines how many dimensions the user wants in their scatterplot. It can be only either 2 or 3 because you can only make a
        scatterplot of 2 or 3 dimensions. If the user enters more than 3 or less than 1, a scatterplot simply isn't made. Default value is None, making this an
        optional parameter. Named as a shorthand for dimension option.
        
        dim_list (List): A list of the dimensions the user would like to plot on a scatterplot. This is integer based. (Named as a shorthand for dimension list)
            Example: To plot the first, second and third dimension, you would write:
            
                        k_means_clustering (dataperson, titles, k, plot, dim_option = 3, [1,2,3])
                        
                   - To plot the thrid and fourth dimension, you can write dim_list = [3,4]
    Key Variables:
        dat2: This is a complete clone of dataperson. We use dat2 to make our actual calculations for K means clustering.

        **pl_colorscale, color3, and color2 will be explained in detail in Plotly_Graph_Version_4.Graph documentation.
        
    Returns:
        ** k is described above
        
        k_cluster (List): This is a list of lists that contains all the data from dat2. Each list in k_cluster contains a column from the csv file. k_cluster is mainly
        used to make the final graph however is returned incase if it needs to be used for external purposes.
        
        k_centroid (List): This is a list of lists where each list inside k_centroid, seperated into columns. Each column is a different dimension, values in each list
        in k_centroid are that dimension's centroid coordinate. Centroids are connected through their index values in the smaller lists inside k_centroid.
            Example: centroid P is at (1,2,3) and centroid Q is at (5,6,7) ----->   X  |   Y   |   Z
                                                                                 ---------------------
                                                                                 [1,5] | [2,6] | [3,7]

        sep_k_cluster (List): This is the same as k_cluster except each cluster is seperated into different lists in sep_k_cluster.
    '''
    dat2 = deepcopy(dataperson)                                         #Here we use the deepcopy function to clone the original list with all of it's dictionary values
                                                                        #floats, and integers. This is so when we make future calculations, we don't pass by reference,
                                                                        #rather we pass by value. Any future use of this will be for cloning values rather than referencing
                                                                        #them.
    def k_means (dat2,k):
        '''
        k_means is a function that performs the necessary calculations for the K means clustering method.

        Parameters:
            **All parameters are explained in the docstrings for k_means_clustering function above.
        Key Variables:
            centroid_point_assignment (List)) : This is a list that will contain index values from dat2 to track which data point is assigned to which centroid.
            centroid_point_assignment will have as many elements as there are centroids, and each element will contain a list of index values stored in that specific centroid.
            To tell which element is for which centroid, simply match index values from centroid_list.

            centroid_list (List): A list that contains the coordinates of every centroid.
            Cluster_2: The final list of columns after all the calculations are done and all clusters are found.
            
        Process:
            1. Selects k number of random points from the dataset (dat2) as starting position for k centroids.
            2. Calculates the euclidean distance of every point to every centroid, picking the smallest distance and assigning that point to that centroid.
            3. Calculate the new mean value.
            4. Repeat steps 2 and 3 until no centroid has moved (changed coordinates)
            5. Assign each cluster a color. Assign that color to each point in that cluster.
            6. Turn all the data points from being row seperated to column seperated
            7. End process
        Returns:
            ** Most returns have been explained. To view Cluster_2,k and centroid_list2, visit k_means_clustering() documentation.
            ** To view pl_colorscale, color3 and color2, view Plotly_Graph_Version_4.Graph documentation.
            Cluster (List): Cluster is the same as k_cluster/Cluster2 except each element in Cluster is a different cluster. This variable is renamed to sep_k_cluster
            as a shorthand for seperated k clusters. Each cluster is a seperate element.
        '''

        ilen_dat2 = len(dat2)                                               #dat2 is a list of rows from the original dataset. Thus when we ge the lenght of dat2(current line)
                                                                            #we get the total number of rows there are.

        ilen_row = len(dat2[0])                                             #Getting the lenght of a row to see how many indexs (columns) there are.
        print ('Length: %i' %(ilen_dat2))                                   #Printing the lenght for confirmation
        centroid_list = []                                                  #make an empty list that will store all the centroid coordinates. Each centroid will have a list of
        centroid_list2 = []                                                                    #coordinates for each dimension.

        centroid_point_assignment = []                                      #make an empty list that will store what points are assigned to what centroid.
                                                                            #This will change each iteration.
        
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
        
        Cluster = []                                                        #Make a list that will store each cluster, but seperated by columns.
        #-----------Assign K Centroid Coordinates-------------------------------------------------------------------------------------------------------------------------
        for a in range (0,ilen_row+1):                                          
            Cluster_2.append([])                                                    #Append as many empty lists as there are columns into Cluster_2. Add one more list(column)
            centroid_list2.append([])                                               #for color
        for c in range (0,k):                                                       #Run a for loop for one to the # of centroids (k)                                   
            centroid_point_assignment.append([])                                    #Append an empty list in centroid_point_assignment. Each empty list will contain row numbers
                                                                                    #(data points) depending on which centroid it is assigned to. Hence the name centroid_point_assignment.

            Cluster.append([])                                                      #append an empty list into Cluster. A placeholder for future values.
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
                Cluster[icounter].append(column)                                    #Add this column into Cluster.
                Cluster_2[n].extend(column)                                         #Add this column into Cluster_2. The extend function instead of just adding another element,
                centroid_list2[n].append(centroid_list[icounter][n])                                                                    #combines two lists, which is what we are doing to make one big list of columns.
            #print (centroid_point_assignment[icounter])
        color_list = deepcopy(Cluster_2[len(Cluster_2) - 1])                      #Assign the last column to color_list
        color_list2 = deepcopy(centroid_list2[len(centroid_list2) - 1])
        del Cluster_2[ilen_row:len(Cluster_2)]                                                #Destroy the last column so we only have to original values.
        del centroid_list2[ilen_row:len(centroid_list2)]
        print ("Centroids: \n" , centroid_list2)
        print ("Data in Columns:\n", Cluster_2)

        return k,Cluster_2,centroid_list2,pl_colorscale,color_list,color_list2,Cluster    #Return the number of centroids, the coordinates of each centroid, the color scale/color
                                                                                 #legend, color identifiers for the data points and lastly, color identifiers for the
                                                                                #Centroids.
    
    option = 1                                                                    #Set option to 1, means we are running K means clustering
    k,k_cluster,k_centroid,pl_colorscale,color3,color2,sep_k_cluster = k_means (dat2,k)         #Run k_means()
    if plot == True:                                                            #If plot is True (a.k.a the user wants us to graph the results)
        Graph(option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles, dim_option, dim_list)  #Run Graph function
    return k,k_cluster,k_centroid,sep_k_cluster    #return the value of k, the dataset in columns, the centroids in columns, the dataset seperated
                                                                    #into clusters in columns.









