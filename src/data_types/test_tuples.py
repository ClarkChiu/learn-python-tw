"""元組

@詳見： https://www.w3schools.com/python/python_tuples.asp
@詳見： https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

元組通常是由已排序且不改變的內容所組成的Python 使用小括號來指派元組資料類型

元組資料類型有以下特性：
- 您不能夠改變元組內的元素內容
- 您不能夠移除元組內的元素
"""

import pytest


def test_tuples():
    """元組"""
    fruits_tuple = ("apple", "banana", "cherry")

    assert isinstance(fruits_tuple, tuple)
    assert fruits_tuple[0] == "apple"
    assert fruits_tuple[1] == "banana"
    assert fruits_tuple[2] == "cherry"

    # 您不能夠改變元組內的元素內容
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        fruits_tuple[0] = "pineapple"

    # 您可以使用 tuple() 建構函式來創建元組（注意範例中有兩個小括號）
    # len() 也支援傳入元組物件
    fruits_tuple_via_constructor = tuple(("apple", "banana", "cherry"))
    assert isinstance(fruits_tuple_via_constructor, tuple)
    assert len(fruits_tuple_via_constructor) == 3

    # 您也可以省略小括號
    another_tuple = 12345, 54321, 'hello!'
    assert another_tuple == (12345, 54321, 'hello!')

    # 元組也可以是巢狀的
    nested_tuple = another_tuple, (1, 2, 3, 4, 5)
    assert nested_tuple == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

    # 如您所見，輸出的元組總是被小括號括住
    # 如此一來，巢狀元組才可以被正確解析
    # 當然您在創建元組時可以省略小括號（不建議）
    # 雖然您無法修改元組內單獨的元素內容，但您可以在元組中加入可變的物件，例如：串列

    # 在元組僅包含 0 或 1 個元素時，指派的語法會有一些奇特

    # 空的元組直接由小括號所構成
    # 包含 1 個元素的元組由數值加上後面的逗號所構成（不能僅用小括號括住某個數值來做指派）
    empty_tuple = ()
    # pylint: disable=len-as-condition
    assert len(empty_tuple) == 0

    # pylint: disable=trailing-comma-tuple
    singleton_tuple = 'hello',  # <-- 注意結尾的逗號
    assert len(singleton_tuple) == 1
    assert singleton_tuple == ('hello',)

    # 以下範例稱為元組打包（Tuple packing）
    packed_tuple = 12345, 54321, 'hello!'

    # 反轉操作也是可以做到的
    first_tuple_number, second_tuple_number, third_tuple_string = packed_tuple
    assert first_tuple_number == 12345
    assert second_tuple_number == 54321
    assert third_tuple_string == 'hello!'

    # 上方這個動作被稱為序列拆解，即等號左右邊的內容是可以一比一的對應及指派
    # 多重指派即是透過這兩個特性（元組打包、序列拆解）組合應用而成。
    # 使用元組來交換兩個變數內容，這個做法可以不用像傳統做法需要額外指派一個變數暫時儲存資料
    first_number = 123
    second_number = 456
    first_number, second_number = second_number, first_number

    assert first_number == 456
    assert second_number == 123
