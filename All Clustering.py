import time

yes = True                                                                                          #Initializes yes to True.
while yes == True:                                                                                  #While Loop runs as long as yes is True
    try:                                                                                            #Tries the following code.
        method = int(input("Choose a clustering method: (1)Density-based (2)K-Means (3)Exit\n"))    #User chooses the method of clustering.
        if method==1:
            import Density_Big_Program
        elif method==2:
            import K_Means_Big_Program
        elif method==3:                                                                             #Program runs until the user inputs the exit command(3).
            yes = False
        else:                                                                                       #Error trapping.
            print ("You think you are funny?")                                                      
            for i in range(5,-1,-1):                                                                #For Loop for i values of 5 to 0(descending).
                print ("CHEATER DELAY: %i seconds remaining..."%(i))                                #Cheater Timer :)
                time.sleep(1)                                                                       
    except ValueError:                                                                              #Error trapping for string input (int expected).
        print("Invalid Input")
        
