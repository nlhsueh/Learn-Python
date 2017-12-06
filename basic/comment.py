# one line comment, 這是一行註解

"""
block commment 
Hello, 這是一個
多行註解
"""  		

''' 
block comment 
這樣也是多行註解，
三個單引號或三個雙引號都可以 
'''

# docstring, 寫在 function 下的說明，稱為 docstring
def add(x, y):
    """ Adding two values
    @param x: one value
    @param y: another value
    @return: the result of adding x and y
    """
    
    return x+y

# docstring 可以透過 __doc__ 或 help 來取得
print (add.__doc__)