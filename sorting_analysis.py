import random
import timeit
from typing import List


# Алгоритм вставками
def insertion_sort(arr: List[int]) -> List[int]:
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Алгоритм злиттям
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result


# Вбудований Timsort
def timsort(arr: List[int]) -> List[int]:
    return sorted(arr)


def run_benchmarks():
    sizes = [100, 1000, 5000]
    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]
        print(f"\n🧪 Тестування для {size} елементів:")

        t_insert = timeit.timeit(lambda: insertion_sort(data), number=1)
        t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
        t_tim = timeit.timeit(lambda: timsort(data), number=1)

        print(f"Вставками: {t_insert:.5f} с")
        print(f"Злиттям:   {t_merge:.5f} с")
        print(f"Timsort:   {t_tim:.5f} с")


# Додаткове завдання: merge_k_lists
import heapq


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
    return result


if __name__ == "__main__":
    run_benchmarks()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(lists)
    print("\n🧩 Результат merge_k_lists:", merged)
