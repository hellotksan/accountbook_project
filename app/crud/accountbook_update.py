import requests
import datetime
import input_utils


def findbyid_accountbook(edit_id: int) -> bool:
    """指定されたIDの家計簿を入手する関数

    Args:
        edit_id (int): 変更したい家計簿のID
    """
    url = f"http://localhost:8000/accountbooks/{edit_id}"
    header = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=header)

        if response.status_code == 200:
            response_json = response.json()
            accountbook = response_json['accountbook']

            # 整列するためにIDを3桁の空白埋めをする
            fill_blank_id = str(accountbook['id']).ljust(3)
            # 金額を3桁ごとにカンマを入れる
            formated_price = f"{accountbook['price']:,}"

            print('以下の帳簿を更新します')
            print()
            print("ID   年月日      種別 内訳      金額")
            print("------------------------------------")
            print(f"{fill_blank_id}", end='  ')
            print(f"{accountbook['date']}", end='  ')
            print(f"{accountbook['type']}", end=' ')
            print(f"{accountbook['breakdown']}", end='  ')
            print(f"¥{formated_price}", end='\n\n')
            return True
        elif response.status_code == 404:
            print()
            print("指定したIDの家計簿は存在しません")
            return False
        else:
            print("家計簿の削除に失敗しました")
            print(f"ステータスコード: {response.status_code}")
            return False

    except requests.exceptions.ConnectionError:
        print("[Error!] APIの呼び出し時にエラーが発生しました")
    except Exception as e:
        print("[Error!] 想定されていないエラーが発生しました")
        print(f"{e}")


def update_accountbook(
        date: datetime.date,
        type_: str,
        breakdown: str,
        price: int,
        edit_id: int) -> None:
    """家計簿を変更する関数

    Args:
        date (datetime.date): 家計簿の日付
        type_ (str): 家計簿の種別
        breakdown (str): 家計簿の内訳
        price (int): 家計簿の値段
        edit_id (int): 編集したい家計簿のID
    """
    url = f"http://localhost:8000/accountbooks/{edit_id}"
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
        response = requests.put(url, json=register_data, headers=header)

        if response.status_code == 204:
            print("帳簿を更新しました")
        else:
            print("家計簿の削除に失敗しました")
            print(f"ステータスコード: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("[Error!] APIの呼び出し時にエラーが発生しました")
    except Exception as e:
        print("[Error!] 想定されていないエラーが発生しました")
        print(f"{e}")


def main() -> None:
    print("*** 帳簿更新 ***")

    edit_id = input_utils.validate_int("IDを入力してください : ")

    is_accountbook_exists = findbyid_accountbook(edit_id)

    if is_accountbook_exists:
        type_ = input_utils.validate_int("収入(1) or 支出(2)を入力してください : ", True)
        date = input_utils.validate_date("日付を入力してください [%Y-%m-%d] : ")
        breakdown = input_utils.validate_len("内訳を入力してください : ")
        price = input_utils.validate_int("金額を入力してください : ")

        update_accountbook(date, type_, breakdown, price, edit_id)


if __name__ == "__main__":
    main()
