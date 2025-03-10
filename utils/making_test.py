import sqlite3


def make_test(
        file
):
    try:
        check_file(file)
    except Exception as e:
        result = f'Во время проверки файла возникла ошибка {e}'
    with open(file, 'r+', encoding='utf-8') as incoming_file:
        con = sqlite3.connect('db.sqlite')
        cur = con.cursor()
        for row in incoming_file:
            if not row:
                continue
            row = row.replace('\n', '')
            splited_row = row.split(sep=', ')
            question, answer = splited_row[0], splited_row[1]
            cur.execute(f'''
                ''')




def check_file(file):
    with open(file, 'r+', encoding='utf-8') as f:
        for row in f:
            print(row)
            if not row:
                continue
            row = row.replace('\n', '')
            splited_row = row.split(sep=', ')
            question, answer = splited_row[0], splited_row[1]
            if len(splited_row) != 2:
                raise ValueError(f'Неправильное количество данных в строке {row}')
            elif question.isdigit() or not answer.isdigit():
                raise ValueError(f'Неправильное значение в строке {row}')
            elif 0 >= int(answer) or int(answer) > 2:
                raise ValueError(f'Значение ответа в строке {row} должно быть от 1 до 2')
            word_1, word_2 = question.split(sep='/')
            if word_1 == word_1.lower() or word_2 == word_2.lower():
                raise ValueError(
                    f'В строке {row} не поставлено ударение'
                )
check_file('test.txt')