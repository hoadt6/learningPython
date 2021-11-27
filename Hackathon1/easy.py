# 1
def day_diff(release_date, code_complete_day):
    from datetime import datetime 
    format_release = "%d/%m/%Y"
    dt1 = datetime.strptime(release_date,format_release)
    format_complete = "%Y-%d-%m"
    dt2 = datetime.strptime(code_complete_day,format_complete)
    day_testing = dt1 - dt2
    return day_testing.days
# 2
def alpha_num(sentence):
    list_str=[]
    sentence= sentence.split()
    for i in sentence:
        if i.isalpha() == False and i.isalnum() == True: 
            list_str.append(i)
    return list_str