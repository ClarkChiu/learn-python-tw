"""指派運算子

@詳見：https://www.w3schools.com/python/python_operators.asp

指派運算子用來設定數值至變數中
"""


def test_assignment_operator():
    """指派運算子"""

    # 指派: =
    number = 5
    assert number == 5

    # 多重指派
    # 同時指派兩個變數
    first_variable, second_variable = 0, 1
    assert first_variable == 0
    assert second_variable == 1

    # 您也可以利用多重指派來交換兩個變數的數值
    first_variable, second_variable = second_variable, first_variable
    assert first_variable == 1
    assert second_variable == 0


def test_augmented_assignment_operators():
    """指派運算子、算術運算子和位元運算子可以一起搭配使用"""

    # 指派: +=
    number = 5
    number += 3
    assert number == 8

    # 指派: -=
    number = 5
    number -= 3
    assert number == 2

    # 指派: *=
    number = 5
    number *= 3
    assert number == 15

    # 指派: /=
    number = 8
    number /= 4
    assert number == 2

    # 指派: %=
    number = 8
    number %= 3
    assert number == 2

    # 指派: %=
    number = 5
    number %= 3
    assert number == 2

    # 指派: //=
    number = 5
    number //= 3
    assert number == 1

    # 指派: **=
    number = 5
    number **= 3
    assert number == 125

    # 指派: &=
    number = 5           # 0b0101
    number &= 3          # 0b0011
    assert number == 1   # 0b0001

    # 指派: |=
    number = 5           # 0b0101
    number |= 3          # 0b0011
    assert number == 7   # 0b0111

    # 指派: ^=
    number = 5           # 0b0101
    number ^= 3          # 0b0011
    assert number == 6   # 0b0110

    # 指派: >>=
    number = 5
    number >>= 3
    assert number == 0   # (((5 // 2) // 2) // 2)

    # 指派: <<=
    number = 5
    number <<= 3
    assert number == 40  # 5 * 2 * 2 * 2
