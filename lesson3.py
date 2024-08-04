# functoolsモジュールからwrapsをインポート
from functools import wraps

# ユーザー情報の辞書
user = {"name": "Nana", "membership": "gold"}

# デコレータの定義


def user_qualified(f):
    """
    ユーザーのメンバーシップが"gold"である場合にのみ関数を実行するデコレータ。
    """
    @wraps(f)
    def judge_func():
        """
        メンバーシップが"gold"の場合に関数を実行する内部関数。
        """
        if user.get("membership") == "gold":
            return f()
    return judge_func

# デコレータを使用して定義された関数1


@user_qualified
def welcome_func():
    """
    ユーザーが"gold"メンバーシップの場合にのみ実行される関数。
    """
    return 'Welcome! 20% OFF クーポン: get 20%off'

# デコレータを使用して定義された関数2


@user_qualified
def another_func():
    """
    メンバーシップの条件に関係なく何もしない関数。
    """
    pass


# 関数の実行と出力
print(welcome_func())  # メンバーシップが"gold"のため実行される

# 関数のメタデータの出力
print("welcome_func.__name__ :" + welcome_func.__name__)  # 関数の名前を表示
print("welcome_func.__doc__ :" + welcome_func.__doc__)   # 関数のドキュメントを表示

print("another_func.__name__ :" + another_func.__name__)  # 関数の名前を表示
print("another_func.__doc__" + another_func.__doc__)   # 関数のドキュメントを表示

print(welcome_func())  # メンバーシップが"gold"のため実行される
