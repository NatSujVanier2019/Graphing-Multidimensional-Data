import csv
from copy import deepcopy
"""
clustering is a function that is the main function 
"""

def clustering (dataperson):                                            #The whole code is in a function which will be used in the Columning_4_0.txt 
    Data = deepcopy(dataperson)
    rad = False
    
    while rad == False:
        try: 
            iradius = float(input("Please input a radius: "))
            rad = True
        except ValueError:
            print ("Get new eyes!!")
            print ()

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

    def density_cluster(Data,iradius, Clusters):                        #This function classifies data points into clusters and noise points

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
        print ("All: ",All)
        print ("Noise: ",Noise)

             
        print ()                
        print ("Number of Clusters: ", len(Clusters))
        print ("Clusters: ", Clusters)
        print ()        
        return All, noise
    All, noise = density_cluster(Data, iradius, Clusters) 
    return All, noise
    
