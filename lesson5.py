# functoolsモジュールからwrapsをインポート
from functools import wraps

# ユーザー情報の辞書
user = {"name": "Nana", "membership": "gold"}

# デコレータの定義


def membership_choice(member_class):
    """
    ユーザーのメンバーシップが指定されたクラスに一致する場合にのみ関数を実行するデコレータ。

    引数:
    - member_class (str): チェックするメンバーシップクラス。
    """
    def user_qualified(f):
        """
        ユーザーのメンバーシップが指定されたクラスに一致する場合に関数を実行するデコレータ。
        """
        @wraps(f)
        def judge_func(*args, **kwargs):
            """
            メンバーシップが指定されたクラスに一致する場合に関数を実行する内部関数。
            任意の引数とキーワード引数を受け取る。
            """
            if user.get("membership") == member_class:
                return f(*args, **kwargs)
        return judge_func
    return user_qualified

# デコレータを使用して定義された関数1


@membership_choice("gold")
def welcome_func(name):
    """
    ユーザーが"gold"メンバーシップの場合に実行される関数。
    名前を受け取り、クーポンメッセージを返す。

    引数:
    - name (str): ユーザーの名前。

    戻り値:
    - str: クーポンメッセージ。
    """
    return f'Welcome {name}! 20% OFF クーポン: get 20%off'


# welcome_funcの実行と出力
print(welcome_func(user.get("name")))  # メンバーシップが"gold"のため実行される

# デコレータを使用して定義された関数2


@membership_choice("silver")
def no_func():
    """
    メンバーシップが"silver"のユーザーにウェルカムメッセージを表示する関数。
    引数なし。

    戻り値:
    - str: ウェルカムメッセージ。
    """
    return "Welcome!"


# no_funcの実行と出力
print(no_func())  # メンバーシップが"gold"のため実行されない
