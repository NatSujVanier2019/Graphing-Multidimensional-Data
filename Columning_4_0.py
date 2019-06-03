from random import uniform,randint
##Clusters = [[['1.0', '2.0', '3.0', '543', '12', '7', '45'], ['2.2', '2.3', '5.8', '76', '21', '5', '654'], ['5.2', '2.8', '8.0', '43', '76', '4', '86']]]
##Clusters = [[[1,2,3]],[[10,20,30]],[[100,200,300]]]

def colcol (Clusters,Noise):
    Columns = []
    Colours = []
    column = -1

##    print ("Clusters: ",Clusters)
##    print ("Clusters Length:",len(Clusters))

    def colgen (Clusters,Noise,Colours):
        for i in range(0,len(Clusters)):
            color_string = "rgb("
            for w in range (0,3):
                if w != 2:
                    color_string +=((str(randint(0,255)) + ","))
                else:
                    color_string +=((str(randint(0,255)) + ")"))
            if i==0:
##                if i==(len(Clusters)-1):
##                    Colours.append(1)
##    ##                print ("Appended 1: ",Colours)
##                else:
                color_val = 0
    ##                print ("Appended 0: ",Colours)
            elif i==(len(Clusters)-1):
                color_val = 1
    ##            print ("Appended 1: ",Colours)
            else:
                color_val = random.uniform(0,1)
                for colour in Colours:
                    while color_val == colour:
                        color_val = random.uniform(0,1)
            for j in (Clusters[i]):
                j.append(color_val)
            Colours.append([color_val,color_string])
    ##            print ("Appended random: ",Colours)
        return Colours

    ##print (colgen(Clusters,Colours))
    Colours = colgen(Clusters,Noise,Colours)


    for corit in range (0,len(Clusters[0][0])):
        column+=1
        Columns.append([])
        print ("Columns: ",Columns)
        for cluster in range (0,len(Clusters)):
            for row in Clusters[cluster]:
                for cor in range (0,len(row)):
                    Columns[column].append(row[cor])
                    row[cor] = "del"
                    break

        for icluster in range (len(Clusters)-1,-1,-1):
            for icount in range (len(Clusters[icluster])-1,-1,-1):
                for icor in range (len(Clusters[icluster][icount])-1,-1,-1):
                    if Clusters[icluster][icount][icor]=="del":
                        Clusters[icluster][icount].remove(Clusters[icluster][icount][icor])

    color_list3 = list(Columns[(len(Columns) - 1)])
    Columns.pop()
    print ("Final Columns: ",Columns)
    print ("Colours: ",Colours)
    return Columns,color_list3,Colours  
    
