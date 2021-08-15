"""數字

@詳見： https://docs.python.org/3/tutorial/introduction.html
@詳見： https://www.w3schools.com/python/python_numbers.asp

在 Python 中，數字可以使用三種資料類型來表示
- 整數類型（例如：2、4、20）
    - 布林類型（例如：假值和真值，對應到 0 和 1）
- 浮點數類型（例如：5.0、1.6）
- 複數類型（例如：5+6j、4-3j）
"""


def test_integer_numbers():
    """整數類型

    整數類型是用來表示不包含小數的正、負號數字（長度無限制）
    """

    positive_integer = 1
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int)
    assert isinstance(negative_integer, int)
    assert isinstance(big_integer, int)


def test_booleans():
    """布林類型

    布林值是用來表示真值或假值，這兩個數值（真值和假值）是布林物件中唯二的兩個表示值。
    布林類型是整數類型的子類型，在幾乎所有的使用情境中，布林值也分別對應至 0 和 1。
    除了您將其轉換為字串時，布林值將做為字串 "False" 或 "True" 分別被傳回。
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean
    assert not false_boolean

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # 讓我們來嘗試將布林值轉換成字串
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"


def test_float_numbers():
    """浮點數類型

    浮點數類型是用來表示包含小數的正、負號數字
    """

    float_number = 7.0
    # 另外一個宣告浮點數的方式為使用 float() 函式
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # 浮點數可以使用 E 表示法（科學記數法）來表示 10 的次方
    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000
    assert float_with_big_e == 120000
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


def test_complex_numbers():
    """複數類型"""

    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


def test_number_operators():
    """基本操作"""

    # 加法
    assert 2 + 4 == 6

    # 乘法
    assert 2 * 4 == 8

    # 除法結果以浮點數回傳
    assert 12 / 3 == 4.0
    assert 12 / 5 == 2.4
    assert 17 / 3 == 5.666666666666667

    # 模數運算子會回傳除法的餘數
    assert 12 % 3 == 0
    assert 13 % 3 == 1

    # 取整除法捨棄了小數部分的結果
    assert 17 // 3 == 5

    # 計算數字的次方
    assert 5 ** 2 == 25   # 5 的平方
    assert 2 ** 7 == 128  # 2 的 7 次方

    # Python 支援浮點數類型和整數類型的混合運算（整數會先被轉換為浮點數後再進行運算）
    assert 4 * 3.75 - 1 == 14.0
