n = int(input())
arr = list(map(int, input().split()))
k=max(arr)
arr=list(dict.fromkeys(arr))//to remove duplicate element from array
arr.remove(k)
print(max(arr))//2nd highest element in array
