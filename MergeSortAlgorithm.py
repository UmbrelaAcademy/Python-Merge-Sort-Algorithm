def Divide(arr):
    print("received->",(arr))
    # if array has no element, return
    # if array has only 1 emelent, return
    if(len(arr)<=1):
        print("out->",(arr))
        return arr
    # if array has more than 1 elements, divide array into two halves
    else:
        mid = int(len(arr)/2)
        print("lefty->",arr[:mid])
        print("right->",arr[mid:])

    # until array have only one element, Divide it recursively
        left = Divide(arr[:mid])    # arr[:mid] and arr[mid:] returns new arrays
        right = Divide(arr[mid:])   # so 'arr' is not required after this step
    # Divide array will call itself recursively until 1 element is returned from both halves
    # Merge those halves
        Merge(left, right, arr)     # left and right are proper instances of arrays, we can use our actual array 'arr' and manipulate it
        print("afterMerge->",(arr))
        return arr

    
    # Receive Two Halves to merge, for first iteration, this will receive single element in each array
    # compare the Two array and sort those
    # we can return merged array from this function by using 'return' statement
    # but for better utilization we using our actual array as output parameter
    # because for return we need to create a new array
    # we have already divided our actual array into left and right arrays using slice operation, so our main array 'arr' is useless
def Merge(left, right, merged):
    i = j = k = 0
    lenLeft = len(left)
    lenRight = len(right)
    print("Merge(L)->",left)
    print("Merge(R)->",right)
    # both arrays are already sorted, so only need to compare 1st elements of each array and put them in sorted array
    # either 1st element of 'left' or 1st element of 'right' array needs to be in sorted array, thats why its complexity is: n Log(n)
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
    # maybe all elements of 'right' were greater than 1st element of 'left' array
    # so copy all/remaining elements of left in merged, as they are already sorted
    while(i<lenLeft):        
        merged[k] = left[i]
        k+=1
        i+=1
    # (copy all/remaining elements of 'right' array if needed)
    while(j<lenRight):
        merged[k]=right[j]
        k+=1
        j+=1

    print("(L)+(R)->",merged)

arr = [12,1,2,14,15,16,13,3,4,5,17,6,10,9,8,7,11]
print("final->",Divide(arr))
