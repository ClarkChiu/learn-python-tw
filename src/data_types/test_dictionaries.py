"""字典

@詳見： https://docs.python.org/3/tutorial/datastructures.html#dictionaries
@詳見： https://www.w3schools.com/python/python_dictionaries.asp

字典通常是由無序的、可變且可以被索引的內容所組成
Python 使用大括號來指派字典變數，並在其中使用鍵值來儲存資料

字典有時也被稱為關聯式記憶或關聯陣列
不像序列，字典是使用鍵值來實作索引
鍵（Key）可以是任何不可修改的資料類型（字串或數字都可以）
當元組只包含字串、數字或元組本身時，其也可以做為鍵
若元組包含可變的物件時，其就不能夠做為鍵
因為串列可以被修改，故其不能夠做為鍵

比較簡單理解字典的方法是將其想成是一群鍵值集合（在同一個字典中，鍵具有唯一性）
在 Python 中可以用一組空白的大括號來創建字典 {}
利用放入逗點分隔的鍵值資料來初始化字典
Python 也是使用相同的方式來輸出字典到螢幕上
"""


def test_dictionary():
    """字典"""

    fruits_dictionary = {
        'cherry': 'red',
        'apple': 'green',
        'banana': 'yellow',
    }

    assert isinstance(fruits_dictionary, dict)

    # 您可以利用鍵來索引值
    assert fruits_dictionary['apple'] == 'green'
    assert fruits_dictionary['banana'] == 'yellow'
    assert fruits_dictionary['cherry'] == 'red'

    # 您可以利用 in 關鍵字來檢查鍵是否存在於字典中
    assert 'apple' in fruits_dictionary
    assert 'pineapple' not in fruits_dictionary

    # 改變某個鍵所對應到的值
    fruits_dictionary['apple'] = 'red'

    # 新增鍵值內容
    fruits_dictionary['pineapple'] = 'yellow'
    assert fruits_dictionary['pineapple'] == 'yellow'

    # 執行 list() 函式可以取得字典中鍵的串列（未排序），若需要排序的話，可以使用 sorted() 函式
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
    assert sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

    # del 也可以用於刪除鍵值資料
    del fruits_dictionary['pineapple']
    assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

    # 序列的鍵值資料可以利用 dict() 建構函式來創建字典
    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    assert dictionary_via_constructor['sape'] == 4139
    assert dictionary_via_constructor['guido'] == 4127
    assert dictionary_via_constructor['jack'] == 4098

    # 此外，字典構建（Dict Comprehensions）可以從任意鍵和值的表達式來創建字典
    dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}
    assert dictionary_via_expression[2] == 4
    assert dictionary_via_expression[4] == 16
    assert dictionary_via_expression[6] == 36

    # 當鍵為簡易的字串時，您可以使用關鍵字引數傳入dict() 函式的方式來創建字典
    dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
    assert dictionary_for_string_keys['sape'] == 4139
    assert dictionary_for_string_keys['guido'] == 4127
    assert dictionary_for_string_keys['jack'] == 4098
