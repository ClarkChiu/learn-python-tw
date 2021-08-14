"""恆等運算子

@詳見： https://www.w3schools.com/python/python_operators.asp

恆等運算子用途為比較物件，不僅是比較物件的內容，而是會更進一步比較到物件的記憶體位址
"""


def test_identity_operators():
    """恆等運算子"""

    # 讓我們使用以下的串列來說明恆等運算子
    first_fruits_list = ["apple", "banana"]
    second_fruits_list = ["apple", "banana"]
    third_fruits_list = first_fruits_list

    # 是（is）
    # 比對兩個變數，若這兩個變數是相同的物件，則回傳真值

    # 範例：
    # first_fruits_list 和 third_fruits_list 是相同的物件
    assert first_fruits_list is third_fruits_list

    # 不是（is not）
    # 比對兩個變數，若這兩個變數不是相同的物件，則回傳真值

    # 範例：
    # 雖然 first_fruits_list 和 second_fruits_list 有著相同的內容，但他們不是相同的物件
    assert first_fruits_list is not second_fruits_list

    # 我們將用以下範例展示 "is" 和 "==" 的差異
    # 因為 first_fruits_list 內容等於 second_fruits_list，故以下比較將回傳真值
    assert first_fruits_list == second_fruits_list
