from random import *

def absorandom2d(low, high,length):
    return [randint(low,high) for i in range(length)]

def absorandom3d(low,high,length,breadth):
    return [[randint(low,high) for i in range(length)] for j in range(breadth)]

def gen_row(breadth,arr, variance):
    for i in range(1,breadth):
        arr.append(arr[i-1]+randint(-variance,variance))
    return arr

def lessrandom3d(length, breadth):
    arr=gen_row(breadth,[0],4)
    for i in range(breadth):                        #mostly suited to smaller arrays... 500x500?
        arr[i]=gen_row(length,[arr[i]],1)
    return arr


def lessrandom3d_ver2(length,breadth, variance):
    arr=[gen_row(breadth,[0],variance)]
    for i in range(1,length):
        arr2=[]
        for j in range(breadth):
            arr2.append(arr[i-1][j]+randint(-variance*5//8,variance))
            if (arr2[j]-arr2[j-1]>variance) or (arr2[j-1]-arr2[j]>variance):
                arr2[j]=(arr2[j-1]+arr[i-1][j])//2
        arr.append(arr2)
    return arr

def pretty_print_1(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print("{:>3}".format(arr[i][j]), end='')
        print()

def pretty_print_2(arr):
    for i in range(1000):
        for j in range(132):
            if arr[i][j]<-15:
                print(" ", end='')
            elif arr[i][j]<-5:
                print("-", end='')
            elif arr[i][j]<5:
                print("=", end='')
            elif arr[i][j]<15:
                print("&", end='')
            else:
                print("@", end='')
        print()
