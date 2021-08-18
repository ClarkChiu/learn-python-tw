"""字串

@詳見： https://docs.python.org/3/tutorial/introduction.html
@詳見： https://www.w3schools.com/python/python_strings.asp
@詳見： https://www.w3schools.com/python/python_ref_string.asp

除了數字之外，Python 也可以處理字串。字串可以使用多種方式來呈現，
可以使用兩個單引號或是雙引號來將內容包起來成為字串，例如：'我是字串' 或是 "我也是字串"
"""

import pytest


def test_string_type():
    """字串類型"""

    # 使用雙引號
    name_1 = "John"
    # 使用單引號
    name_2 = 'John'

    # 不管使用以上哪種方式創建字串，Python 皆會將其視為相同物件
    assert name_1 == name_2
    assert isinstance(name_1, str)
    assert isinstance(name_2, str)

    # 在 Python 中，我們使用 \（反斜線）來跳脫引號
    # 用法為 \' 或是 \"
    single_quote_string = 'doesn\'t'
    double_quote_string = "doesn't"

    assert single_quote_string == double_quote_string

    # \n 代表換行字元
    multiline_string = 'First line.\nSecond line.'
    # 若沒有使用 print() 函式，\n 會作為字串存在
    # 若使用 print() 函式，\n 會輸出成換行
    assert multiline_string == 'First line.\nSecond line.'

    # 字串可以被索引，例如：可以透過索引值 0 來取得第 1 個字元
    # Python 中並沒有字元資料類型，一個字元可以簡單看成長度為 1 的字串
    # 注意索引值 -0 和 0 是相同的，負號的索引值是從 -1 作為起始點
    word = 'Python'
    assert word[0] == 'P'   # 第 1 個字元
    assert word[5] == 'n'   # 第 5 個字元
    assert word[-1] == 'n'  # 最後 1 個字元
    assert word[-2] == 'o'  # 倒數第 2 個字元
    assert word[-6] == 'P'  # 倒數第 6 個字元或第 0 個字元

    assert isinstance(word[0], str)

    # Python 中的字串不僅支援索引功能，也支援切片功能
    # 索引功能是取得單獨的字元，切片功能則可以讓您獲得子字串
    assert word[0:2] == 'Py'   # 從位置 0（包含）到位置 2（不包含）的字串
    assert word[2:5] == 'tho'  # 從位置 2（包含）到位置 5（不包含）的字串

    # 要特別注意的是，切片功能總是會包含起始索引值所對應到的字元（冒號左邊）
    # 也總是不包含結束索引值對應到的字元（冒號右邊）
    # 這個特性讓我們可以確定 s[:i] + s[i:] 總是等於 s
    assert word[:2] + word[2:] == 'Python'
    assert word[:4] + word[4:] == 'Python'

    # 切片功能有個實用的設計：若您省略了起始索引值，其預設會從 0 起始。
    # 若您省略了結束索引值，其預設以字串的最後一個字元作為結束。
    assert word[:2] == 'Py'   # 從位置 0（預設）到位置 2（不包含）的字串
    assert word[4:] == 'on'   # 從位置 4（包含）到字串中最後一個字元（預設）的子字串
    assert word[-2:] == 'on'  # 從倒數第 2 個字元（包含）到字串中最後一個字元（預設）的子字串

    # 一個記住切片運作方式的方法為
    # 想像索引值是指向字元和字元的中間，最左邊邊界是位置 0
    # 最右邊邊界是此字串的長度，如以下範例：
    #
    #  +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #  0   1   2   3   4   5   6
    # -6  -5  -4  -3  -2  -1

    # 若您嘗試使用大於字串長度的索引值將會導致錯誤發生
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # 然而，若您使用切片，超過範圍的索引值是可以被允許的：
    assert word[4:42] == 'on'
    assert word[42:] == ''

    # Python 的字串類型變數是不可修改的
    # 因此，若您嘗試賦值給某個索引位置的字元，
    # 將會導致錯誤發生
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'

    # 若您需要一個不同的字串，您必須重新創建一個新的：
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # 內建的 len() 函式可以用來回傳字串的長度
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34

    # 字串可以利用三個引號來跨多行進行賦值： """...""" 或 '''...'''
    # 當使用此種方式賦值時，連空白行也會被包含至字串中
    # 但可以在行尾加上 \ 來避免這個問題，如以下範例：
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''


def test_string_operators():
    """基本操作

    若要連接字串，可以使用 + 運算子
    若要重複字串，則可以使用 * 運算子
    """

    assert 3 * 'un' + 'ium' == 'unununium'

    # 若使用以下寫法，直譯器也會將字串連接在一起
    # pylint: disable=implicit-str-concat
    python = 'Py' 'thon'
    assert python == 'Python'

    # 這個特性在您想要避免使用過長字串時特別有用
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )

    assert text == 'Put several strings within parentheses to have them joined together.'

    # + 運算子也可以用於連接字串變數
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'


def test_string_methods():
    """字串方法"""

    hello_world_string = "Hello, World!"

    # strip() 方法可以用來移除在目標字串前後的所有空白字元
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # len() 方法會將字串長度回傳
    assert len(hello_world_string) == 13

    # lower() 方法會將字串內所有英文字元轉換成小寫
    assert hello_world_string.lower() == 'hello, world!'

    # upper() 方法會將字串內所有英文字元轉換成大寫
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # replace() 方法會將目標字串取代成為新字串
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # split() 方法會將目標字串分割為子字串（若其找到分割基準字串/字元）
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # 將第一個字元轉換為英文大寫
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # 計算某個字元/串在整個字串出現的次數
    assert 'low letter at the beginning'.count('t') == 4

    # 搜尋目標字串在整個字串中的索引位置
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # 將字串內的每個英文單字字首轉為大寫字母
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # 取代字串
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # 將可以被迭代的目標物件連接成字串
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # 若字串內的每個字元皆為大寫，則回傳真值
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # 檢查字串內的每個字元是否都是字母
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # 若字串內的每個字元皆為數字，則回傳真值
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()


def test_string_formatting():
    """字串格式化

    常常我們會有格式化輸出的需求，
    Python 提供了一些方法來幫助我們格式化字串
    """

    # 我們可以使用 f-string 的功能來進行字串格式化
    # 首先，在使用字串時，我們先在引號左邊加上 f 或是 F，
    # 在字串中您就可以使用 { } 符號來撰寫 Python 表達式或是取得變數/文字內容
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # str.format() 字串格式化方法則需要多一點手工，我們還是一樣使用 { } 符號來標記變數取代的位置
    # 並提供更詳細的格式化指示，但用來取代的資料需要透過 .format() 函式傳入
    yes_votes = 42_572_654  # 等同於 42572654
    no_votes = 43_132_495   # 等同於 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes 49.67%'

    # 當您僅是需要快速輸出來進行除錯時，
    # 您可以使用 repr() 或 str() 函式來將任何物件轉換為字串，
    # str() 函式的用途為將物件轉換為人類可以閱讀的字串，
    # 而 repr() 函式則是將物件轉換成直譯器可以讀取的字串，
    # 若該物件沒有實作 __str__() 方法，則此函式會回傳 repr() 函式的執行結果，
    # 若該物件沒有 __repr__() 方法則會導致語法錯誤，

    # 許多資料結構，例如數字、串列和字典，
    # 在個別的物件中都實作了相同的 __str__() 和 __repr__() 表示函式，
    # 但字串則是有兩個不同的表示函式

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1/7) == '0.14285714285714285'

    # repr() 函式可以傳入任何 Python 物件：
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # 字串格式化：
    # f-string 功能可以讓您在字串中直接使用 Python 的表達式，
    # 語法為 f'{expression}'，
    # 您可以利用以下可選的描述符號來更進一步格式化輸出

    # 以下範例將 pi 四捨五入至小數點後三位
    pi_value = 3.14159
    assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # 在 : 後寫上整數可以設定輸出的字元寬度，這個功能在對齊時很有用
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    for name, phone in table_data.items():
        table_string += f'{name:7}==>{phone:7d}'

    assert table_string == ('Sjoerd ==>   4127'
                            'Jack   ==>   4098'
                            'Dcab   ==>   7678')

    # format() 方法
    # str.format() 的基本使用方式為
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # 在字串中的大括號（稱為格式化欄位）將會被傳入 str.format() 方法的物件內容所取代
    # 您也可以在大括號中填入數字來標示傳入 str.format() 方法的物件位置，藉以來索引用來取代的內容
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # 若 str.format() 傳入的是關鍵字索引，則您可以利用關鍵字來選取用來取代的內容
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # 位置索引和關鍵字索引可以被任意搭配使用
    formatted_string = 'The story of {0}, {1}, and {other}.'. format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'

    # 若您要格式化的字串很長，且您不想分割它的話
    # 您可以使用鍵值索引的方式來達成這個需求
    # 您可以傳入一個字典物件並使用中括號 '[]' 來使用鍵值索引
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'. format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

    # 您也可以使用關鍵字索引的方式傳入此表格（透過 ** 標記）來達成相同的效果
    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'. format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
