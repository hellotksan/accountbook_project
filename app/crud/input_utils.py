import datetime


def validate_int(prompt: str, type_check: bool = False):
    """入力される値がint型になるかをチェックする関数

    Args:
        prompt (str): inputするときに表示する文字
        type_check (bool, optional): type(種別)を入力させるときにTrueにしておけば
        1か2を入力させるようにしつつ、戻り値にも文字列の内訳を返すことができる。
        デフォルトはFalse。

    Returns:
        _type_: type_checkがTrueのときはstr, Falseのときはint
    """
    while True:
        num = input(prompt)
        try:
            num = int(num)

            if type_check:
                if num != 1 and num != 2:
                    print("[Error!] 無効な値です。1か2を入力してください。")
                    continue
                if num == 1:
                    return "収入"
                elif num == 2:
                    return "支出"
            break
        except ValueError:
            print("[Error!] 無効な値です。整数を入力してください。")
            continue
    return num


def validate_date(prompt: str, show_check: bool = False) -> datetime.date:
    """入力される値がdatetime.date型になるかをチェックする関数

    Args:
        prompt (str): inputするときに表示する文字
        show_check (bool, optional): 年月のみをチェックしたいときにTrueにしておく。
        デフォルトはFalse。
    """
    while True:
        str = input(prompt)
        try:
            if show_check:
                datetime.datetime.strptime(str, "%Y-%m")
            else:
                datetime.datetime.strptime(str, "%Y-%m-%d")
        except ValueError:
            print("[Error!] 無効な値です。日付を入力してください [%Y-%m-%d]")
            continue
        break

    return str


def validate_len(prompt: str, length: int = 100) -> str:
    """入力される文字列が指定した長さになるかをチェックする関数

    Args:
        prompt (str): inputするときに表示する文字
        length (int): 指定した長さ。デフォルトは100。
    """
    while True:
        str = input(prompt)
        if len(str) > length:
            print(f"[Error!] 無効な文字数です。{length}文字以内で入力してください。")
            continue
        break

    return str


def confirm(prompt: str) -> bool:
    """削除するときに確認する関数

    Args:
        prompt (str): inputするときに表示する文字
    """
    while True:
        str = input(prompt)
        if str == "y":
            return True
        elif str == "n":
            return False
        else:
            print("[Error!] 無効な値です。yかnを入力してください")
