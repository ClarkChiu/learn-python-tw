"""賦值運算子

@詳見：https://www.w3schools.com/python/python_operators.asp

賦值運算子是用來幫變數設定內容
"""


def test_assignment_operator():
    """賦值運算子"""

    # 賦值: =
    number = 5
    assert number == 5

    # 多重賦值
    # 同時賦值兩個變數
    first_variable, second_variable = 0, 1
    assert first_variable == 0
    assert second_variable == 1

    # 您也可以利用多重賦值來交換兩個變數的內容
    first_variable, second_variable = second_variable, first_variable
    assert first_variable == 1
    assert second_variable == 0


def test_augmented_assignment_operators():
    """賦值運算子、算術運算子和位元運算子可以一起搭配使用"""

    # 賦值: +=
    number = 5
    number += 3
    assert number == 8

    # 賦值: -=
    number = 5
    number -= 3
    assert number == 2

    # 賦值: *=
    number = 5
    number *= 3
    assert number == 15

    # 賦值: /=
    number = 8
    number /= 4
    assert number == 2

    # 賦值: %=
    number = 8
    number %= 3
    assert number == 2

    # 賦值: %=
    number = 5
    number %= 3
    assert number == 2

    # 賦值: //=
    number = 5
    number //= 3
    assert number == 1

    # 賦值: **=
    number = 5
    number **= 3
    assert number == 125

    # 賦值: &=
    number = 5          # 0b0101
    number &= 3         # 0b0011
    assert number == 1  # 0b0001

    # 賦值: |=
    number = 5          # 0b0101
    number |= 3         # 0b0011
    assert number == 7  # 0b0111

    # 賦值: ^=
    number = 5          # 0b0101
    number ^= 3         # 0b0011
    assert number == 6  # 0b0110

    # 賦值: >>=
    number = 5
    number >>= 3
    assert number == 0  # (((5 // 2) // 2) // 2)

    # 賦值: <<=
    number = 5
    number <<= 3
    assert number == 40  # 5 * 2 * 2 * 2
