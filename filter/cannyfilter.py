import cv2


def cannyfilter(road: str):

    img = cv2.imread(road,0)
    h, w = img.shape[:2] 
    edges = cv2.Canny(img,100,100)
    
    cv2.imshow("ss", edges)
    cv2.waitKey()
    return(edges)
    



        


    

