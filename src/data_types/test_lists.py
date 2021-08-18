"""串列

# @詳見：https://www.learnpython.org/en/Lists
# @詳見： https://docs.python.org/3/tutorial/introduction.html
# @詳見： https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Python 提供了一些可以由多種資料類型組成的資料結構
其中最通用的即為串列，串列將資料包括於中括號中，並使用逗號進行分隔
串列可以包含不同類型的資料，但通常我們會將其拿來儲存同類型的資料
"""

import pytest


def test_list_type():
    """串列類型"""

    # 串列非常類似陣列，可以用來儲存任意類型的資料
    # 且長度沒有限制，串列可以使用非常簡單的方式來進行迭代
    # 請見以下範例
    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)

    # 像是字串（以及其他所有內建的序列資料類型），
    # 串列可以被索引和切片：
    assert squares[0] == 1  # 利用索引值回傳該位置的內容
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]  # 切片回傳新的串列

    # 所有串列的切片操作皆會回傳新的包含指定位置範圍資料的串列
    # 這表示以下範例將會回傳一個新的一摸一樣的串列
    assert squares[:] == [1, 4, 9, 16, 25]

    # 串列也支援連接的操作
    assert squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # 不像字串是不可修改的，串列是可以被修改的
    # 其可以改變內容值：
    cubes = [1, 8, 27, 65, 125]  # 這邊有個錯誤，4^4 是 64 才對
    cubes[3] = 64  # 修正這個錯誤
    assert cubes == [1, 8, 27, 64, 125]

    # 您也可以透過 append() 方法來新增內容到串列中
    cubes.append(216)     # 新增 6^3
    cubes.append(7 ** 3)  # 以及 7^3
    assert cubes == [1, 8, 27, 64, 125, 216, 343]

    # 切片指派也是可以做到的，且此操作可以改變串列的大小
    # 或是直接將其完全清除：
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # 取代部分內容
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []  # 現在直接移除它們
    assert letters == ['a', 'b', 'f', 'g']
    # 可以利用取代整個串列的方式來清空串列
    letters[:] = []
    assert letters == []

    # 串列一樣可以使用內建的 len() 函式
    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4

    # Python 也支援巢狀串列（串列中包含另一個串列）
    # 例如：
    list_of_chars = ['a', 'b', 'c']
    list_of_numbers = [1, 2, 3]
    mixed_list = [list_of_chars, list_of_numbers]
    assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]
    assert mixed_list[0] == ['a', 'b', 'c']
    assert mixed_list[0][1] == 'b'


def test_list_methods():
    """測試串列方法"""

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.append(x)
    # 新增內容到串列的最後面
    # 等同於 a[len(a):] = [x]
    fruits.append('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

    # list.remove(x)
    # 移除串列中第一個出現的目標內容
    # 若目標內容不存在於串列中，則會產生 ValueError 錯誤
    fruits.remove('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    with pytest.raises(Exception):
        fruits.remove('not existing element')

    # list.insert(i, x)
    # 插入目標內容至指定位置，第一個傳入引數是索引值，表示在該索引值前插入目標內容
    # 因此 a.insert(0, x) 表示在起始點插入目標內容
    # a.insert(len(a), x) 等同於 a.append(x)
    fruits.insert(0, 'grape')
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.index(x[, start[, end]])
    # 從索引值 0 開始尋找目標內容 x（預設情況）
    # 若沒有找到目標內容的話，會產生 ValueError 錯誤
    # 也可以傳入起始搜尋位置和結束搜尋位置，就像是使用切片時一樣，藉以來限制搜尋範圍
    # 回傳的索引值是基於位置 0 而非這個傳入的搜尋位置
    assert fruits.index('grape') == 0
    assert fruits.index('orange') == 1
    assert fruits.index('banana') == 4
    assert fruits.index('banana', 5) == 7  # 在位置 5 之後搜尋下一個香蕉字串

    with pytest.raises(Exception):
        fruits.index('not existing element')

    # list.count(x)
    # 回傳目標內容在串列中的出現次數
    assert fruits.count('tangerine') == 0
    assert fruits.count('banana') == 2

    # list.copy()
    # 回傳串列的淺複製，等同於 a[:]
    fruits_copy = fruits.copy()
    assert fruits_copy == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.reverse()
    # 在原始串列中反轉串列元素
    fruits_copy.reverse()
    assert fruits_copy == [
        'banana',
        'apple',
        'kiwi',
        'banana',
        'pear',
        'apple',
        'orange',
        'grape',
    ]

    # list.sort(key=None, reverse=False)
    # 在原始串列中進行排序（傳入的引數可以用來做進階排序）
    # 詳見 sorted() 函式文件
    fruits_copy.sort()
    assert fruits_copy == [
        'apple',
        'apple',
        'banana',
        'banana',
        'grape',
        'kiwi',
        'orange',
        'pear',
    ]

    # list.pop([i])
    # 移除傳入索引值對應到位置之內容並將其回傳
    # 若沒有傳入索引值 a.pop() 將會從串列最後一個位置開始移除並回傳
    # 在資訊界的慣例裡，中括號表示這個參數是可選的，故您使用此方法時不用打上中括號
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits.pop() == 'banana'
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # list.clear()
    # 移除串列內的全部內容，等同於 del a[:]
    fruits.clear()
    assert fruits == []


def test_del_statement():
    """del 陳述式

    您可以使用 del 陳述式透過指定索引值來移除串列元素，
    此方式也可以搭配切片來移除串列內容（甚至可以移除整個串列），
    與 pop() 方法不同的是，此方式不會回傳該位置之內容
    """

    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    assert numbers == [1, 66.25, 333, 333, 1234.5]

    del numbers[2:4]
    assert numbers == [1, 66.25, 1234.5]

    del numbers[:]
    assert numbers == []

    # del 也可以用於刪除整個變數
    del numbers
    with pytest.raises(Exception):
        # 因為我們剛剛把變數刪掉了，所以使用該變數會產生錯誤
        assert numbers == []  # noqa: F821


def test_list_comprehensions():
    """列表構建

    列表構建提供了一個簡潔的方式來創建串列，
    一般我們創建串列的方式是透過迴圈以及條件判斷來新增內容至串列中，
    列表構建則是直接將迴圈和條件判斷寫在一行程式碼內， 並直接以串列的方式回傳結果
    """

    # 舉例來說，假設我們想要創建一個串列來表示數值平方
    squares = []
    for number in range(10):
        squares.append(number ** 2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 用這個方法的話需要創建一個 number 的整數變數且在迴圈的程式區塊內此變數都會存在
    # 我們可以使用以下的優化寫法來達成相同的功能
    squares = list(map(lambda x: x ** 2, range(10)))
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 或是，我們可以使用更簡潔並更具有可讀性的寫法
    squares = [x ** 2 for x in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 甚至我們可以用此方法來做更進階的操作，找出兩個串列的所有組合
    combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # 等同於
    combinations = []
    for first_number in [1, 2, 3]:
        for second_number in [3, 1, 4]:
            if first_number != second_number:
                combinations.append((first_number, second_number))

    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # 在這兩個範例中，for 和 if 的對應是相同的

    # 若表達式是元組，例如：上個例子中的 (x, y)
    # 在列表構建的表達式中就必須加上括號

    # 讓我們來看更多範例
    vector = [-4, -2, 0, 2, 4]

    # 創建一個新的串列，內容為 vector 的數值內容乘以 2
    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -4, 0, 4, 8]

    # 過濾串列中的負數
    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 2, 4]

    # 對串列中的所有元素套用函式
    abs_vector = [abs(x) for x in vector]
    assert abs_vector == [4, 2, 0, 2, 4]

    # 對串列中的所有元素執行其物件方法
    fresh_fruit = [' banana', ' loganberry ', 'passion fruit ']
    clean_fresh_fruit = [weapon.strip() for weapon in fresh_fruit]
    assert clean_fresh_fruit == ['banana', 'loganberry', 'passion fruit']

    # 創建一個包含這個元祖結構（number, square）的串列
    square_tuples = [(x, x ** 2) for x in range(6)]
    assert square_tuples == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # 將巢狀串列攤平（變成一維串列）
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_vector = [num for elem in vector for num in elem]
    assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_nested_list_comprehensions():
    """巢狀列表構建

    列表構建的初始表達式可以是另一個列表構建表達式
    """

    # 例如以下範例所呈現的 3x4 矩陣（透過 3 個串列，每個串列有 4 個值所組成）
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # 以下的列表構建可以實作出行列轉換
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    assert transposed_matrix == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 以上範例等同於：
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 也等同於：
    transposed = []
    for i in range(4):
        # 原本使用列表構建取得的列數值
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # 在現實世界中，您應該儘可能的使用內建函式來取代複雜的流程實作（不重複造輪）
    # 在這個實作範例中，zip() 函式可以給我們帶來很多的幫助：
    assert list(zip(*matrix)) == [
        (1, 5, 9),
        (2, 6, 10),
        (3, 7, 11),
        (4, 8, 12),
    ]
