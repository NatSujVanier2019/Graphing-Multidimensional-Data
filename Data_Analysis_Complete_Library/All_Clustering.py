#--------------Importing Modules------------------------------------------
import time
from plotly import tools
#----------------------Import Files--------------------------------
from Indexing_Rev_31 import fileinput                           #Importing the file input function that allows the program to take in files and index them.
from Ploty_Graph_Version_3 import Graph              #Importing the graphing function
import K_Means_Clustering_1                          #Importing K-Means Clustering algorithm
from Columning_RGB_2 import colcol                               #Importing Density rows ---> Columning function and color assignment for Density
from Infinite_Dimensional_Clustering_RGB_3 import clustering      #Importing Density Clustering Algorithm and it's accompanying Anomaly Detection
#----OPEN WINDOW---------------
# Underneath a check to see if the user has made a plotly account or not.
print ("""In order to use our program, you require the modules Plotly,random,csv and time. To use plotly, you need to make a plotly account. This account is completely
free. Once you make your account, be sure to generate an API key to use it. We can make the credentials file for you. All we need is your username and the API key.
This program works completely offline and only uses your browser to open an embed HTML file. That HTML file will be your interactive graph. Thank you for using our
program.""")

option3 = int(input("Do you have a plotly account that is set up on this computer?\n(1)Yes   (2)No \n"))
if option3 == 2:
    print ("""**Please make sure you enter the following information correctly. If you don't want us to make your credentials file, you can do it on Python yourself.
Visit https://plot.ly/python/getting-started/ for the instructions on how to do it on your own.""")

#Underneath, we make the user's credential files that will allow them to make graphs for them.
    user = input("What is your username:  ")
    API = input("Please enter the API key for your account:  ")
    tools.set_credentials_file(username= user, api_key= API)
    print ("Congrats. Your credentials file has been set.")
#------DESTROY WINDOW----------------    
yes = True                                                                                          #Initializes yes to True.
titles,dataperson,category_legend = fileinput()
while yes == True:                                                                                  #While Loop runs as long as yes is True
##    try:
    #DESTROY WINDO
    method = int(input("Choose a clustering method: (1)Density-based (2)K-Means (3)Exit\n"))    #User chooses the method of clustering.
    if method==1:                   #Run Density and Anomaly clustering Algorithm
        option = 2
        Clusters,anomaly_detector = clustering (dataperson)      #Run Density-based Clustering
        d_cluster,color4,pl_colorscale2 = colcol (Clusters,anomaly_detector)     #Run Columning for color assignment and turning rows to columns.
        k,k_cluster,k_centroid,pl_colorscale,color3,color2 = None,None,None,None,None,None      #Set all the values from K-Means to none as it is not being used
                                                                                                #Rather than have K-Means run unecessarily, we give the user an option
                                                                                                #and whichever is not being used will be set to none.
        print ("Loading...")
        #Delete Loading.....
        Graph (option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles)  #Run the Graph function to graph the results
        
    elif method==2:                                                                                #Run K-Means Clustering         
        option = 1
        k,k_cluster,k_centroid,pl_colorscale,color3,color2 = K_Means_Clustering_1.K_Means (dataperson)
        d_cluster,color4,pl_colorscale2 = None,None,None
        print ("Loading...")
        Graph (option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles)  #Run Graph  
    elif method==3:                                                                             #Program runs until the user inputs the exit command(3).
        yes = False
    else:                                                                                       #Error trapping.
        print ("You think you are funny?")                                                      
        for i in range(5,-1,-1):                                                                #For Loop for i values of 5 to 0(descending).
            print ("CHEATER DELAY: %i seconds remaining..."%(i))                                #Cheater Timer :)
            time.sleep(1)                                                                       
##    except ValueError:                                                                              #Error trapping for string input (int expected).
##        print("Invalid Input")      
