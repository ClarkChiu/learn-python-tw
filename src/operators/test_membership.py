"""成員運算子

@詳見： https://www.w3schools.com/python/python_operators.asp

成員運算子用途為判斷序列類型的資料是否存在於某個物件中
"""


def test_membership_operators():
    """成員運算子"""

    # 讓我們使用以下的範例來說明成員的概念
    fruit_list = ["apple", "banana"]

    # 在其中（in）
    # 若此序列類型的資料存在於物件中，則回傳真值
    # 因為 fruit_list 串列包含 "banana"，故以下陳述式將回傳真值
    assert "banana" in fruit_list

    # 不在其中（not in）
    # 若此序列類型的資料不存在於物件中，則回傳真值
    # 因為 fruit_list 串列不包含 "pineapple"，故以下陳述式將回傳真值
    assert "pineapple" not in fruit_list
