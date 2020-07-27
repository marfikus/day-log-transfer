
import re

DAY_LOG_YEAR = "day_log_20.txt"
DAY_LOG_WEEK = "day_log_week.txt"

with open(DAY_LOG_WEEK, "r", encoding="utf-8") as day_log_week:
    # номер текущей строки:
    line_num = 0
    # номер строки с последней встретившейся датой:
    last_date_line_num = 0
    # счётчик найденных строк с датой:
    date_line_count = 0
    lines = []
    for line in day_log_week:
        lines.append(line)
        # ищем дату вида: "12.7.20 Sun 8:38"
        result = re.findall(r"^\d{1,2}\.\d{1,2}\.\d{1,2} \w{2,3} \d{1,2}:\d{1,2}$", line)
        if len(result) != 0:
            # если нашли, то запоминаем номер строки:
            last_date_line_num = line_num
            date_line_count += 1
        line_num += 1

# защита от повторного запуска 
if date_line_count <= 1:
    print("Not enough days in the log for transfer")
    exit()

# обрезаем список строк с конца до строки с последней датой
# (убираем последний день):
last_week = lines[:last_date_line_num - 1]
# отделяем последний день:
last_day = lines[last_date_line_num:]

# дописываем список в файл общего лога:
with open(DAY_LOG_YEAR, "a", encoding="utf-8") as f:
    f.write("\n\n")
    f.writelines(last_week)

# обновляем файл недельного лога (оставляем только последний день):
with open(DAY_LOG_WEEK, "w", encoding="utf-8") as f:
    f.writelines(last_day)

