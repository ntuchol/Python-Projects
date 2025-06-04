import heapq

def find_largest_in_max_heap(heap_list):
   if not heap_list:
    return None
  return heap_list[0]

max_heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
largest_element = find_largest_in_max_heap(max_heap)
print(f"The largest element in the max-heap is: {largest_element}")

min_heap = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
heapq.heapify(min_heap)

def find_largest_in_min_heap(heap_list):

    if not heap_list:
        return None
    return max(heap_list[len(heap_list)//2:]) 

largest_element = find_largest_in_min_heap(min_heap)
print(f"The largest element in the min-heap is: {largest_element}")