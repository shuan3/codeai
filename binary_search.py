def binary_search(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        middle=(left+right)//2
        if array[middle]==target:
            return middle
        elif array[middle]<target:
            left=middle+1
        else:
            right=middle-1
    return -1

def binary_search(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        middle=(left+right)//2
        if array[middle]==target:
            return middle
        if array[left]<array[middle]:
            if array[left]<=target<array[middle]:
                right=middle-1
            else:
                left=middle+1
        else:
            if target<=array[right] and target>array[middle]:
                left=middle+1
            else:
                right=middle-1
    return -1

def recursive_binary_search(array,target,left,right):
    if left>right:
        return -1
    middle=(left+right)//2
    if array[middle]==target:
        return middle
    elif array[middle]<target:
        return recursive_binary_search(array,target,middle+1,right)
    else:
        return recursive_binary_search(array,target,left,middle-1)