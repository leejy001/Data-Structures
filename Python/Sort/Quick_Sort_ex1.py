from tkinter import *

def qSort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low+high)//2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low+1, high-1

    mid = low

    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

def quickSort(arr):
    qSort(arr, 0, len(arr)-1)

window = Tk()
window.geometry("480x720")
photo = PhotoImage(file = 'filename.gif')

photoArray = []
h = photo.height()
w = photo.width()
for i in range(w):
    for k in range(h):
        r, g, b = photo.get(i, k)
        value = (r+g+b)//3
        photoArray.append(value)

dataArray = photoArray[:]
quickSort(dataArray)
midValue = dataArray[h*w//2]

for i in range(len(photoArray)):
    if photoArray[i] <= midValue:
        photoArray[i] = 0
    else:
        photoArray[i] = 255

pos = 0
for i in range(w):
    for k in range(h):
        r = g = b = photoArray[pos]
        pos += 1
        photo.put("#%02x%02x%02x " % (r, g, b), (i, k))

paper = Label(window, image=photo)
paper.pack(expand=1, anchor=CENTER)
window.mainloop()