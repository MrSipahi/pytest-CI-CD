
from main import Employee


def test_give_raise():
    emp1 = Employee("Alice", 5000)
    emp2 = Employee("Bob", 6000)

    # Test 1: Give raise of $1000 to emp1
    emp1.give_raise(2000)
    assert emp1.salary == 7000

    # Test 2: Give raise of $2000 to emp2
    emp2.give_raise(3000)
    assert emp2.salary == 9000

    # Test 3: Give negative raise to emp1
    emp1.give_raise(-500)
    assert emp1.salary == 6500