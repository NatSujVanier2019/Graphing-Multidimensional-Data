#--------------Importing Modules-------------------------------
import plotly
import plotly.graph_objs as graph
#-----------Functions----------------------------------------------------
"""
make_dimension is a function that allows us to make an infinite number of dimensions based on the current dataset being graphed, be it the original or the edited version.
make_dimensions takes a column in a dataset and sorts it to get the maximum and minimum value. It then makes a directory for that column. This directory contains the
range of the data, it's label and the values that will be graphed. It then appends that directory into a pre-made list named axis. The range, label and values are all
required so that we can graph this column in our parallel coordinates graph.
"""
def make_dimension(ilen,data,axis,Scatter_dimensions):                              #Creating the function make_dimensions with the parameters ilen, dat2 and axis.
    '''
    make_dimension is a function that allows us to make an infinite number of dimensions based on data set for plotly. This makes an infinite number of dimensions for
    Parallel Coordinaes Plot and the Scatterplot Matrix.

    Parameters:
        ilen (int): The lenght of the data set(a.k.a how many columns/dimensions there are)
        data (List): The dataset that will be used to make the dictionaries for each dimension according to Plotly syntax. Is either k_cluster or d_cluster
        axis (List): A list of dictionaries for each dimension for the Parallel Coordinates plot according to Plotly syntax.
        Scatter_dimensions (List): A list of dictionaries for each dimension according to Plotly syntax.
    Returns:
        Returns axis and Scatter_dimensions in order for them to be used to make the different graphs.
    '''
    for x in range (0,ilen):                                                        #Running a for loop that will go through every index value of the list dat2.
                                                                               #dat2 is a list that contains all the columns and values from the original data list.
                                                                                    #It is basically a list of lists.
        
        icolumn = list(data[x])                                                           #Making a temporary list, icolumn to store the current list in dat2.
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
                values = data[x]                                                    #Setting which values to plot on this dimension/axis.
                )                                                                   #Ending the directory
        )                                                                           #Ending the append bracket.
        Scatter_dimensions.append(                                                  #Append a directory for each axis/dimension
            dict(
                label = chr(65 + x),                                                
                values = data[x]
                )
        )                                                                            #End of function.
    return (list(axis)),(list(Scatter_dimensions))

'''
Graph is the main graphing function for this program. It was made using the Plotly module and it makes four types of graphs: Parallel Coordinates Plot, Scatterplot
Matrix and a 2D Scatterplot or a 3D Scatterplot. This function takes in arguments on how many datapoints there are, colors assigned to each point, colors of each
cluster, and axes titles. The function runs after Density or K-Means. All the interactive graphs are made here.
'''
def Graph (option,k,k_cluster,k_centroid,pl_colorscale,color3,color2,d_cluster,color4,pl_colorscale2,titles,category_legend):
    '''
    Graph is the main graphing function for Data_Analysis_Lib. This function graphs the results of the K means clustering and Density clustering methods.
    
    Parameters:
        **Certain parameters such as k,k_cluster,k_centroid,titles,dim_option and dim_list are explained in the k_means_clustering() documentation.
        
        color3 (List): color3 is also known as color_list in k_means(). This parameter is a list of color identifiers that go from 0 to 1 based on Plotly syntax.
        This is used in conjuction with pl_colorscale for colorscaling in Plotly.
        
        color2 (List): It is the same as color3 except it is for k_centroids.
        
        pl_colorscale (List): pl_colorscale is the colorscale for k_cluster and k_centroids. This is used to color individual data points a different color based on
        which cluster it is in. It is a list of lists in which each element in pl_colorscale is a list in which the first value is the color identifier and the second
        value is the actual color they represent, made using rgb values. Used for the colorscale function in Plotly.
        
        pl_colorscale2 (List): pl_colorscale2 is the colorscale for d_cluster. This is for the Plotly colorscale function.
        
        option (int): option is a variable used to check if the user had run k_means() or density_cluster() beforehand. This will help determine if the program needs
        needs to use k_cluster or d_cluster for the data.
    Returns:
        There are no returns however, the program opens 4 HTML graphs: A parallel coordinates plot, scatterplot matrix, 2D scatterplot and a 3D scatterplot.
    '''
    #Underneath is an if statement to check to see if option is 1(K-Means) or 2(Density). This will determine from which Clustering method are we getting our data from
    #and thus, which type of clustering results are we showing.
    if option == 1:
        ilen = len(k_cluster)               #Set ilen to lenght of k_cluster
        data = k_cluster                    #Set data to k_cluster
    else:
        ilen = len(d_cluster)               #Set ilen to lenght of d_cluster
        data = d_cluster                    #Set data to d_cluster.
    axis = []                                                                     #Make an empty list for all the axis/dimensions to go into.
    Scatter_dimensions = []                                         #Make an empty list for all the dimensions specifically for the Scatterplot Matrix
    axis, Scatter_dimensions = make_dimension(ilen,data,axis,Scatter_dimensions)        #Run the make_dimensions function to make dimensions for our graph
                                                                                        #based on the data(K-Means Clusters or Density Clusters)
    #------------Plotting time--------------------------------------------------------
    #This is where we graph all the data we got from the dataset. For plotly to graph, you require 3 parameters. First is the data a.k.a the actual graph, a file name and
    #a boolean value that determines to automatically open the figure or not. Plotly offline mode stores the graph as a local HTML file and opens it on your web browser.
    #-----------------Scatterplot Matrix------------------------------------------------------
    # Underneath is where we graph the scatterplot matrix. This follows the syntax of plotly scatterplot matrix function.
    trace = [graph.Splom(                                                                   #Running the function Splom to graph the scatterplot matrix. We need to make
                                                                                            #a list called trace because the module that shows the graph only takes list arguments
        
                dimensions = Scatter_dimensions,                                            #Add the dimension arguments/ axis directories from our make_dimensions function.
                marker=dict(
                    color= 'lightsteelblue',                                                #Set the marker style(the way our dots will look)
                    size=5,                                                                 #Here we set a size for the dots, give them a color
                    showscale=False,
                    line= dict(                                                             #Line will represent the set of data from the y axis. It will be represented by blue.
                                                                                            #The set of corresponding data from the x axis will be light blue.
                        width=0.5,                                                       
                        color='blue'                                                        #Set the line color to blue and the width to 0.5
                               )
                    )
                )
             ]

    #-----------------Parallel Coordinates Graph-----------------------------------
    #Underneath, we make a list called data to store the function that lets us make the parallel coordinates graph. Again, we need a list to graph the data.
    #We also run a check to see which clustering method are we representing. Different methods means using a different colorscale and color assignment.
    if option == 1:
        data = [                                                                            
                    graph.Parcoords(                                                        
                        line = dict(color = color3, colorscale = pl_colorscale),        #We use the colorscale and color argument to make it so that each line will have
                                                                                        #a color identifier between 0 and 1, according to plotly syntax. We then use
                                                                                        #the colorscale variable to match the color identifier with a color. Such as
                                                                                        #all datapoints with the color identifier 0 are going to be white, and all the
                                                                                        #datapoints with the color identifier 1 are going to be black. pl_colorscale is
                                                                                        #our colorscale variable and color3 is the list of identifiers. Each identifier
                                                                                        #matches the index value of it's corresponding point.
                        
                        dimensions = axis                           #The number of dimensions is a list, thus we add our list of axis to the dimensions variable.
                    )                                                                       
                ]
    else:
        data = [                                                                            
                graph.Parcoords(                                                        
                    line = dict(color = color4, colorscale = pl_colorscale2),           #This is the same as the one above, only except this is for Density clusters (d_cluster)
                    dimensions = axis                                   #The number of dimensions is a list, thus we add our list of axis to the dimensions variable.
                )                                                                       
            ]

    #Underneath, we save the figure/graph as a local HTML file, Give the file the name Parallel Cooridinates.html and make the boolean argument auto_open to true. This
    #will allow us to graph offline and open it instantly.
    plotly.offline.plot(data, filename = 'Parallel Coordinates.html',auto_open = True)  #Here, we save the figure/graph and plot it.
    plotly.offline.plot(trace, filename = 'Scatter Plot Matrix.html', auto_open = True)
    print ("Dimension Legend")                  #Since on a Parallel Coordinates and Scatterplot Matrix, giving each individual dimension/axis a title will make the
                                                #graph too congested. Thus we have decided to give a graph a letter based Identifier which we will now display a legend for.
    for m in range (0,ilen):                #Run a loop that goes for how many columns there are.
        identifier = chr(m + 65)            #Make a capital alphabet character for that axis/column. This is the same as the one we have graphed
        print (identifier, ":", titles[0][m])       #print out the letter and it's corresponding axis label/Column title.
    print (category_legend)
    #---------------Scatter Plots------------------------------------------------
    #Underneath, We ask the user if they what 3 axis they want to see. This is an option for the user to see the relationship between three specific axis ans visually see
    #data trends. 
    x_option = ((ord(input("Enter the x axis: "))) - 65)            #Here we ask the user for an axis that will be plotted on the x dimension.
                                                                    #We ask for the letter identifier.
    y_option = ((ord(input("Enter the y axis: "))) - 65)            #Ask for y dimension
    
                                            #If the user had asked for 3 dimensions, then we ask for z.
    z_option = ((ord(input("Enter the z axis: ")))- 65)            #ask for Z dimension 
    trace = []                                                  #Make an empty list called trace.
    trace1 = []                                
    if option == 1:                         #Check if K-Means was the clustering method used.
        trace.append(                       #Append into the list trace.
            graph.Scatter(                  #Run the function Scatter from plotly to make the 2D scatterplot.
                x = k_cluster[x_option],        #Set the x axis to have the values from k_cluster based on the axis picked by the user
                y = k_cluster[y_option],        #Set the y axis values from k_cluster
                mode = "markers",               #Set the mode to markers which will plot only dots
                marker = dict(              #Make a dictionary for marker
                    size = 10,          #make the size of each datapoint 10
                    color = color3,         #Run the colorscaling
                    colorscale = pl_colorscale
                    )))
        trace.append(                   #Append the results from another Scatter function for the centroids.
            graph.Scatter(              
                x = k_centroid[x_option],       #Pick the x axis from k_centroids list
                y = k_centroid[y_option],       #Pick the y_axis from k_centroids list
                mode = "markers",           #Set the mode to markers(dots)
                marker = dict(          #Make a dictionary for these marker points as well
                    size = 13,          #To distinguish between centroids and datapoints, the centroids will be larger than all the datapoints.
                    color = color2,         #Use the colorscaling for centroids.
                    colorscale = pl_colorscale
                    )))
    else:
        trace.append(               #If K-means is not the clustering method that was picked, then it is obviously Density.
            graph.Scatter(          #Run a Scatter Funtion for Density. It is the same for Density as it is for K-Means
                x = d_cluster[x_option],
                y = d_cluster[y_option],
                mode = "markers",
                marker = dict(
                    size = 10,
                    color = color4,
                    colorscale = pl_colorscale2
                    )))
    layout = graph.Layout(                  #make a layout using the layout function
        xaxis = dict(                   #Give the x axis it's corresponding title from titles
            title= titles[0][x_option]),
        yaxis = dict(                   #Give the y axis it's corresponding title from titles.
            title=titles[0][y_option]))
    if option == 1:             #Check to see if the Clustering method was K-Means
        trace1.append(           #Append into trace the results from the follwoing function
            graph.Scatter3d(            #Run the function Scatter3d. We use Scatter3d to make 3D scatterplots in Plotly
                #Set the Dimensions and the points underneath
                x = k_cluster[x_option],
                y = k_cluster[y_option],
                z = k_cluster[z_option],
                mode = "markers",
                marker = dict(
                    size = 10,
                    #Colorscaling, same as what was described for 2D Scatterplot
                    color = color3,
                    colorscale = pl_colorscale
                    )))
        trace1.append(
            graph.Scatter3d(                        #Append in a second element in trace to graph the centroids as a scatterplot.
                #Set the dimensions
                x = k_centroid[x_option],
                y = k_centroid[y_option],
                z = k_centroid[z_option],
                mode = "markers",
                marker = dict(
                    size = 13,                          #As shown above, centroids will be larger than other datapoints to distinguish them
                    color = color2,
                    colorscale = pl_colorscale
                    )))
    else:
        trace1.append(
            graph.Scatter3d(                        #Run the Scatter3d function to make a scatterplot of clusters made by Density
                x = d_cluster[x_option],
                y = d_cluster[y_option],
                z = d_cluster[z_option],
                mode = "markers",
                marker = dict(
                    size = 10,
                    color = color4,
                    colorscale = pl_colorscale2
                    )))
#Underneath, we make a layout for the 3D Scatterplot to give each axis a label. We make a dictionary for each axis and then run the title argument to give it
#an actual title from titles list.
    layout2 = graph.Layout(
        scene = dict(               #Make a scene. This is essential for 3D graphs because Plotly.
        xaxis = dict(
            title = titles[0][x_option]),       #Give the x-axis a title
        yaxis = dict(
            title = titles[0][y_option]),       #Give the y-axis a title
        zaxis = dict(
            title = titles[0][z_option]),)      #Give the z-axis a title
      )
    fig = graph.Figure(trace,layout)
    fig2 = graph.Figure(trace1,layout2)
    plotly.offline.plot(fig, filename = "Scatter Plot 2D.html", auto_open = True)  #Graph the 2D/3D Scatterplot
    plotly.offline.plot(fig2, filename = "Scatter Plot 3D.html", auto_open = True)
