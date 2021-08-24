"""集合

@詳見： https://www.w3schools.com/python/python_sets.asp
@詳見： https://docs.python.org/3.7/tutorial/datastructures.html#sets

集合通常是由無序的且不需索引的內容所組成，
Python 使用大括號來指派集合變數，
集合物件也支援數學操作，例如：聯集、交集、差集、對稱差
"""


def test_sets():
    """集合"""
    fruits_set = {"apple", "banana", "cherry"}

    assert isinstance(fruits_set, set)

    # 您也可以使用 set() 建構函式來創建集合（注意範例中有兩個小括號）
    fruits_set_via_constructor = set(("apple", "banana", "cherry"))

    assert isinstance(fruits_set_via_constructor, set)


def test_set_methods():
    """集合方法"""

    fruits_set = {"apple", "banana", "cherry"}

    # 您可以使用 in 陳述式來檢查該內容是否存在於集合中
    assert "apple" in fruits_set
    assert "pineapple" not in fruits_set

    # len() 方法將會回傳集合長度
    assert len(fruits_set) == 3

    # 您可以使用 add() 物件方法來新增內容至集合中
    fruits_set.add("pineapple")
    assert "pineapple" in fruits_set
    assert len(fruits_set) == 4

    # 您可以使用 remove() 物件方法在集合中移除內容
    fruits_set.remove("pineapple")
    assert "pineapple" not in fruits_set
    assert len(fruits_set) == 3

    # 利用集合操作來展示如何從兩個字串中找出所有出現過的字母（不重複，因為集合中的內容具有唯一性）
    first_char_set = set('abracadabra')
    second_char_set = set('alacazam')

    assert first_char_set == {'a', 'r', 'b', 'c', 'd'}   # 在第一個字串中出現過的字母（不重複）
    assert second_char_set == {'a', 'l', 'c', 'z', 'm'}  # 在第二個字串中出現過的字母（不重複）

    # 在第一個字串出現過但不在第二個字串出現過的字母
    assert first_char_set - second_char_set == {'r', 'b', 'd'}

    # 在這兩個字串中任何一個字串出現過或兩個字串都出現過的字母（或 運算子）
    assert first_char_set | second_char_set == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

    # 在這兩個字串中都出現過的字母（且 運算子）
    assert first_char_set & second_char_set == {'a', 'c'}

    # 在這兩個字串中任何一個字串出現過但不同時出現在這兩個字串中的字母（互斥或 運算子）
    assert first_char_set ^ second_char_set == {'r', 'd', 'b', 'm', 'z', 'l'}

    # 與列表構建類似，Python 也支援集合構建（Set Comprehensions）
    word = {char for char in 'abracadabra' if char not in 'abc'}
    assert word == {'r', 'd'}
