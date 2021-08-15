"""變數

@詳見: https://docs.python.org/3/tutorial/introduction.html
@詳見: https://www.w3schools.com/python/python_variables.asp
@詳見: https://www.learnpython.org/en/Variables_and_Types

Python 是完全物件導向且是非靜態型別（Statically typed）的程式語言。您不用在使用變數前事先宣告變數及其形態。每一個變數在 Python 中皆是物件。

不像其他程式語言，Python 沒有用來宣告變數的關鍵字。當直譯器執行到指派變數的那行程式碼時，變數會自動被創建。

一個變數名稱可以是很短的（例如：x 或 y）也可以是具有描述性的名稱（例如：age、carname 和 total_volume）。

Python 變數規則：
- 變數名稱必須以字母或是底線作為起始字元
- 變數名稱不能夠以數字作為起始字元
- 變數名稱僅能夠包含英文字母、數字和底線（即 A-z、0-9 和 _）
- 變數名稱是區分大小寫的（例如：age、Age 和 AGE 是三個不同的變數）
"""


def test_variables():
    """變數測試"""

    integer_variable = 5
    string_variable = 'John'

    assert integer_variable == 5
    assert string_variable == 'John'
    variable_with_changed_type = 4  # 此變數目前是整數類型
    variable_with_changed_type = 'Sally'  # 此變數目前是字串類型

    assert variable_with_changed_type == 'Sally'
