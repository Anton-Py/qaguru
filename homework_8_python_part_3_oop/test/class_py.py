class User:
    name: str
    age: int
    status: str
    item: list[str]

    def __init__(self, name, age, status, items):
        self.name = name
        self.age = age
        self.status = status
        self.item = items

if __name__ == '__main__':
    d = {"name": "Oleg",
         "age": 16,
         "status": "student",
         "items": ["book", "pen", "paper"]}

    oleg = User(name="Oleg", age=16, status="student", items=["book", "pen", "paper"])
    olga = User(name="Olga", age=18, status="student", items=["book", "pen", "paper"])

    # olga.status

    assert oleg.age == 18
    assert olga.age == 18