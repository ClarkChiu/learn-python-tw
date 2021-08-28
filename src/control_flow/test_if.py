"""IF 陳述式

@詳見： https://docs.python.org/3/tutorial/controlflow.html

IF 陳述式有可選的例外判斷，elif 或是 else，
關鍵字 elif 是 else if 的縮寫，可以有效的避免過多縮排

if … elif … elif … 可以用來代替其他程式語言中的 switch 陳述式
"""


def test_if_statement():
    """IF 陳述式"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = '數字小於零'
    elif number == 0:
        conclusion = '數字等於零'
    elif number < 1:
        conclusion = '數字大於零但小於一'
    else:
        conclusion = '數字大於等於一'

    assert conclusion == '數字大於等於一'
