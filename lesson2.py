# デコレータAを定義
def A(myfunc):
    """
    myfuncの前後にメッセージを出力するデコレータ。
    """
    def inner_func():
        print(" A 1st_decorator")  # デコレータAの最初のメッセージ
        myfunc()  # 元の関数を実行
        print(" A 2nd_decorator")  # デコレータAの最後のメッセージ
    return inner_func

# デコレータBを定義


def B(myfunc):
    """
    myfuncの前後にメッセージを出力するデコレータ。
    """
    def inner_func():
        print(" B 1st_decorator")  # デコレータBの最初のメッセージ
        myfunc()  # 元の関数を実行
        print(" B 2nd_decorator")  # デコレータBの最後のメッセージ
    return inner_func

# デコレータBとAを使用してmyfuncを定義


@B  # まずデコレータBが適用される
@A  # 次にデコレータAが適用される
def myfunc():
    """
    デコレータの動作を確認するための関数。
    """
    print("Hello, decorator")  # 元の関数のメッセージ


# 関数を実行
myfunc()
