def arraySeach(arr,n,key):
    s=0
    e=n

    input("the index number is:")
    while(s<=e):
        mid=(s+e)/2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>key):
            e=mid-1
        else:
            s=mid+1
    return -1    



n=int(input("enter the size of array"))

arr=[n]
for i in range(0,n,1):
    input(arr[i])    
key=int(input("enter the elemate:"))

arraySeach(arr,n,key)



