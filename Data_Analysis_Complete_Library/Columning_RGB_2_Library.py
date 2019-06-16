from random import uniform,randint
#from Infinite_Dimensional_Clustering_RGB_3 import clustering

#dataperson = [[1,10],[2,10],[10,10],[500,1000],[5,10],[600,1000],[5000,1000]]

#All, noise = clustering(dataperson)

def colcol (All, noise):
    Columns = []
    Colours = []
    column = -1
    taken = []

    def colgen (All,Colours):
        for i in range(0,len(All)):
            print ("Loading...")
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
##    print ()
##    print ("Colour Identifier: ", color_list3)
##    print ()
##    print ("Colour Strings: ",Colours)
    return Columns,color_list3,Colours
