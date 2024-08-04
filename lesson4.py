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
    def judge_func(*args, **kwargs):
        """
        メンバーシップが"gold"の場合に関数を実行する内部関数。
        任意の引数とキーワード引数を受け取る。
        """
        if user.get("membership") == "gold":
            return f(*args, **kwargs)
    return judge_func

# デコレータを使用して定義された関数1


@user_qualified
def welcome_func(name):
    """
    ユーザーが"gold"メンバーシップの場合に実行される関数。
    名前を受け取り、クーポンメッセージを返す。
    """
    return f'Welcome {name}! 20% OFF クーポン: get 20%off'


# welcome_funcの実行と出力
print(welcome_func(user.get("name")))  # メンバーシップが"gold"のため実行される

# デコレータを使用して定義された関数2


@user_qualified
def no_func():
    """
    メンバーシップが"gold"のユーザーにウェルカムメッセージを表示する関数。
    引数なし。
    """
    return "Welcome!"


# no_funcの実行と出力
print(no_func())  # メンバーシップが"gold"のため実行される

# デコレータを使用して定義された関数3


@user_qualified
def multi_func(first_name, last_name, stamps=3):
    """
    ユーザーが"gold"メンバーシップの場合に実行される関数。
    名前とスタンプ数を受け取り、メッセージを返す。
    """
    return f"Welcome {first_name} {last_name}!, you have {stamps} stamps."


# multi_funcの実行と出力
print(multi_func("Taro", "Momo", stamps=5))  # メンバーシップが"gold"のため実行される
