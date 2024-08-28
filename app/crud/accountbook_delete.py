import requests
import input_utils


def findbyid_accountbook(delete_id: int) -> bool:
    """指定されたIDで家計簿を入手する関数

    Args:
        delete_id (int): 削除したい家計簿のID
    """
    url = f"http://localhost:8000/accountbooks/{delete_id}"
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

            print()
            print("ID   年月日      種別 内訳      金額")
            print("------------------------------------")
            print(f"{fill_blank_id}", end='  ')
            print(f"{accountbook['date']}", end='  ')
            print(f"{accountbook['type']}", end=' ')
            print(f"{accountbook['breakdown']}", end='  ')
            print(f"{formated_price}", end='\n\n')
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


def delete_accountbook(delete_id: int) -> None:
    """指定されたIDの家計簿を削除する関数

    Args:
        delete_id (int): 削除したい家計簿のID
    """
    url = f"http://localhost:8000/accountbooks/{delete_id}"
    header = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=header)
        print()

        if response.status_code == 204:
            print("帳簿を削除しました")
        else:
            print("家計簿の削除に失敗しました")
            print(f"ステータスコード: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("[Error!] APIの呼び出し時にエラーが発生しました")
    except Exception as e:
        print("[Error!] 想定されていないエラーが発生しました")
        print(f"{e}")


def main() -> None:
    print("*** 帳簿削除 ***")

    delete_id = input_utils.validate_int("IDを入力してください : ")

    is_accountbook_exists = findbyid_accountbook(delete_id)

    if is_accountbook_exists:
        confirm_flag = input_utils.confirm("本当に削除してもよろしいですか？(y/n) : ")

        if confirm_flag:
            delete_accountbook(delete_id)
        else:
            print()
            print("削除をキャンセルしました")


if __name__ == "__main__":
    main()
