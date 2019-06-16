import Data_Analysis_Lib

#dataperson = [[1,10],[2,10],[10,10],[500,1000],[5,10],[600,1000],[5000,1000]]
file = "C:\Users\Owner\Desktop\My_Programs\Data_Analysis\Data_Analysis_Complete_Library\Book1.csv"
Label,Data,category_legend = Data_Analysis_Lib.fileinput(file)
plot = True
Data_Analysis_Lib.density_and_anomaly (Data,Label,5,plot,2,[1,2,3])
