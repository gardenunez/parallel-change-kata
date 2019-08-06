import csv


def load_data():
    with open('data.csv') as csvfile:
        reader = csv.DictReader(filter(lambda row: row[0]!='#', csvfile))
        for row in reader:
            yield row