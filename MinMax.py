import cv2
img=cv2.imread("lenagray.jpg",0)
def minMaxMat(mat):
    min=255
    max=0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mat[i,j]>max:
                max=mat[i,j]
            if mat[i,j]<min:
                min=mat[i,j]
    return (min,max)
print(minMaxMat(img))