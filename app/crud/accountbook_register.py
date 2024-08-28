import requests
import datetime
import input_utils


def register_accountbook(
        date: datetime.date,
        type_: str,
        breakdown: str,
        price: int) -> None:
    """新規に家計簿に登録するプログラム

    Args:
        date (datetime.date): 家計簿の日付
        type_ (str): 家計簿の種別
        breakdown (str): 家計簿の内訳
        price (int): 家計簿の値段
    """

    url = "http://localhost:8000/accountbooks"
    register_data = {
        "id_": 0,
        "date": date,
        "type_": type_,
        "breakdown": breakdown,
        "price": price,
    }
    header = {"Content-Type": "application/json"}
    print()

    try:
        response = requests.post(url, json=register_data, headers=header)

        if response.status_code == 201:
            print("帳簿を登録しました")
        else:
            print("家計簿の削除に失敗しました")
            print(f"ステータスコード: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("[Error!] APIの呼び出し時にエラーが発生しました")
    except Exception as e:
        print("[Error!] 想定されていないエラーが発生しました")
        print(f"{e}")


def main() -> None:
    print("*** 帳簿登録 ***")

    type_ = input_utils.validate_int("収入(1) or 支出(2)を入力してください : ", True)
    date = input_utils.validate_date("日付を入力してください [%Y-%m-%d] : ")
    breakdown = input_utils.validate_len("内訳を入力してください : ")
    price = input_utils.validate_int("金額を入力してください : ")

    register_accountbook(date, type_, breakdown, price)


if __name__ == "__main__":
    main()
