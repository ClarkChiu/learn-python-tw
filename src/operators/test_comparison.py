"""比較運算子

@詳見：https://www.w3schools.com/python/python_operators.asp

比較運算子是用來比較兩個數值
"""


def test_comparison_operators():
    """比較運算子"""

    # 等於
    number = 5
    assert number == 5

    # 不等於
    number = 5
    assert number != 3

    # 大於
    number = 5
    assert number > 3

    # 小於
    number = 5
    assert number < 8

    # 大於等於
    number = 5
    assert number >= 5
    assert number >= 4

    # 小於等於
    number = 5
    assert number <= 5
    assert number <= 6
