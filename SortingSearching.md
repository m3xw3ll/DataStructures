# Table of Content

- [Binary Search](#binary-search)
- [Bucket Sort](#bucket-sort)
- [Bubble Sort](#bubble-sort)
- [Counting Sort](#counting-sort)
- [Heap Sort](#heap-sort)
- [Insertion Sort](#insertion-sort)
- [Linear Search](#linear-search)
- [Merge Sort](#merge-sort)
- [Quick Sort](#quick-sort)
- [Radix Sort](#radix-sort)
- [Selection Sort](#selection-sort)
- [Shell Sort](#shell-sort)

---

## Binary Search
```python
def binarySearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return -1

if __name__ == '__main__':
    data = [2, 4, 0, 1, 9]
    x = 1
    print(binarySearch(data, x, 0, len(data) - 1))
```


## Bucket Sort
```python
def bucketSort(array):
    bucket = []
    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


if __name__ == '__main__':
    data = [.42, .32, .33, .52, .37, .47, .51]
    print(bucketSort(data))
```


## Bubble Sort
```python
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    print(bubbleSort(data))
```


## Counting Sort
```python
def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
        
    return array


if __name__ == '__main__':
    data = [4, 2, 2, 8, 3, 3, 1]
    print(countingSort(data))
```

## Heap Sort
```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == '__main__':
    data = [1, 12, 9, 5, 6, 10]
    print(heapSort(data))
```


## Insertion Sort
```python
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    print(insertionSort(data))
```


## Linear Search
```python
def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

if __name__ == '__main__':
    data = [2, 4, 0, 1, 9]
    x = 1
    print(linearSearch(data, len(data), x))
```


## Merge Sort
```python
def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    print(mergeSort(data))
```


## Quick Sort
```python
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    return array


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    print(quickSort(data, 0, len(data) -1))
```

## Radix Sort
```python
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
    return array


if __name__ == '__main__':
    data = [4, 2, 2, 8, 3, 3, 1]
    print(radixSort(data))
```


## Selection Sort
```python
def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    return array

if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    print(selectionSort(data, len(data)))
```


## Shell Sort
```python
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    return array

if __name__ == '__main__':
    data = [1, 12, 9, 5, 6, 10]
    print(shellSort(data, len(data)))
```