def binarySearch(arr,key):
    length = len(arr)
    start,mid = 0,0
    end = length-1
    while start<= end :
        mid = start + (end - start)//2
        
        if arr[mid] == key :
            return mid
        elif arr[mid] < key :
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == '__main__':
    evenArray = [3,6,9,12,14,16]
    oddArray  = [2,4,6,8,10]
    
    indexEvenArray = binarySearch(evenArray,12)
    print("index of 12 is {}".format(indexEvenArray))
    
    indexOddArray = binarySearch(oddArray,30)
    print("index of 30 is {}".format(indexOddArray))
    