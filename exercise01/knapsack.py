import random
import re

limit = 15


class Book:
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price


def generate_random_books(num_books):
    books = []
    for _ in range(num_books):
        weight = random.uniform(0.5, 3.0)
        price = random.uniform(10.0, 50.0)
        book = Book(weight, price)
        books.append(book)
    return books


random_books = generate_random_books(5)


def knapsack(books, limit):
    weight = 0
    score = 0
    for b in books:
        weight += b.weight
        score += b.price
    if weight > limit:
        return -1

    return score


results = []
fails = 0
cart = 100
while len(results) < 5:
    random_books = generate_random_books(cart)
    result = knapsack(random_books, limit)
    if result == -1:
        fails += 1
    else:
        results.append({"result": result, "books": len(random_books)})

    if fails > 100:
        cart = cart - 1

for r in results:
    print(f"Books: {r['books']}\tValue: {r['result']}")