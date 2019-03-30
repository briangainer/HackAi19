import csv


cur_id = ''
cur_rating = 0
cur_count = 0
with open('ratings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    with open('clean_reviews.csv', newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in reader:
            temp_id, _, temp_rating = row
            temp_rating = float(temp_rating)

            if temp_id != cur_id:

                if cur_count > 0:
                    writer.writerow([cur_id, str(round(cur_rating / cur_count, 1))])

                cur_count = 1
                cur_id = temp_id
                cur_rating = temp_rating

            else:
                cur_count += 1
                cur_rating += temp_rating

