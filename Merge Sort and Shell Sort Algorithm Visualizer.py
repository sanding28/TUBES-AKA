from tkinter import *
import random
import time

root = Tk()
root.title('Merge Sort and Shell Sort Algorithm Visualizer')
root.maxsize(1080,800)
root.config (bg='gray10')

data0 = []
data1 = []
time_start = time.time()

#merge sort

def merge_sort(data,drawArr,canvas):
    global time_start
    time_start = time.time()
    mergeSort(data)

def mergeSort(data):
    canvas = canvas0
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              data[k] = left[i]
              drawArr(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))], canvas)
              i += 1
            else:
                data[k] = right[j]
                drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            drawArr(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))], canvas)
            i += 1
            k += 1

        while j < len(right):
            data[k]=right[j]
            drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
            j += 1
            k += 1
    updateTime(timer1,time_start)
    drawArr(data, ['green' for x in range(len(data))], canvas)

#Shell Sort
def shell_sort(data,drawArr,canvas):
    global time_start
    time_start = time.time()    
    gap = len(data) // 2

    while gap > 0:
        for i in range(gap,len(data)):
            temp = data[i]
            j = i
            while j >= gap and data[j-gap] > temp:
                data[j] = data[j-gap]
                drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
                updateTime(timer2,time_start)
                j -= gap
            data[j] = temp
        gap //= 2
    drawArr(data, ['green' for x in range(len(data))], canvas)

# Functions
def updateTime(timeLabel,startTime):
    timeLabel.config(text=time.time() - time_start)

def drawArr(data, color, canvas):
    canvas.delete("all")
    c_width = 336
    c_height = 380
    x_width = c_width / (len(data) + 1)
    offset = 10
    space = 5
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        
        x0 = i * x_width + offset + space
        y0 = c_height - height * 336
       
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i], outline=color[i])

    root.update_idletasks()

def generate():
    global data0
    global data1
    data0 = []  
    data1 = []
    
    size = int(sizeInput.get())
    
    for _ in range(size):
        data0.append(random.randrange(5, 100))
    data1[:] = data0[:]
    drawArr(data0,['snow' for x in range(len(data0))],canvas0)
    drawArr(data1,['snow' for x in range(len(data1))],canvas1)

def visualize():
    global data0
    global data1

    merge_sort(data0, drawArr, canvas0)
    shell_sort(data1, drawArr, canvas1)


# layout

canvas0 = Canvas(root, width=350, height=380, bg='gold4')
canvas0.grid(row=3, column=0, padx=10, pady=10)

canvas1 = Canvas(root, width=350, height=380, bg='gold4')
canvas1.grid(row=3, column=1, padx=10, pady=10)

Label(root,text="Merge Sort",fg='gold3', bg='gray6').grid(row=2,column=0)
Label(root,text="Shell Sort",fg='gold3', bg='gray6').grid(row=2,column=1)

labelFrame1 = Frame(root, width = 850, height = 50, bg='gray6')
labelFrame1.grid(row= 4,column=0, padx=20,pady=20)
Label(labelFrame1,text="Running Time :",fg='gold3', bg='gray6').grid(row=1,column=0)
Label(labelFrame1,text="seconds",fg='gold3', bg='gray6').grid(row=1,column=2)

timer1 = Label(labelFrame1, text="               0.0              ",fg='gold3', bg='gray6')
timer1.grid(row=1, column=1,pady=20)

labelFrame2 = Frame(root, width = 850, height = 50, bg='gray6')
labelFrame2.grid(row= 4,column=1, padx=20,pady=10)
Label(labelFrame2,text="Running Time :",fg='gold3', bg='gray6').grid(row=1,column=1)
Label(labelFrame2,text="seconds",fg='gold3', bg='gray6').grid(row=1,column=3)

timer2 = Label(labelFrame2, text="               0.0              ", fg='gold3', bg='gray6')
timer2.grid(row=1, column=2,pady=20)

# Buttons
buttonsFrame = Frame(root, width = 900, height = 500, bg ='gray6')
buttonsFrame.grid(row = 0, column=1, padx =10, pady=10)

Label(buttonsFrame, text="Input n :", fg = 'wheat1', bg= 'gray3').grid(row=0, column=0, padx=5,pady=5)

sizeInput = Entry(buttonsFrame)
sizeInput.grid(row=0, column=1, padx=10,pady=5)

genButton =Button(buttonsFrame, text="Generate", fg = 'black', bg = 'gold3', command=generate)
genButton.grid(row=0, column=2, padx=5, pady=5)

startButton = Button(buttonsFrame, text="Visualize", fg = 'black', bg = 'gold3', command=visualize)
startButton.grid(row=0, column=3, padx=5, pady=5)

# Guide

labelguide = Frame(root, width = 500, height = 50, bg='gray3')
labelguide.grid(row= 0,column=0, padx=20,pady=20)
Label(labelguide,text="Cara Menggunakan Merge Sort and Shell Sort Algorithm Visualizer   ",fg='wheat1', bg='black').grid(row=0,column=0)
Label(labelguide,text="1. Masukkan angka integer ke dalam input box            ",fg='wheat1', bg='gray3').grid(row=1,column=0)
Label(labelguide,text="2. Klik 'Generate' untuk membuat data array acak        ",fg='wheat1', bg='gray3').grid(row=2,column=0)
Label(labelguide,text="3. Klik 'Visualize' untuk memulai visualisasi algoritma sort ",fg='wheat1', bg='gray3').grid(row=3,column=0)

root.mainloop()