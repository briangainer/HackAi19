import csv

foods = set([])
with open('foods.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    with open('clean_recipes.csv', newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=';', quotechar='|')

        for row in reader:
            list = row[7]
            for e in list.split(','):
                add = True
                for c in e:
                    if c in '0123456789()/|':
                        add = False
                if add:
                    foods.add(e.lower().strip().strip(':').strip(';').strip('\''))
    for f in foods:
        writer.writerow([f])
