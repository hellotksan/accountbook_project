import requests
import datetime
import input_utils


def show_accountbook(date: datetime.date) -> None:
    """指定された年月の家計簿を表示するプログラム

    Args:
        date (datetime.date): 指定された年月
    """

    date = date + "-01"
    url = "http://localhost:8000/accountbooks"
    header = {"Content-Type": "application/json"}
    payload = {
        "date": date
    }

    try:
        response = requests.get(url, headers=header, params=payload)

        # 収支の合計をそれぞれ引数に入れておく
        total_income = 0
        total_spending = 0

        if response.status_code == 200:
            response_json = response.json()
            accountbooks = response_json['accountbooks']

            print()
            print(f"-- {date[:4]}年{date[5:7]}月 --", end="\n\n")
            print("ID   年月日     種別 内訳      金額")
            print("---------------------------------------")

            for accountbook in accountbooks:
                # 収支の合計をそれぞれ計算する
                if accountbook['type'] == '収入':
                    total_income += accountbook['price']
                elif accountbook['type'] == '支出':
                    total_spending += accountbook['price']

                # 整列するためにIDを3桁の空白埋めをする
                fill_blank_id = str(accountbook['id']).ljust(3)
                # 金額を3桁ごとにカンマを入れる
                formated_price = f"{accountbook['price']:,}"

                print(f"{fill_blank_id}", end='  ')
                print(f"{accountbook['date']}", end=' ')
                print(f"{accountbook['type']}", end=' ')
                print(f"{accountbook['breakdown']}", end='  ')
                print(f"¥{formated_price}", end='\n')

            # 収支の合計をそれぞれ3桁ごとにカンマを入れる
            formated_total_income = f"{total_income:,}"
            formated_total_spending = f"{total_spending:,}"
            formated_total = f"{total_income - total_spending:,}"

            print()
            print(f"収入: ¥{formated_total_income}")
            print(f"支出: ¥{formated_total_spending}")
            print(f"合計: ¥{formated_total}")
        else:
            print("家計簿の削除に失敗しました")
            print(f"ステータスコード: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("[Error!] APIの呼び出し時にエラーが発生しました")
    except Exception as e:
        print("[Error!] 想定されていないエラーが発生しました")
        print(f"{e}")


def main() -> None:
    print("*** 帳簿⼀覧 ***")

    date = input_utils.validate_date("日付を入力してください [%Y-%m] : ", True)

    show_accountbook(date)


if __name__ == "__main__":
    main()
