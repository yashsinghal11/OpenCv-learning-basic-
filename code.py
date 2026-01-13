'''quicksort

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)
arr=[1,30,3,20,5,4,144,2]
print(quicksort(arr))'''

'''
linearsearch


def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
        
    return -1        

print(linearsearch([1,2,3,4,5,6],4))'''



'''binarysearch

def binarysearch(arr,target):
    arr=sorted(arr)
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1

        else:
            r=mid-1
    return -1

print(binarysearch([1,2,3,44,4,5,6,7],4))
'''


'''bubble sort
def bubblesort(arr):
    n=len(arr)
    for i in range(len(arr)):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubblesort([1,2,22,3,44,14,5]))'''


'''selectionsort
def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(selectionsort([1,2,22,3,44,14,5]))'''


'''insertionsort

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[i]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

print(insertionsort([1,2,22,3,44,14,5]))'''


'''mergesort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

print(merge_sort([38,27,43,3,9,82,10]))'''


'''bfsdfs
from collections import deque

graph = {
    0:[1,2],
    1:[3,4],
    2:[5],
    3:[],
    4:[5],
    5:[]
}

def bfs(start):
    visited=set()
    q=deque([start])
    while q:
        node=q.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            q.extend(graph[node])



def dfs(start,visited=set()):
    if start not in visited:
        print(start,end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs(neighbor,visited)
print(bfs(0))
print(dfs(0))'''


'''merge two ll
def merge_sorted(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1; l1 = l1.next
        else:
            tail.next = l2; l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


'''

'''
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):
    if not root:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)

    '''
'''Absraction
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
print("Abstraction Example:", dog.sound())

'''

'''Encapsultion
class Student:
    def __init__(self, name, age):
        self.__name = name   # private variable
        self.__age = age     # private variable
    
    def get_info(self):      # public method
        return f"Name: {self.__name}, Age: {self.__age}"

s = Student("Yash", 21)
print("Encapsulation Example:", s.get_info())

'''

'''Inheritance
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):   # Inherits Animal
    def speak(self):
        return "Woof!"

dog = Dog()
print("Inheritance Example:", dog.speak())

'''

'''Polymorphism

class Dog:
    def sound(self):
        return "Woof!"

class Puppy:
    def sound(self):
        return "Yip!"

# Same function name, different behavior
animals = [Dog(), Puppy()]
for a in animals:
    print("Polymorphism Example:", a.sound())
'''


'''constructor& destructor

class Demo:
    def __init__(self):
        print("Constructor called!")

    def __del__(self):
        print("Destructor called!")

d = Demo()
del d   # explicitly calling destructor

'''

def binarysearch(arr,target):
    left=0
    right=len(arr)-1
    while left<right:
        mid=len(arr)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

print(binarysearch([1,22,33,44],22))