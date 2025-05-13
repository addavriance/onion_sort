def onion_sort(arr):
    """
    Onion Sort - сортировка, работающая путем постепенного "отслаивания" крайних элементов.
    На каждой итерации находим минимальный и максимальный элементы в текущем срезе
    и помещаем их на края, затем сужаем диапазон поиска.

    Сложность: O(n²) в худшем случае, как и Selection Sort
    """
    a = arr.copy()
    left = 0
    right = len(a) - 1

    while left < right:
        # Найдем индексы min и max в текущем срезе
        current_slice = a[left:right + 1]

        min_val, max_val = min(current_slice), max(current_slice)
        min_idx, max_idx = a.index(min_val, left, right + 1), a.index(max_val, left, right + 1)

        # Поставим минимальный элемент на левый край
        a[left], a[min_idx] = a[min_idx], a[left]

        # Если максимальный элемент был на позиции left, после обмена он теперь в min_idx
        if max_idx == left:
            max_idx = min_idx

        # Поставим максимальный элемент на правый край
        a[right], a[max_idx] = a[max_idx], a[right]

        # "Отслоим" крайние элементы
        left += 1
        right -= 1

    return a
