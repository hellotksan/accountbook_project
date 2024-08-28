from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Accountbook(BaseModel):
    id_: int = None
    date: datetime.date
    type_: str = None
    breakdown: str = None
    price: int = None


# MySQLに接続
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="accountbook"
)
# MySQLに接続(AWS上のRDSに接続)
# mydb = mysql.connector.connect(
#     host="sample-mysql.ceuuapfocode.us-east-1.rds.amazonaws.com",
#     user="admin",
#     password="tondesaitama123",
#     database="accountbook"
# )


# すべての家計簿情報を取得するAPI
@app.get("/accountbooks/all")
def fetch_all():
    sql = """
    SELECT * FROM accountbooks
    ORDER BY date;
    """

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()

    return {"accountbooks": results}


# 指定された年月の家計簿情報を取得するAPI
@app.get("/accountbooks")
def find_by_date(date):
    sql = """
    SELECT * FROM accountbooks
    WHERE date BETWEEN %s AND LAST_DAY(%s)
    ORDER BY date;
    """

    values = (date, date)

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, values)
    results = cursor.fetchall()

    return {"accountbooks": results}


# 指定されたIDの家計簿情報を取得するAPI
@app.get("/accountbooks/{accountbook_id}")
def find_one(accountbook_id: int, response: Response):
    sql = """
    SELECT * FROM accountbooks
    WHERE id = %s
    """
    value = (accountbook_id, )

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, value)
    result = cursor.fetchone()

    if result is not None:
        return {"accountbook": result}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Accountbook not found"}


# 新規に家計簿を登録するAPI
@app.post('/accountbooks', status_code=201)
def register(accountbook: Accountbook):
    sql = """
    INSERT INTO accountbooks (date, type, breakdown, price)
    VALUES (%s, %s, %s, %s)
    """
    values = (accountbook.date, accountbook.type_,
              accountbook.breakdown, accountbook.price)

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, values)
    mydb.commit()

    return {"message": "Accountbook created successfully"}


# 指定されたIDの家計簿を更新するAPI
@app.put('/accountbooks/{accountbook_id}', status_code=204)
def update(accountbook_id: int, accountbook: Accountbook, response: Response):
    if is_accountbook_id_exists(accountbook_id):
        sql = """
        UPDATE accountbooks
        SET date = %s, type = %s, breakdown = %s, price = %s
        WHERE id = %s
        """
        values = (accountbook.date, accountbook.type_,
                  accountbook.breakdown, accountbook.price, accountbook_id)

        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql, values)
        mydb.commit()

        return {"message": "Accountbook updated successfully"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Accountbook not found"}


# 指定されたIDの家計簿を削除するAPI
@app.delete('/accountbooks/{accountbook_id}', status_code=204)
def delete(accountbook_id: int, response: Response):
    if is_accountbook_id_exists(accountbook_id):
        sql = """
        DELETE FROM accountbooks
        WHERE id = %s
        """
        value = (accountbook_id,)

        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql, value)
        mydb.commit()

        return {"message": "Accountbook deleted successfully"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Accountbook not found"}


# IDの存在をチェックする
def is_accountbook_id_exists(accountbook_id: int):
    sql = """
    SELECT * FROM accountbooks
    WHERE id = %s
    """
    value = (accountbook_id, )

    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql, value)
    result = cursor.fetchone()

    return result is not None
