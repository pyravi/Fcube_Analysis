list1=list(input("Enter the list ||"))
items=int(input("Enter the list ||"))

beg=0
end=len(list1)-1
mid=int((beg+end)/2)
while beg<=end:
    if int(list1[mid])<items:
        beg=mid+1
    elif int(list1[mid])==items:
        print("Element found at location -" +str(mid+1))
        break
    else:
        end=mid-1
    mid=int((beg+end)/2)
if beg>end:
    print("Element Not found" )
