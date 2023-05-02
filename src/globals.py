WRONG_COMPARE = "Write only 1 or 2."
COMPARE_MESSAGE = "{} or {}? (1 or 2):"
FIRST = "1"
SECOND = "2"

WRONG_MESSAGE = "Wrong name."
NO_LISTS = "There are no lists."
NO_RATINGS = "There are no ratings."
CHOOSE_MESSAGE = "Choose one or write -1:"
NEW_RATING = "This is your new rating:"
RATING_SAVED = "Rating was saved."
LIST_SAVED = "List was saved."
NEW_LIST = "Enter name of your list or -1 if you do not want to build list"
NEXT_ITEM = "Enter a new item to list or -1 if you want to finish build list"
ADD_ITEM = "Enter name of your new item or -1 if you do not want to add item"
ITEM_SAVED = "Item was saved."
STOP_COMMAND = "-1"

COMMANDS = """===========
Commands:
help
lists
ratings
print list
print rating
build
delete
add list
add item
exit"""
WRONG_COMMAND = "{}: command not found."
HELP_COMMAND = "help"
LISTS_COMMAND = "lists"
PRINT_LIST_COMMAND = "print list"
PRINT_RATING_COMMAND = "print rating"
RATINGS_COMMAND = "ratings"
BUILD_COMMAND = "build"
ADD_LIST_COMMAND = "add list"
ADD_ITEM_COMMAND = "add item"
DELETE_COMMAND = "delete"
DELETE_ITEM_COMMAND = "delete item"
EXIT_COMMAND = "exit"
HELLO_MESSAGE = "Hello!"
SEPARATOR = "==========="

DEFAULT_NAME = "default"

DATA_BASE_NAME = "src/data.db"
INIT_SQL = "CREATE TABLE IF NOT EXISTS items(user_id TEXT, list_id TEXT, place INT, name TEXT, is_sorted BIT, is_favorite BIT, photo TEXT)"
GET_ITEMS = "SELECT name, photo FROM items WHERE user_id = '{}' AND list_id = '{}' ORDER BY place ASC"
GET_LISTS = "SELECT list_id FROM items WHERE user_id = '{}'"
GET_RATINGS = "SELECT list_id FROM items WHERE user_id = '{}' AND is_sorted = 1"
GET_FAVORITES = "SELECT list_id FROM items WHERE user_id = '{}' AND is_sorted = 1 AND is_favorite = 1"
INSERT_LIST = "INSERT INTO items VALUES(?, ?, ?, ?, ?, ?, ?)"
DELETE_LIST = "DELETE FROM items WHERE user_id = '{}' AND list_id = '{}'"
DELETE_ITEM = "DELETE FROM items WHERE user_id = '{}' AND list_id = '{}' AND name = '{}'"
IS_SORTED = "SELECT is_sorted FROM items WHERE user_id = '{}' AND list_id = '{}'"
IS_FAVORITE = "SELECT is_favorite FROM items WHERE user_id = '{}' AND list_id = '{}'"
