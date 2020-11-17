import time
import random

cmp = 0


def algochooser(numbers, paint, label_comparison, label_index, algo_name, speed, searched_element):
    global cmp
    if algo_name == "Linear Search":
        label_comparison.configure(text="No. of comparisons: 0")
        label_index.configure(text="")
        linearsearch(numbers, paint, label_comparison, label_index, speed, int(searched_element))
        cmp = 0

    elif algo_name == "Binary Search":
        label_comparison.configure(text="No. of comparisons: 0")
        label_index.configure(text="")
        binarysearch(numbers, paint, label_comparison, label_index, speed, int(searched_element))
        cmp = 0


def linearsearch(number, paint, label_comparison, label_index, speed, searched_element):
    global cmp
    index = -1
    for i in range(len(number)):
        colors = []
        cmp += 1
        if number[i] == searched_element:
            for x in range(len(number)):
                if x < i:
                    colors.append("firebrick1")
                elif x == i:
                    colors.append("green2")
                else:
                    colors.append("antique white")
            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
            index = i
            break
        else:
            for x in range(len(number)):
                if x <= i:
                    colors.append("firebrick1")
                else:
                    colors.append("antique white")
            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
        time.sleep(1 / speed)
    if index == -1:
        label_index.configure(text="Element not found")
    else:
        label_index.configure(text="Element " + str(number[index]) + " found\nat index " + str(index + 1))


def binarysearch(number, paint, label_comparison, label_index, speed, searched_element):
    global cmp
    l = 0
    r = len(number) - 1
    index = -1
    colors = ["antique white"] * (len(number))
    number.sort()
    paint(colors)
    while l <= r:
        mid = l + (r - l) // 2
        colors[mid] = "SteelBlue1"
        paint(colors)
        time.sleep(1 / speed)
        if number[mid] == searched_element:
            cmp += 1
            colors[mid] = "green2"
            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
            index = mid
            break
        elif number[mid] < searched_element:
            l = mid + 1
            cmp += 1
            for i in range(mid + 1):
                colors[i] = "firebrick1"
            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
        else:
            r = mid - 1
            cmp += 1
            for i in range(mid, len(number)):
                colors[i] = "firebrick1"
            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
        time.sleep(1 / speed)
    if index == -1:
        label_index.configure(text="Element not found")
    else:
        label_index.configure(text="Element " + str(number[index]) + " found\nat index " + str(index + 1))
