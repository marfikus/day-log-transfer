
import re

DAY_LOG_YEAR = "day_log_year.txt"
DAY_LOG_WEEK = "day_log_week.txt"

with open(DAY_LOG_WEEK, "r", encoding="utf-8") as day_log_week:
    # номер текущей строки:
    line_num = 0
    # номер строки с последней встретившейся датой:
    last_date_line_num = 0
    lines = []
    for line in day_log_week:
        # print(line)
        lines.append(line)
        # ищем дату вида: "12.7.20 Sun 8:38"
        result = re.findall(r"^\d{1,2}\.\d{1,2}\.\d{1,2} \w{2,3} \d{1,2}:\d{1,2}$", line)
        if len(result) != 0:
            # print(result)
            # если нашли, то запоминаем номер строки:
            last_date_line_num = line_num
        line_num += 1

# print(last_date_line_num)
# обрезаем список строк с конца до строки с последней датой
# (убираем последний день):
last_week = lines[:last_date_line_num - 1]
# print(last_week)
# отделяем последний день:
last_day = lines[last_date_line_num:]
# print(last_day)

# дописываем список в файл общего лога:
# with open(DAY_LOG_YEAR, "a", encoding="utf-8") as f:
with open("test2.txt", "a", encoding="utf-8") as f:
    f.write("\n\n")
    f.writelines(last_week)
