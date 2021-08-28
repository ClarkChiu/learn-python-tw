"""類型轉換

@詳見： https://www.w3schools.com/python/python_casting.asp

有些時候我們會想要指定變數的資料類型這時候就可以使用類型轉換來達成
Python 是物件導向程式語言，故資料類型皆是使用物件實作

在 Python 中使用建構函式來執行類型轉換
- int()：由整數、浮點數（四捨五入到前一個整數）或是字串來建構整數
- float()：由整數、浮點數或是字串來建構浮點數
- str() - 由多種資料類型（字串、整數文字、浮點數文字）來建構字串
"""


def test_type_casting_to_integer():
    """整數類型轉換"""

    assert int(1) == 1
    assert int(2.8) == 2
    assert int('3') == 3


def test_type_casting_to_float():
    """浮點數類型轉換"""

    assert float(1) == 1.0
    assert float(2.8) == 2.8
    assert float("3") == 3.0
    assert float("4.2") == 4.2


def test_type_casting_to_string():
    """字串類型轉換"""

    assert str("s1") == 's1'
    assert str(2) == '2'
    assert str(3.0) == '3.0'
