import time
import random

cmp = 0
TYPE = 0


def algochooser(numbers, paint, label_comparison, something, TYPE_OF_DRAW, speed):
    global cmp, TYPE
    TYPE = TYPE_OF_DRAW
    if something == "Bubble Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        bubblesort(numbers, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Selection Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        selectionsort(numbers, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Insertion Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        insertionsort(numbers, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Merge Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        mergesort(numbers, 0, len(numbers), paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Heap Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        heapsort(numbers, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Quick Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        quicksort(numbers, 0, len(numbers) - 1, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Shell Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        shellsort(numbers, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0

    elif something == "Radix Sort":
        label_comparison.configure(text="No. of comparisons: 0")
        radixsort(numbers, paint, speed)
        if TYPE == 0:
            paint(["lawn green"] * len(numbers))
        cmp = 0


def bubblesort(number, paint, label_comparison, speed):
    global cmp, TYPE
    is_sort = False
    colors = []
    for i in range(len(number) - 1):
        is_sort = True
        for j in range(len(number) - 1 - i):
            if (number[j] > number[j + 1]):
                is_sort = False
                number[j], number[j + 1] = number[j + 1], number[j]
                time.sleep(1 / speed)
            cmp += 1
            if TYPE == 0:
                colors = ["#cc0000" if x == number[j] or x == number[j + 1] else "antique white" for x in number]
            else:
                colors = [((int)(x * 360) / 950) for x in number]
            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
        if is_sort:
            break
        time.sleep(1 / speed)


def selectionsort(number, paint, label_comparison, speed):
    global cmp
    colors = []
    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            if (number[i] > number[j]):
                number[i], number[j] = number[j], number[i]
            time.sleep(1 / speed)
            cmp += 1
            if TYPE == 0:
                colors = ["#cc0000" if x == number[j] else "antique white" if x != number[i] else "green" for x in number]
            else:
                colors = [((int)(x * 360) / 950) for x in number]
            paint(colors)
            label_comparison.configure(text="No. of comparisons: " + str(cmp))


def insertionsort(number, paint, label_comparison, speed):
    global cmp, TYPE
    colors = []
    for i in range(1, len(number)):
        current = number[i]
        y = i - 1
        while (y >= 0 and number[y] > current):
            number[y + 1] = number[y]
            y -= 1
            cmp += 1
            # ----------------------------------------------------------
            if TYPE == 0:
                for gh in range(len(number)):
                    if y == gh:
                        colors.append("#cc0000")
                    elif gh == i:
                        colors.append("green")
                    else:
                        colors.append("antique white")
            else:
                colors = [((int)(x * 360) / 950) for x in number]
            time.sleep(1 / speed)
            paint(colors)
            colors = []
            label_comparison.configure(text="No. of comparisons: " + str(cmp))
            # ------------------------------------------------------------
        number[y + 1] = current
        cmp += 1
        # -----------------------------------------------------------
        label_comparison.configure(text="No. of comparisons: " + str(cmp))


def mergesort(number, left, right, paint, label_comparison, speed):
    if left < right:
        middle = (left + right) // 2
        mergesort(number, left, middle, paint, label_comparison, speed)
        mergesort(number, middle + 1, right, paint, label_comparison, speed)
        merge(number, left, middle, right, paint, label_comparison, speed)


def merge(number, left, middle, right, paint, label_comparison, speed):
    global cmp, TYPE
    si = fi = 0
    colors = []
    firstlist = number[left:middle + 1]
    secondlist = number[middle + 1:right + 1]
    for ai in range(left, right + 1):
        if (fi < len(firstlist) and si < len(secondlist)):
            if (firstlist[fi] < secondlist[si]):
                number[ai] = firstlist[fi]
                fi += 1
                cmp += 1
            else:
                number[ai] = secondlist[si]
                si += 1
        elif (fi < len(firstlist)):
            number[ai] = firstlist[fi]
            fi += 1
        elif (si < len(secondlist)):
            number[ai] = secondlist[si]
            si += 1
        if TYPE == 0:
            for x in range(len(number)):
                if x > middle and x <= right:
                    colors.append("yellow")
                elif x >= left and x <= middle:
                    colors.append("teal")
                else:
                    colors.append("antique white")
        else:
            colors = [((int)(x * 360) / 950) for x in number]
        paint(colors)
        time.sleep(1 / speed)
        label_comparison.configure(text="No. of comparisons: " + str(cmp))


def heapsort(number, paint, label_comparison, speed):
    global cmp, TYPE
    n = len(number) // 2
    colors = []

    for i in range(n-1, -1, -1):
        heapify(number, len(number), i, paint, label_comparison)

    for i in range(len(number) - 1, 0, -1):
        number[i], number[0] = number[0], number[i]
        if TYPE == 0:
            colors = ["green" if x == number[i] else "antique white" for x in number]
        else:
            colors = [((int)(x * 360) / 950) for x in number]
        paint(colors)
        time.sleep(1 / speed)
        # ----------------------------------------------------------------
        heapify(number, i, 0, paint, label_comparison)


def heapify(number, limit, parent, paint, label_comparison):
    global cmp
    colors = []
    largest = parent
    left = 2 * parent + 1
    right = 2 * parent + 2

    if (left < limit and number[left] > number[parent]):
        largest = left
    cmp += 1
    if (right < limit and number[right] > number[largest]):
        largest = right
    cmp += 1
    if (largest != parent):
        number[largest], number[parent] = number[parent], number[largest]
        if TYPE == 0:
            for i in range(len(number)):
                if number[i]==parent:
                    colors.append("yellow")
                else:
                    colors.append("antique white")
        else:
            colors = [((int)(x * 360) / 950) for x in number]
        paint(colors)
        label_comparison.configure(text="No. of comparisons: " + str(cmp))
        # --------------------------------------------------------------------------
        heapify(number, limit, largest, paint, label_comparison)


def quicksort(number, left, right, paint, label_comparison, speed):
    color = []
    if (left < right):
        mid = partition(number, left, right, paint, label_comparison, speed)
        quicksort(number, left, mid - 1, paint, label_comparison, speed)
        quicksort(number, mid + 1, right, paint, label_comparison, speed)


def partition(number, low, high, paint, label_comparison, speed):
    global cmp, TYPE
    tracker = low
    pivot = number[high]
    color = []
    if TYPE == 0:
        for i in range(len(number)):
            if i == low and i == high - 1:
                color.append("#cc0000")
            elif i == high:
                color.append("yellow")
            else:
                color.append("antique white")
    else:
        color = [((int)(x * 360) / 950) for x in number]
    paint(color)
    label_comparison.configure(text="No. of comparisons: " + str(cmp))
    for i in range(low, high, 1):
        if number[i] <= pivot:
            number[i], number[tracker] = number[tracker], number[i]
            tracker += 1
            color = []
        time.sleep(1 / speed)
        cmp += 1
        if TYPE == 0:
            for i in range(len(number)):
                if i == low or i == high - 1:
                    color.append("#cc0000")
                elif i == high:
                    color.append("yellow")
                else:
                    color.append("antique white")
        else:
            color = [((int)(x * 360) / 950) for x in number]
        paint(color)
        label_comparison.configure(text="No. of comparisons: " + str(cmp))
    number[tracker], number[high] = number[high], number[tracker]
    label_comparison.configure(text="No. of comparisons: " + str(cmp))
    return tracker


def shellsort(number, paint, label_comparison, speed):
    global cmp, TYPE
    colors = []
    length = len(number)
    gap = length // 2
    while gap > 0:
        for x_sort in range(gap, length):
            j = x_sort - gap
            if TYPE == 0:
                colors = ["#cc0000" if xy == j + gap or xy ==
                                       j else "antique white" for xy in range(len(number))]
            else:
                colors = [((int)(x * 360) / 950) for x in number]
            paint(colors)
            while j >= 0:
                if (number[j + gap] < number[j]):
                    number[j + gap], number[j] = number[j], number[j + gap]
                else:
                    break
                cmp += 1
                if TYPE == 0:
                    colors = ["#cc0000" if xy == j + gap or xy ==
                                           j else "antique white" for xy in range(len(number))]
                else:
                    colors = [((int)(x * 360) / 950) for x in number]
                paint(colors)
                label_comparison.configure(text="No. of comparisons: " + str(cmp))
                # --------------------------------------------------------------------------------------------------
                j -= gap
            time.sleep(1 / speed)
        gap //= 2


def countsort(number, exp, paint):
    global TYPE
    colors = []
    count = [0] * 10
    temp = [0] * len(number)
    for x in range(len(number)):
        count[(number[x] // exp) % 10] += 1

    for y in range(1, len(count)):
        count[y] += count[y - 1]
    for z in range(len(number) - 1, -1, -1):
        index = count[(number[z] // exp) % 10]
        temp[index - 1] = number[z]
        count[(number[z] // exp) % 10] -= 1
    for w in range(len(temp)):
        number[w] = temp[w]
    if TYPE == 0:
        colors = ["antique white" for h in number]
    else:
        colors = [((int)(x * 360) / 950) for x in number]
    paint(colors)


def radixsort(number, paint, speed):
    global TYPE
    colors = []
    maximum = max(number)
    exp = 1
    while (maximum // exp >= 1):
        countsort(number, exp, paint)
        if TYPE == 0:
            colors = ["antique white" for h in number]
        else:
            colors = [((int)(x * 360) / 950) for x in number]
        paint(colors)
        time.sleep(1 / speed)
        exp *= 10
