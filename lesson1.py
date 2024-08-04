import datetime

# 時間を出力するデコレータ関数


def area(f):
    """
    関数の実行開始と終了時に現在の時間を出力するデコレータ。
    """
    def wrapper(*args, **kwargs):
        print(f"開始 : {datetime.datetime.now()}")  # 関数の実行開始時刻を出力
        f(*args, **kwargs)  # 元の関数を実行
        print(f"終了 : {datetime.datetime.now()}")  # 関数の実行終了時刻を出力
        print("---------------------------------")  # 区切り線を出力
        print("")  # 空行を出力（見やすさのため）

    return wrapper

# 三角形の面積を計算する関数


@area
def triangle(base, height):
    """
    三角形の面積を計算して出力する関数。
    """
    area = base * height / 2
    print(f"triangle_area : {area}")  # 三角形の面積を出力

# 円の面積を計算する関数


@area
def circle(pi, radius):
    """
    円の面積を計算して出力する関数。
    """
    area = pi * radius * 2
    print(f"circle_area : {area}")  # 円の面積を出力

# 台形の面積を計算する関数


@area
def trapezoid(up, down, height):
    """
    台形の面積を計算して出力する関数。
    """
    area = (up + down) * height / 2
    print(f"trapezoid_area : {area}")  # 台形の面積を出力


# 各関数を実行する
triangle(20, 30)
circle(3.14, 30)
trapezoid(20, 40, 40)
