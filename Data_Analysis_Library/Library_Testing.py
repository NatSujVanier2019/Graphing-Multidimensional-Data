import Data_Analysis_Lib
from os import path
#filename = path.expanduser('~'), input('enter the file location, ignoringthe wierd tuff')
#dataperson = [[1,10],[2,10],[10,10],[500,1000],[5,10],[600,1000],[5000,1000]]
Label,Data,category_legend = Data_Analysis_Lib.fileinput()
plot = True
Data_Analysis_Lib.density_and_anomaly(Data,Label,6,plot, 2, [1,2])
#Data_Analysis_Lib.k_means_clustering(Data,Label,3,plot, 2, [1,2])

