from .scraper import getData
from .scorer import score_article
import json
from collections import defaultdict
import os

if __name__ == '__main__':
    print("Alive")

    print("Scraping articles...")
    data = getData()
    print("Done scraping!")
    # Fore-xFactory Weight: 70% Hotest 30% Latest
    print("Grading data...")
    latest_graded = []
    hotest_graded = []
    graded_data = [latest_graded, hotest_graded]
    enumerate(graded_data)

    for session_index, section in enumerate(data):
        graded_data[session_index] = []
        for article_index, article in enumerate(section):
            score = score_article(data[session_index][article_index])
            graded_data[session_index].append(score)
    print("Graded data!")
    # with open('graded_data.json', 'r') as file:
    #     graded_data = json.load(file)

    print("Maniputaling data...")
    currency_totals_1 = defaultdict(lambda: {'total': 0, 'count': 0})
    currency_totals_2 = defaultdict(lambda: {'total': 0, 'count': 0})
    weight = 0.6

    for session_index, session in enumerate(graded_data):
        for json_string in session:
            currency_data = json.loads(json_string)

            # Debug print to check the structure of currency_data
            print("currency_data:", currency_data)

            for currency, value in currency_data.items():
                 # Ensure 'value' is a number before processing
                if isinstance(value, (int, float)):
                    if session_index == 0:
                        currency_totals_1[currency]['total'] += value * (1 - weight)
                        currency_totals_1[currency]['count'] += 1
                    else:
                        currency_totals_2[currency]['total'] += value * weight
                        currency_totals_2[currency]['count'] += 1
                else:
                    print(f"Skipping non-numeric value for {currency}: {value}")

    currency_averages_1 = {currency: totals['total'] / totals['count']
                           for currency, totals in currency_totals_1.items()}
    currency_averages_2 = {currency: totals['total'] / totals['count']
                           for currency, totals in currency_totals_2.items()}

    combined_dict = {}
    for key, value in currency_averages_1.items():
        combined_dict[key] = value
    for key, value in currency_averages_2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value * (weight ** -1)

    for key, value in combined_dict.items():
        combined_dict[key] = round(value, 2)

    print("Done!")
    print("Printing to json...")
    file_path = "currencies.json"

    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            json_data = json.load(file)
    else:
        json_data = []

    json_data.append(combined_dict)

    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)

    print("Done, program complete!")
