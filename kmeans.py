
def k_means_fit(X,centroids, n = 5):
    #get a copy of the original data
    X_data = X
    
    
    diff = 1
    j=0

    while(diff!=0):

        #creating a copy of the original dataframe
        i=1

        #iterate over each centroid point 
        for index1,row_c in centroids.iterrows():
            ED=[]

            #iterate over each data point
            for index2,row_d in X_data.iterrows():

                #calculate distance between current point and centroid
                d1=(row_c["Height"]-row_d["Height"])**2
                d2=(row_c["Weight"]-row_d["Weight"])**2
                d=np.sqrt(d1+d2)

                #append distance in a list 'ED'
                ED.append(d)

            #append distace for a centroid in original data frame
            X[i]=ED
            i=i+1

        C=[]
        for index,row in X.iterrows():

            #get distance from centroid of current data point
            min_dist=row[1]
            pos=1

            #loop to locate the closest centroid to current point
            for i in range(n):

                #if current distance is greater than that of other centroids
                if row[i+1] < min_dist:

                    #the smaller distanc becomes the minimum distance 
                    min_dist = row[i+1]
                    pos=i+1
            C.append(pos)

        #assigning the closest cluster to each data point
        X["Cluster"]=C

        #grouping each cluster by their mean value to create new centroids
        centroids_new = X.groupby(["Cluster"]).mean()[["Weight","Height"]]
        if j == 0:
            diff=1
            j=j+1

        else:
            #check if there is a difference between old and new centroids
            diff = (centroids_new['Weight'] - centroids['Weight']).sum() + (centroids_new['Height'] - centroids['Height']).sum()
            print(diff.sum())

        centroids = X.groupby(["Cluster"]).mean()[["Weight","Height"]]
        
    return X, centroids