import csv

import pytest


# def test_workers_are_adults():
#
#     with open("users_two.csv") as file:
#         users = csv.DictReader(file, delimiter=";")
#         workers = [user for user in users if user[""]]

@pytest.fixture
def users():
    with open("users.csv", newline='', encoding='utf-8') as file:
        users = list(csv.DictReader(file, delimiter=";"))

        for user in users:
            print("users", user)

    return users


@pytest.fixture
def workers(users):
    workers = [user for user in users if user["status"] == "worker"]

    return workers


def test_workers_are_adults_v2(workers):
    for worker in workers:
        assert int(worker["age"]) >= 18, f"{worker['age']} младше 18 лет"
