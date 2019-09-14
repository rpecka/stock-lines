import csv
import matplotlib
import random

reader = csv.reader(open('/Users/rico/Downloads/S&P 500 Historical Data (3).csv'))
percent_change_dict ={}
balance = 500

def count_cat(dict, categ):
    count = 0
    for x in percent_change_dict:
        if dict[x] == categ:
            count = count + 1
    return count

for r in reader:
    curr_date = r[0]
    curr_percent = float(r[6].strip('%'))
    curr_category = ""
    if curr_percent < -1.60:
        curr_category = "drastic decrease"
    elif curr_percent < -0.07:
        curr_category = "decrease"
    elif curr_percent < 0.2:
        curr_category = "no change"
    elif curr_percent < 1.93:
        curr_category = "increase"
    else:
        curr_category = "drastic increase"
    percent_change_dict[curr_date] = curr_category

while True:
    count_dras_low = count_cat(percent_change_dict, "drastic decrease")
    count_low = count_cat(percent_change_dict, "decrease")
    count_no_change = count_cat(percent_change_dict, "no change")
    count_high = count_cat(percent_change_dict, "increase")
    count_dras_high = count_cat(percent_change_dict, "drastic increase")

    curr_pick = random.choice(list(percent_change_dict))

    if percent_change_dict[curr_pick] == "drastic decrease" and count_dras_low > balance:
        percent_change_dict.pop(curr_pick)
    elif percent_change_dict[curr_pick] == "decrease" and count_low > balance:
        percent_change_dict.pop(curr_pick)
    elif percent_change_dict[curr_pick] == "no change" and count_no_change > balance:
        percent_change_dict.pop(curr_pick)
    elif percent_change_dict[curr_pick] == "increase" and count_high > balance:
        percent_change_dict.pop(curr_pick)
    elif percent_change_dict[curr_pick] == "drastic increase" and count_dras_high > balance:
        percent_change_dict.pop(curr_pick)
    elif count_dras_low <= balance and count_low <= balance and count_no_change <= balance and count_high <= balance and count_dras_high <= balance:
        break

num_5 = [count_dras_low, count_low, count_no_change, count_high, count_dras_high]


    

