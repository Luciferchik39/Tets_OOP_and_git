import unittest
from typing import Any, List

a = [1, 2, 3, [4, 5,], [[6], 7, 8]]


def my_fun(obj: List):
    new_list: list = []

    for element in obj:
        if not isinstance(element, list):
            new_list.append(element)
        elif isinstance(element, list):
            new_list.extend(my_fun(element))
    return new_list



class TestMyFun(unittest.TestCase):

    def test_flat_list_returns_same(self):
        """Тест: плоский список возвращается без изменений"""
        self.assertEqual(my_fun([1, 2, 3]), [1, 2, 3])

    def test_one_level_nesting(self):
        """Тест: один уровень вложенности"""
        self.assertEqual(my_fun([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_multi_level_nesting(self):
        """Тест: многоуровневая вложенность"""
        data = [1, 2, 3, [4, 5], [[6], 7, 8]]
        self.assertEqual(my_fun(data), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_deep_nesting_single_path(self):
        """Тест: глубокая вложенность с одним путем"""
        self.assertEqual(my_fun([[[[[1]]]]]), [1])

    def test_empty_list(self):
        """Тест: пустой список"""
        self.assertEqual(my_fun([]), [])

    def test_empty_nested_lists(self):
        """Тест: пустые вложенные списки"""
        self.assertEqual(my_fun([[], [[], []], 1]), [1])

    def test_preserves_order(self):
        """Тест: сохранение порядка элементов"""
        self.assertEqual(my_fun([3, [1, [2]], 4]), [3, 1, 2, 4])

    def test_mixed_types_kept_as_is(self):
        """Тест: смешанные типы данных сохраняются"""
        self.assertEqual(
            my_fun([1, ['a', [True, None]], 2.5]),
            [1, 'a', True, None, 2.5]
        )

    def test_tuple_is_not_flattened_current_behavior(self):
        """
        Тест: кортежи не разворачиваются (текущее поведение)
        Разворачиваем только списки, кортежи остаются как элементы
        """
        self.assertEqual(my_fun([1, (2, 3), [4]]), [1, (2, 3), 4])

    def test_does_not_modify_original_list(self):
        """Тест: исходный список не изменяется"""
        data = [1, [2, 3], 4]
        _ = my_fun(data)  # Вызываем функцию
        self.assertEqual(data, [1, [2, 3], 4])  # Проверяем, что оригинал не изменился

    # Дополнительные тесты для проверки граничных случаев
    def test_none_values(self):
        """Тест: значения None обрабатываются корректно"""
        self.assertEqual(my_fun([1, None, [2, None]]), [1, None, 2, None])

    def test_mixed_nesting_with_strings(self):
        """Тест: строки не разворачиваются"""
        self.assertEqual(
            my_fun(['hello', ['world', ['!']], 123]),
            ['hello', 'world', '!', 123]
        )

    def test_very_deep_nesting(self):
        """Тест: очень глубокая вложенность"""
        # Создаем список с глубиной 100
        deep_list = 1
        for _ in range(100):
            deep_list = [deep_list]
        self.assertEqual(my_fun(deep_list), [1])


if __name__ == '__main__':
    # Запускаем тесты с подробным выводом
    unittest.main(verbosity=2)