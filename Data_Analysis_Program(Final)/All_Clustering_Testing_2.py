#--------------Importing Modules------------------------------------------
from tkinter import *
import time
from plotly import tools
#----------------------Import Files--------------------------------
from Indexing_Rev_31 import fileinput                           #Importing the file input function that allows the program to take in files and index them.
from Ploty_Graph_Version_3 import Graph              #Importing the graphing function
import K_Means_Clustering_1                          #Importing K-Means Clustering algorithm
import Columning_RGB_2                                #Importing Density rows ---> Columning function and color assignment for Density
from Infinite_Dimensional_Clustering_RGB_3 import clustering      #Importing Density Clustering Algorithm and it's accompanying Anomaly Detection
# Underneath a check to see if the user has made a plotly account or not.
print ("""In order to use our program, you require the modules Plotly,random,csv and time. To use plotly, you need to make a plotly account. This account is completely
free. Once you make your account, be sure to generate an API key to use it. We can make the credentials file for you. All we need is your username and the API key.
This program works completely offline and only uses your browser to open an embed HTML file. That HTML file will be your interactive graph. Thank you for using our
program.""")
def plotly():
    class Window(Frame):
        def __init__(main, graph=None):
            Frame.__init__(main, graph)                 
            main.graph = graph
            main.init_window()

                                                                        #Creation of init_window
        def init_window(main):

                                                                        #Changing the title of our master widget      
            main.graph.title("Welcome To The MainFrame!")

                                                                        #Allowing the widget to take the full space of the root window
            main.pack(fill=BOTH, expand=2)

                                                                        #Creating Kmeans Button
            Yes = Button(main, text="Yes", font = ("Times",30),fg="White", bg="Black",command = mainprogram, width = 15)

                                                                        #Placing Kmeans button on the screen
            Yes.place(x=500, y=200)

                                                                        #Creating Density Clustering button
            No = Button(main, text="No",fg="white",bg = "Black",font =("Times",30),command = account, width = 15)#,height = 30) #width = 50,bg = 'blue')
            #DensityButton.config( width = 200, height = 200)
                                                                        #Placing the the Density Clustering Button on the screen
            No.place(x=75, y=200)

            Welcometext = Label(root,text = "Data Analysts", font = ("Times", 44), fg= "Black").place (x=250, y=0)

            ImportantMessage = Label(root,text="***Do You Have A Plotly Credential File?***", font =("Arial", 25), fg = "red").place (x=150,y=90)
    root = Tk()
    root.minsize(871, 715)
    root.maxsize(871, 715)
    app = Window(root)
    root.mainloop()  
    print ("""**Please make sure you enter the following information correctly. If you don't want us to make your credentials file, you can do it on Python yourself.
    Visit https://plot.ly/python/getting-started/ for the instructions on how to do it on your own.""")

#Underneath, we make the user's credential files that will allow them to make graphs for them.
def account():
    user = input("What is your username:  ")
    API = input("Please enter the API key for your account:  ")
    tools.set_credentials_file(username= user, api_key= API)
    print ("Congrats. Your credentials file has been set.")
    mainprogram()
def mainprogram():
    yes = True                                                                                          #Initializes yes to True.
    titles,dataperson,category_legend = fileinput()
    while yes == True:                                                                                  #While Loop runs as long as yes is True
        try:
            def method1():
                    #method = int(input("Choose a clustering method: (1)Density-based (2)K-Means (3)Exit\n"))    #User chooses the method of clustering.
                                   #Run Density and Anomaly clustering Algorithm
                    option = 2
                    Clusters,anomaly_detector = clustering (dataperson)      #Run Density-based Clustering
                    d_cluster,color4,pl_colorscale2 = Columning_RGB_2.colcol (Clusters,anomaly_detector)     #Run Columning for color assignment and turning rows to columns.
                    k,k_cluster,k_centroid,pl_colorscale,color3,color2 = None,None,None,None,None,None      #Set all the values from K-Means to none as it is not being used
                                                                                                            #Rather than have K-Means run unecessarily, we give the user an option
                                                                                                            #and whichever is not being used will be set to none.
                    print ("Loading...")
                    Graph (option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles)  #Run the Graph function to graph the results
            def method2():    
                                                                                                    #Run K-Means Clustering         
                    option = 1
                    k,k_cluster,k_centroid,pl_colorscale,color3,color2 = K_Means_Clustering_1.K_Means (dataperson)
                    d_cluster,color4,pl_colorscale2 = None,None,None
                    print ("Loading...")
                    Graph (option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles)  #Run Graph  
    ##        def method3():                                                                            #Program runs until the user inputs the exit command(3).
    ##                yes = False
    ##            else:                                                                                       #Error trapping.
    ##                print ("You think you are funny?")                                                      
    ##                for i in range(5,-1,-1):                                                                #For Loop for i values of 5 to 0(descending).
    ##                    print ("CHEATER DELAY: %i seconds remaining..."%(i))                                #Cheater Timer :)
    ##                    time.sleep(1)
            class Window(Frame):
                def __init__(main, graph=None):
                    Frame.__init__(main, graph)                 
                    main.graph = graph
                    main.init_window()

                                                                                #Creation of init_window
                def init_window(main):

                                                                                #Changing the title of our master widget      
                    main.graph.title("Welcome To The MainFrame!")

                                                                                #Allowing the widget to take the full space of the root window
                    main.pack(fill=BOTH, expand=2)

                                                                                #Creating Kmeans Button
                    KmeansButton = Button(main, text="K Means", font = ("Times",30),fg="White", bg="Black",command = method2, width = 15)
                                                                                #Placing Kmeans button on the screen
                    KmeansButton.place(x=500, y=200)

                                                                                #Creating Density Clustering button
                    DensityButton = Button(main, text="Density Clustering",fg="white",bg = "Black",font =("Times",30),command = method1)#,height = 30) #width = 50,bg = 'blue')
                    #DensityButton.config( width = 200, height = 200)
                                                                                #Placing the the Density Clustering Button on the screen
                    DensityButton.place(x=75, y=200)

                    Welcometext = Label(root,text = "Data Analysts", font = ("Times", 44), fg= "Black").place (x=250, y=0)

                    ImportantMessage = Label(root,text="***Please make sure you have these modules: plotly, copy, csv, time and random***", font =("Arial", 10), fg = "red").place (x=175,y=90)
            root = Tk()
            root.minsize(871, 715)
            root.maxsize(871, 715)
            app = Window(root)
            root.mainloop()
        except ValueError:                                                                              #Error trapping for string input (int expected).
            print("Invalid Input")      
plotly()
