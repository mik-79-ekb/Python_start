"""
Task 5.7
"""
import json
with open('text_5.7.txt', 'r', encoding="utf-8") as test_file:
    company_list = test_file.readlines()
    comp_dict = {}
    ave_profit = {}
    result = []
    sum_profit = 0
    for x in range(len(company_list)):
        company = company_list[x].split(' ')
        if int(company[2]) > int(company[3]):
            sum_profit += sum_profit + (int(company[2]) - int(company[3]))
        comp_dict[company[0]] = (int(company[2]) - int(company[3]))
        ave_profit["Средняя прибыль"] = (sum_profit/len(company_list))
    result = [comp_dict, ave_profit]
with open("text_5.7.json", "w", encoding="utf-8") as test_json:
    json.dump(result, test_json)
    #