HELP_MESSAGE = """вас приветствует телеграм бот @mipt_ratings_bot
он поддерживает следующий функционал:
    1)добавление новых списков элементов, для этого воспользуйтесь командой add list:
     нажмите на кнопку ввода названия листа потом введите имя листа, после чего вам предлагается кнопка ввести имя элемента или создать лист
     введите имя элемента после чего вставьте фотографию этого элемента, после чего повторяйте процесс пока не соберете нужный лист
    2)создание новых рейтингов из списка, для этого воспользуйтесь командой build:
      вам предаставиться возможность выбрать один из списков добавленных заранее, если списки еще не были добавлены, то сначала добавьте список омандой add list
    3)просмотром уже созданных рейтингов и списков, команды print rating и print lists соответственно:
      выберите список или рейтинг который хотите посмотреть
    4)удаление листа, команда delete
      выберите список которой хотите удалить (ВМЕСТЕ С УДАЛЕНИЕ СПИСКА УДАЛЯЕТЬСЯ РЕЙТИНГ СОЗДАННЫЙ ПО ЭТОМУ ЛИСТУ!)
    5)редактирование листа команды: delete item и add item
      выберите лист, и элемент которыйй хотите удалить,
      если вы хотите добавить элемент в список, то нужно повторить процедуру описанную в команде add list
"""
CALLBACK_COMPARE_DATA_FIRST = 'callback_data_first_is_best'
CALLBACK_COMPARE_DATA_SECOND = 'callback_data_second_is_best'
CALLBACK_PRINT_LIST_COMMAND = 'callback_data_print_list'
CALLBACK_PRINT_RATING_COMMAND = 'callback_data_print_ratings'
CALLBACK_BUILD_COMMAND = 'callback_data_build'
CALLBACK_DELETE_COMMAND = 'callback_data_delete'
CALLBACK_ADD_ITEM_COMMAND = 'callback_data_add_item'
CALLBACK_ADD_LIST_COMMAND = 'callback_data_add_list'
CALLBACK_DELETE_ITEM_COMMAND = 'callback_data_delete_item'
CALLBACK_ENTER_NAME_OF_LIST = 'callback_data_enter_name_of_list'

START_COMMAND = 'start'
MESSAGE_CHOOSE = 'choose best'
MESSAGE_CHOOSE_LIST = 'choose list'
MESSAGE_CHOOSE_RATINGS = 'choose ratings'
MESSAGE_CHOOSE_LIST_FOR_DELETE = 'choose list for delete item in list'

CALLBACK_ENTER_NAME_OF_ITEM = "callback_enter_name_of_item"
MESSAGE_ENTER_NAME_OF_LIST = "enter name of list"
MESSAGE_ENTER_NAME_OF_ITEM = "enter name of item"
CALLBACK_CANCEL_CREAT_NEW_LIST = "callback_cancel_of_creat_new_list"
PHOTO_COMMAND = 'photo'

ENTER_NAME = "enter name of element"
CALLBACK_ENTER_NAME = "callback_data_enter_name"
CREAT_LIST = "create list"
CALLBACK_CREAT_LIST =  "callback_data_creat_list"
QUESTION_ABOUT_CREATING_LIST = "enter new element name or creat list"

PRINT_CALLBACK_ADDED = "_print_callback"
SORTED_CALLBACK_ADDED = "_sorted_callback"
DELETE_CALLBACK_ADDED = "_delete_callback"
ADD_ITEM_CALLBACK_ADDED = "_add_item"
DELETE_ITEM_FROM_LIST_CALLBACK_ADDED = "_delete_item_from_list"
