import system
from item import Item
from telegram_globals import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from globals import *

# @mipt_ratings_botd
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

is_read_new_element_of_list = False
is_read_name_of_list=False
is_read_name_of_list_for_add_item = False
is_compared = False
is_less = False
name_of_new_list = ''
name_of_list_for_add_item = ''
name_of_list_for_delete_item = ''
name_of_list_for_sorted = ''
new_list = []

is_read_photo = False
name_of_item_for_add = ''

layer1 = []
layer2 = []
first_block = []
second_block = []
res_block = []
is_right_best = False
item_1 = Item('')
item_2 = Item('')
name_of_sortd_list = ''

async def Sort(list_of_elements, chat_id):
    global name_of_list_for_sorted
    if len(list_of_elements) == 0:
        system.saveSortedList(name_of_list_for_sorted, list_of_elements)
        return
    for element in list_of_elements:
        global layer1
        layer1.append([element])
    await ContinueSort(chat_id)

async def ContinueSort(chat_id):
    global layer1
    global layer2
    global name_of_list_for_sorted
    if len(layer1) == 0:
        layer1 = layer2[:]
        layer2 = []
        if len(layer1) <= 1:
            system.saveSortedList(name_of_list_for_sorted, layer1[0][:])
            layer1 = []
        else:
            await ContinueSort(chat_id)
        return
    if len(layer1) == 1:
        layer2.append(layer1[0][:])
        layer1 = []
        await ContinueSort(chat_id)
        return
    global first_block
    global second_block
    first_block = layer1[0][:]
    second_block = layer1[1][:]
    del layer1[0]
    del layer1[0]
    await Merge(chat_id)

async def Merge(chat_id):
    global res_block
    global first_block
    global second_block
    if len(first_block) == len(second_block) == 0:
        layer2.append(res_block[:])
        res_block = []
        await ContinueSort(chat_id)
        return
    if len(first_block) == 0:
        res_block += second_block
        second_block = []
        await Merge(chat_id)
        return
    if len(second_block) == 0:
        res_block += first_block
        first_block = []
        await Merge(chat_id)
        return
    global item_1
    global item_2
    item_1 = first_block[0]
    item_2 = second_block[0]
    await Compare(item_1, item_2, chat_id)
    
async def EndCompare(chat_id):
    global res_block
    global item_1
    global item_2
    global is_right_best
    global first_block
    global second_block

    if is_right_best:
        res_block.append(item_1)
        del first_block[0]
    else:
        res_block.append(item_2)
        del second_block[0]
    await Merge(chat_id)
    return
    
async def Compare(first_item: Item, second_item: Item, chat_id):
    temp_inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    tib1 = types.InlineKeyboardButton(text=first_item.name, callback_data=CALLBACK_COMPARE_DATA_FIRST)
    tib2 = types.InlineKeyboardButton(text=second_item.name, callback_data=CALLBACK_COMPARE_DATA_SECOND)
    temp_inline_keyboard.add(tib1, tib2)
    photos = types.MediaGroup()
    photos.attach_photo(first_item.photo)
    photos.attach_photo(second_item.photo, caption=f'{first_item.name} or {second_item.name}')
    await bot.send_message(chat_id=chat_id, text=MESSAGE_CHOOSE, reply_markup=temp_inline_keyboard)
    await bot.send_media_group(chat_id, media=photos)

@dp.message_handler(commands=[START_COMMAND])
async def process_start_command(message: types.Message):
    await message.answer(HELLO_MESSAGE)

@dp.message_handler(commands=[HELP_COMMAND])
async def process_help_command(message: types.Message):
    helpTable = types.InlineKeyboardMarkup(row_width=1)
    ibh_1 = types.InlineKeyboardButton(text=PRINT_LIST_COMMAND, callback_data=CALLBACK_PRINT_LIST_COMMAND)
    ibh_2 = types.InlineKeyboardButton(text=PRINT_RATING_COMMAND, callback_data=CALLBACK_PRINT_RATING_COMMAND)
    ibh_3 = types.InlineKeyboardButton(text=BUILD_COMMAND, callback_data=CALLBACK_BUILD_COMMAND)
    ibh_4 = types.InlineKeyboardButton(text=DELETE_COMMAND, callback_data=CALLBACK_DELETE_COMMAND)
    ibh_5 = types.InlineKeyboardButton(text=ADD_LIST_COMMAND, callback_data=CALLBACK_ADD_LIST_COMMAND)
    ibh_6 = types.InlineKeyboardButton(text=ADD_ITEM_COMMAND, callback_data=CALLBACK_ADD_ITEM_COMMAND)
    ibh_7 = types.InlineKeyboardButton(text=DELETE_ITEM_COMMAND, callback_data=CALLBACK_DELETE_ITEM_COMMAND)
    helpTable.add(ibh_1, ibh_2, ibh_3, ibh_4, ibh_5, ibh_6, ibh_7)
    await bot.send_message(chat_id=message.chat.id, text=HELP_MESSAGE, reply_markup=helpTable)

async def print_enter_name_tabel(chat_id):
    temp_inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    tib1 = types.InlineKeyboardButton(text=ENTER_NAME, callback_data=CALLBACK_ENTER_NAME)
    tib2 = types.InlineKeyboardButton(text=CREAT_LIST, callback_data=CALLBACK_CREAT_LIST)
    temp_inline_keyboard.add(tib1, tib2)
    await bot.send_message(chat_id=chat_id, text=QUESTION_ABOUT_CREATING_LIST, reply_markup=temp_inline_keyboard)

@dp.message_handler()
async def echo(msg: types.Message):
    global is_read_new_element_of_list
    global is_read_name_of_list
    global name_of_new_list
    global new_list

    global name_of_item_for_add
    global name_of_list_for_add_item
    global is_read_name_of_list_for_add_item
    global is_read_photo

    if is_read_name_of_list or is_read_new_element_of_list:
        if is_read_name_of_list:
            name_of_new_list = msg.text
            is_read_name_of_list = False
        elif is_read_new_element_of_list:
            new_list.append(Item(msg.text))
            is_read_photo = True
        if not is_read_photo:
            await print_enter_name_tabel(msg.chat.id)
    if is_read_name_of_list_for_add_item:
        name_of_item_for_add = msg.text
        is_read_photo = True

@dp.message_handler(content_types=[PHOTO_COMMAND])
async def scan_message(msg: types.Message):
    global is_read_photo
    global new_list
    global is_read_new_element_of_list
    global is_read_name_of_list_for_add_item
    global name_of_list_for_add_item
    global name_of_item_for_add

    if is_read_photo:
        is_read_photo = False
        document_id = msg.photo[0].file_id
        if is_read_name_of_list_for_add_item:
            system.saveItem(name_of_item_for_add, name_of_list_for_add_item, photo=str(document_id))
            is_read_name_of_list_for_add_item = False
            return
        else:
            new_list[-1].photo = str(document_id)
            is_read_new_element_of_list = False
            await print_enter_name_tabel(msg.chat.id)

async def print_list(chat_id, is_sorted=False, callback_added=''):
    names_of_lists = system.uploadNamesOfLists(is_sorted)
    temp_inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for name_list in names_of_lists:
        tib = types.InlineKeyboardButton(text=name_list, callback_data=name_list+callback_added)
        temp_inline_keyboard.add(tib)
    await bot.send_message(chat_id=chat_id, text="choose list", reply_markup=temp_inline_keyboard)

@dp.callback_query_handler()
async def callback(callback: types.CallbackQuery):
    global is_read_name_of_list
    global is_read_new_element_of_list
    global is_read_name_of_list_for_add_item
    global new_list
    global name_of_new_list
    global name_of_list_for_add_item
    global name_of_list_for_delete_item
    global name_of_list_for_sorted
    global is_right_best
    global name_of_list_for_sorted

    chat_id = callback.message.chat.id

    if callback.data == CALLBACK_PRINT_LIST_COMMAND:
        await print_list(chat_id, is_sorted=False, callback_added=PRINT_CALLBACK_ADDED)

    elif callback.data == CALLBACK_PRINT_RATING_COMMAND:
        await print_list(chat_id, is_sorted=True, callback_added=PRINT_CALLBACK_ADDED)

    elif callback.data == CALLBACK_BUILD_COMMAND:
        await print_list(chat_id, is_sorted=False, callback_added=SORTED_CALLBACK_ADDED)
        
    elif callback.data == CALLBACK_DELETE_COMMAND:
        await print_list(chat_id, is_sorted=False, callback_added=DELETE_CALLBACK_ADDED)

    elif callback.data == CALLBACK_ADD_LIST_COMMAND:
        temp_inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
        tib1 = types.InlineKeyboardButton(text='enter name', callback_data=CALLBACK_ENTER_NAME_OF_LIST)
        tib2 = types.InlineKeyboardButton(text='cancel', callback_data=CALLBACK_CANCEL_CREAT_NEW_LIST)
        temp_inline_keyboard.add(tib1, tib2)
        await bot.send_message(chat_id=chat_id, text='press on button enter na me or cancel', reply_markup=temp_inline_keyboard)

    elif callback.data == CALLBACK_ENTER_NAME_OF_LIST:
        is_read_name_of_list = True

    elif callback.data == CALLBACK_CANCEL_CREAT_NEW_LIST:
        is_read_name_of_list = is_read_new_element_of_list = False
        name_of_new_list=''
        new_list = []

    elif callback.data == CALLBACK_ENTER_NAME:
        is_read_new_element_of_list = True

    elif callback.data == CALLBACK_CREAT_LIST:
        await bot.send_message(chat_id=chat_id, text='new list was created')
        system.saveList(name_of_new_list, new_list)
        name_of_new_list = ''
        new_list = []
        is_read_new_element_of_list = is_read_name_of_list = False
    
    elif callback.data == CALLBACK_ADD_ITEM_COMMAND:
        await print_list(chat_id=chat_id, is_sorted=False, callback_added=ADD_ITEM_CALLBACK_ADDED)

    elif callback.data == CALLBACK_DELETE_ITEM_COMMAND:
        await print_list(chat_id=chat_id, is_sorted=False, callback_added=DELETE_ITEM_FROM_LIST_CALLBACK_ADDED)
        
    elif callback.data == CALLBACK_COMPARE_DATA_FIRST:
        is_right_best = False
        await EndCompare(chat_id)

    elif callback.data == CALLBACK_COMPARE_DATA_SECOND:
        is_right_best = True
        await EndCompare(chat_id)
    else:
        is_founded_callback_data = False

        names_of_lists = system.uploadNamesOfLists(False)
        names_of_ratings = system.uploadNamesOfLists(True)

        names_of_all = names_of_ratings + names_of_lists
        for name in names_of_all:
            if callback.data == (name + PRINT_CALLBACK_ADDED):
                current_list = system.uploadList(name)
                curent_list_text = ''
                counter = 1
                current_list = current_list[::-1]
                for element in current_list:
                    curent_list_text += str(counter) + ') ' + element.name + '\n'
                    counter += 1
                await bot.send_message(chat_id=chat_id, text=curent_list_text)
                is_founded_callback_data = True
                break
            if callback.data == (name + DELETE_CALLBACK_ADDED):
                system.deleteList(name)
                is_founded_callback_data = True
                break
            if callback.data == (name + ADD_ITEM_CALLBACK_ADDED):
                await bot.send_message(chat_id=chat_id, text=MESSAGE_ENTER_NAME_OF_ITEM)
                name_of_list_for_add_item = name
                is_read_name_of_list_for_add_item = True
                is_founded_callback_data = True
                break
            if callback.data == (name + DELETE_ITEM_FROM_LIST_CALLBACK_ADDED):
                name_of_list_for_delete_item = name
                current_list = system.uploadList(name)
                temp_inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
                for element in current_list:
                    tib = types.InlineKeyboardButton(text=element.name, callback_data= element.name + '_delete_item')
                    temp_inline_keyboard.add(tib)
                await bot.send_message(chat_id=chat_id, text='choose element for delete', reply_markup=temp_inline_keyboard)
                is_founded_callback_data = True
                break
            if callback.data == (name + SORTED_CALLBACK_ADDED):
                sorted_list = system.uploadList(name)
                name_of_list_for_sorted = name
                await Sort(sorted_list, chat_id)
                is_founded_callback_data = True
                break
        
        if not is_founded_callback_data:
            if name_of_list_for_delete_item != '':
                system.deleteItem(callback.data[:-12], name_of_list_for_delete_item)
                name_of_list_for_delete_item = ''
                is_founded_callback_data = True
    await callback.answer()
    await bot.delete_message(chat_id, callback.message.message_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
