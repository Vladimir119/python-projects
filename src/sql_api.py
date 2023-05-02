import sqlite3
from globals import *

con = sqlite3.connect(DATA_BASE_NAME)
cursor = con.cursor()
cursor.execute(INIT_SQL)


def getItemsInList(user_id: str, list_id: str) -> list:
    cursor.execute(GET_ITEMS.format(user_id, list_id))
    rows = cursor.fetchall()
    return [(row[0], row[1]) for row in rows]


def getNamesOfLists(
        user_id: str,
        is_sorted: bool,
        is_favorite: bool = False) -> list:
    cursor.execute(
        (GET_FAVORITES if is_favorite else GET_RATINGS if is_sorted else GET_LISTS).format(user_id))
    rows = cursor.fetchall()
    names = set()
    for row in rows:
        names.add(row[0])
    return list(names)


def insertList(
        user_id: str,
        name: str,
        new_list: list,
        is_sorted: bool,
        is_favorite: bool) -> None:
    data = []
    for i, item in enumerate(new_list):
        data.append(
            (user_id,
             name,
             i + 1,
             item.name,
             is_sorted,
             is_favorite,
             item.photo))
    cursor.executemany(INSERT_LIST, data)
    con.commit()


def isSorted(user_id: str, name: str) -> int:
    cursor.execute(IS_SORTED.format(user_id, name))
    try:
        return cursor.fetchone()[0]
    except BaseException:
        return 0


def isFavorite(user_id: str, name: str) -> int:
    cursor.execute(IS_FAVORITE.format(user_id, name))
    try:
        return cursor.fetchone()[0]
    except BaseException:
        return 0


def insertItem(user_id: str, name: str, new_item: str, photo: str='') -> None:
    cursor.execute(INSERT_LIST, (user_id, name, len(getItemsInList(
        user_id, name)) + 1, new_item, isSorted(user_id, name), isFavorite(user_id, name), photo))
    con.commit()


def deleteItem(user: str, name_of_list: str, name_of_item: str) -> None:
    cursor.execute(DELETE_ITEM.format(user, name_of_list, name_of_item))
    con.commit()


def deleteList(user_id: str, list_id: str) -> None:
    cursor.execute(DELETE_LIST.format(user_id, list_id))
    con.commit()
