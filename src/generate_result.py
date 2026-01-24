import json
import csv


with open("users.json", "r") as f:
    users = json.load(f)

result_list_users = []

for user in users:
    result_list_users.append(
        {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [],
        }
    )

books = []
with open("books.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        books.append(
            {
                "title": row["Title"],
                "author": row["Author"],
                "pages": row["Pages"],
                "genre": row["Genre"],
            }
        )

extra_books = len(books) % len(users)
i = 0

for user in result_list_users:
    for _ in range(7):
        user["books"].append(books[i])
        i += 1

    if extra_books > 0:
        user["books"].append(books[i])
        extra_books -= 1
        i += 1

with open("result.json", "w") as f:
    json.dump(result_list_users, f)
