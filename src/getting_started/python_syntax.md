# Python 語法

**Python 語法與其他程式語言語法的差異**

- Python 是基於可讀性的考量來設計的，其擁有類似英文的簡單語法（當然還是略微受到了數學呈現的影響）

- Python 使用換行來代表新的命令執行，不像其他程式語言通常是使用分號或括號

- Python 依靠空白字元建立縮排來定義程式範圍，例如：迴圈、函式和類別。相比於 Python，其他程式語言通常使用大括號來代表範圍

## Python 縮排

在其他程式語言中縮排通常只是為了可讀性，但在 Python 中，縮排有著特殊意義。

因為 Python 使用縮排來表示程式區塊。

```python
if 5 > 2:
    print("Five is greater than two!")
```

因此，若您搞錯了縮排，Python 將會輸出錯誤訊息。

## 註解

Python 擁有在程式碼內利用註解來撰寫文件的能力。

當某行程式碼以 `#` 開頭時，Python 會將此行視為註解。

```python
# 這行是註解
print("Hello, World!")
```

## 文件字串（Docstrings）

Python 也擁有擴充註解成為文件的能力，官方稱為文件字串。

文件字串可以是單行也可以是多行，其用途與註解相同。

Python 使用三個引號（單引號和雙引號皆可）作為文件字串的開始和結尾識別：

```python
"""這是
多行的文字字串"""
print("Hello, World!")
```

## 參考資料

- [w3schools.com](https://www.w3schools.com/python/python_syntax.asp)