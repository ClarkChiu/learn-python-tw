"""算術運算子

@詳見: https://www.w3schools.com/python/python_operators.asp

算術運算子被使用來對數字進行數學運算
"""


def test_arithmetic_operators():
    """算術運算子"""

    # 加法
    assert 5 + 3 == 8

    # 減法
    assert 5 - 3 == 2

    # 乘法
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # 除法
    # 除法結果以浮點數呈現
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # 模數（取餘數）
    assert 5 % 3 == 2

    # 指數
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # 取整除法
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)
