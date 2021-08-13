"""邏輯運算子

@詳見： https://www.w3schools.com/python/python_operators.asp

邏輯運算子用途為合併條件陳述式
"""


def test_logical_operators():
    """邏輯運算子"""

    # 讓我們用以下範例來說明邏輯運算子
    first_number = 5
    second_number = 10

    # 且
    # 若 "and（且）" 關鍵字兩旁的陳述式皆為真值（True），則回傳真值
    assert first_number > 0 and second_number < 20

    # 或
    # 若 "or（或）" 關鍵字兩旁的陳述式其中一個為真值，則回傳真值
    assert first_number > 5 or second_number < 20

    # 反相
    # 反轉結果，若結果為真值，則回傳假值（False）
    # pylint: disable=unneeded-not
    assert not first_number == second_number
    assert first_number != second_number
