import time
import random
from bubble_sort import bubble_sort

bubble_sort_times = []
merge_sort_times = []

for i in range(100):
    test_string = ''.join(['1234567890qwertyuiopasdfghjklzxcvbnm'[random.randint(0,35)] for j in range(200)])
    print test_string
    start_time = time.clock()
    bubble_sort(test_string)
    bubble_sort_times.append(time.clock() - start_time)

    start_time = time.clock()
    sorted(test_string)
    merge_sort_times.append(time.clock() - start_time)
bubble_average = sum(bubble_sort_times) / len(bubble_sort_times)
merge_average = sum(merge_sort_times) / len(merge_sort_times)
print "Bubble Average: %f"%bubble_average
print "Merge Average: %f" %merge_average
print "Merge sort is %f times faster than bubble sort."%(bubble_average/merge_average)