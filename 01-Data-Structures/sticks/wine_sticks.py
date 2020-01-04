"""
appends JSON wine records from given data, formats and sort'em,
output is JSON file, contains summary information by built-in parameters
"""

winedata_full = []
avg_wine_price_by_origin = []
ratings_count = []


def string_comb(raw_str):
    form_str = ' '.join(
        raw_str[1:-1].split()
    ).replace(
        'price": ', 'price": "'
    ).replace(
        ', "designation', '", "designation'
    ).replace(
        'null', '"None"'
    )
    return form_str.split('": "')


def flatten(nonflat_arr):
    flat_arr = []
    for m in nonflat_arr:
        flat_arr.extend(m)
    return flat_arr


def parser(inp_json):
    json_arr = set()
    for s in inp_json[2:-2].split('}, {'):
        json_arr.add(s)
    for x in json_arr:
        temp = flatten([i.split('", "', 2) for i in string_comb(x)])
        curr_rec = {
            temp[k]: temp[k + 1] for k in range(0, len(temp), 2)
        }
        winedata_full.append(curr_rec)


def sort_by_price(wine_record):
    if wine_record['price'] == '"None"':
        return 0
    return int(wine_record['price'])


def summary(kind):
    all_coinc = []
    for w in winedata_full:
        if kind in w['variety']:
            all_coinc.append(w)
    if all_coinc == []:
        return f"no records on {kind} were found"

    prices_arr = [
        int(r['price']) for r in all_coinc if r['price'] != '"None"'
    ]

    avarege_price = round(sum(prices_arr) / len(prices_arr), 1)
    min_price = min(prices_arr)
    max_price = max(prices_arr)

    regions = {}
    for i in all_coinc:
        if i['region_1'] == 'None':
            continue
        elif i['region_1'] not in regions:
            regions[i['region_1']] = 1
        else:
            regions[i['region_1']] = +1
        if i['region_2'] == 'None':
            continue
        elif i['region_2'] not in regions:
            regions[i['region_2']] = 1
        else:
            regions[i['region_2']] = +1
    regions = [[r, regions[r]] for r in regions]
    regions.sort(key=lambda x: x[1])
    regions.sort()

    most_common_region = [i for i in regions if i[1] == regions[0][1]]

    countries = {}
    for i in all_coinc:
        if i['country'] == 'None':
            continue
        elif i['country'] not in countries:
            countries[i['country']] = 1
        else:
            countries[i['country']] = +1
    countries = [[c, countries[c]] for c in countries]
    countries.sort(key=lambda x: x[1])
    countries.sort()

    most_common_country = [n for n in countries if n[1] == countries[0][1]]

    avarage_score = int(
        sum([int(i['points']) for i in all_coinc]) / len(all_coinc)
    )

    return f'''avarege_price: {avarege_price},
    min_price: {min_price},
    max_price: {max_price},
    most_common_region: {most_common_region},
    most_common_country: {most_common_country},
    avarage_score: {avarage_score}'''


def most_expensive_wine(w_data):
    max_price = w_data[0]['price']
    most_expensive_arr = []
    for r in w_data:
        if r['price'] == max_price:
            most_expensive_arr.append(r)
        else:
            break
    print(max_price)
    print(w_data[0]['price'])
    return most_expensive_arr


def cheapest_wine(w_data):
    cheap_arr = []
    for w in reversed(w_data):
        if w['price'] != '"None"':
            min_price = w['price']
            break
    for r in reversed(w_data):
        if r['price'] <= min_price:
            cheap_arr.append(r)
        else:
            break
    return cheap_arr


def highest_score(w_data):
    hi_score = int(w_data[0]['points'])
    highest_score_arr = []
    for r in w_data:
        if int(r['points']) >= hi_score:
            highest_score_arr.append(r)
        else:
            break
    return highest_score_arr


def lowest_score(w_data):
    lowest_score_arr = []
    for w in reversed(w_data):
        if w['points'] != '"None"':
            low_score = int(w['points'])
            break
    for r in reversed(w_data):
        if int(r['points']) <= low_score:
            lowest_score_arr.append(r)
        else:
            break
    return lowest_score_arr


def most_expensive_country(w_data):
    unsort_prc = {}
    for w in w_data:
        if w['price'] == '"None"':
            continue
        elif w['country'] not in unsort_prc:
            w_count = 1
            sum_price = int(w['price'])
            unsort_prc[w['country']] = [sum_price, w_count]
        else:
            unsort_prc[w['country']][0] += int(w['price'])
            unsort_prc[w['country']][1] += 1
    global avg_wine_price_by_origin
    avg_wine_price_by_origin = [
        [i, int(unsort_prc[i][0] / unsort_prc[i][1])] for i in unsort_prc
    ]
    avg_wine_price_by_origin.sort(key=lambda x: x[1], reverse=True)
    return avg_wine_price_by_origin[0]


def cheapest_country(w_data):
    return w_data[-1]


def most_rated_country(w_data):
    unsort_cnt = {}
    for w in w_data:
        if w['country'] == 'None':
            continue
        elif w['country'] not in unsort_cnt:
            unsort_cnt[w['country']] = 1
        else:
            unsort_cnt[w['country']] += 1
    global ratings_count
    ratings_count = [[i, unsort_cnt[i]] for i in unsort_cnt]
    ratings_count.sort(key=lambda x: x[1], reverse=True)
    return ratings_count[0]


def most_underrated_country(w_data):
    return w_data[-1]


def most_active_commentator(w_data):
    commentators = {}
    for w in w_data:
        if w['taster_name'] == 'None':
            continue
        elif w['taster_name'] not in commentators:
            commentators[w['taster_name']] = 1
        else:
            commentators[w['taster_name']] += 1
    commentators = [[i, commentators[i]] for i in commentators]
    commentators.sort(key=lambda x: x[1], reverse=True)
    return commentators[0]


with open("./winedata_1.json") as wd_1:
    for line in wd_1:
        parser(line)

with open("./winedata_2.json") as wd_2:
    for line in wd_2:
        parser(line)

winedata_full.sort(key=lambda x: x['title'])
winedata_full.sort(key=sort_by_price, reverse=True)

w_data_by_points = winedata_full
w_data_by_points.sort(key=lambda x: int(x['points']), reverse=True)

extr_data = {
    "Gewurztraminer_summ": summary('Gewurztraminer'),
    "Riesling_summ": summary('Riesling'),
    "Merlot_summ": summary('Merlot'),
    "Madera_summ": summary('Madera'),
    "Tempranillo_summ": summary('Tempranillo'),
    "Red_Blend_summ": summary('Red Blend'),
    "most_ex_wine": most_expensive_wine(winedata_full),
    "chp_wine": cheapest_wine(winedata_full),
    "hi_scr": highest_score(w_data_by_points),
    "low_scr": lowest_score(w_data_by_points),
    "most_cnt": most_expensive_country(winedata_full),
    "chp_cnt": cheapest_country(avg_wine_price_by_origin),
    "rate_cnt": most_rated_country(winedata_full),
    "undr_cnt": most_underrated_country(ratings_count),
    "act_cnt": most_active_commentator(winedata_full)
}

extr_str = """{{"statistics": {{
                "wine": {{
                        "Gewurztraminer": {Gewurztraminer_summ}
                        }},
                        {{
                        "Riesling": {Riesling_summ}
                        }},
                        {{
                        "Merlot": {Merlot_summ}
                        }},
                        {{
                        "Madera": {Madera_summ}
                        }},
                        {{
                        "Tempranillo": {Tempranillo_summ}
                        }},
                        {{
                        "Red Blend": {Red_Blend_summ}
                        }},
                "most_expensive_wine": {most_ex_wine},
                "cheapest_wine": {chp_wine},
                "highest_score": {hi_scr},
                "lowest_score": {low_scr},
                "most_expensive_country": {most_cnt},
                "cheapest_country": {chp_cnt},
                "most_rated_country": {rate_cnt},
                "underrated_country": {undr_cnt},
                "most_active_commentator": {act_cnt}
        }}
}}""".format(**extr_data)

# with open('./stats.json', 'a') as ex:
#     ex.write(extr_str)
