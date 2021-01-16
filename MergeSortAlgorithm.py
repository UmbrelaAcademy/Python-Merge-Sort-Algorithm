def Divide(arr):
    print("received->",(arr))
    if(len(arr)<=1):
        print("out->",(arr))
        return arr
    else:
        mid = int(len(arr)/2)
        print("lefty->",arr[:mid])
        print("right->",arr[mid:])

        left = Divide(arr[:mid])
        right = Divide(arr[mid:])

        Merge(left, right, arr)
        print("afterMerge->",(arr))
        return arr

def Merge(left, right, merged):
    i = j = k = 0
    lenLeft = len(left)
    lenRight = len(right)
    print("Merge(L)->",left)
    print("Merge(R)->",right)
    while(i<lenLeft and j<lenRight):
        #print("comparing ",left[i]," ",right[j])
        if(left[i]>=right[j]):
            merged[k] = left[i]
            k+=1
            i+=1
        else:
            merged[k]=right[j]
            k+=1
            j+=1

    while(i<lenLeft):        
        merged[k] = left[i]
        k+=1
        i+=1
    while(j<lenRight):
        merged[k]=right[j]
        k+=1
        j+=1

    print("(L)+(R)->",merged)

arr = [12,1,2,14,15,16,13,3,4,5,17,6,10,9,8,7,11]
print("final->",Divide(arr))
