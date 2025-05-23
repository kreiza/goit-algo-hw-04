# Аналіз алгоритмів сортування у Python

## 🔍 Алгоритми:
- **Insertion Sort**: O(n²), працює добре лише на малих/майже відсортованих списках.
- **Merge Sort**: O(n log n), стабільний і рекурсивний, але потребує додаткову пам’ять.
- **Timsort**: Гібрид злиття та вставок, використовується у `sorted()`/`.sort()`.

## ⚡ Емпіричні результати

Тестування на списках розміру 100, 1000, 5000:

| Розмір | Insertion Sort | Merge Sort | Timsort |
|--------|----------------|------------|---------|
| 100    |   0.0015 с     | 0.0018 с   | 0.0004 с|
| 1000   |   0.098 с      | 0.013 с    | 0.002 с |
| 5000   |   >1.5 с       | 0.077 с    | 0.006 с |

## 💡 Висновок

Timsort використовує переваги вставок для маленьких підмасивів та злиття для великих. Це робить його **набагато ефективнішим** за окрему реалізацію злиття чи вставок, що підтверджено як теоретично, так і на практиці.

У звичайному програмуванні **завжди краще використовувати вбудовану `sorted()`**, ніж реалізовувати сортування вручну.

## 🧩 Додаткове

Функція `merge_k_lists` ефективно об'єднує k відсортованих списків за допомогою мін-купи з модуля `heapq`.
