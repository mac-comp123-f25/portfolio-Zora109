"""
Contains a simulation of the Petrie Multiplier that is based on classes.
"""

import random
import math


class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender: str, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee to zero.
        """
        self.gender = gender                # "Man" or "Woman"
        self.will_comment = bool(will_comment)  # True/False
        self.comments_received = 0          # start at 0

    def __str__(self):
        """
        Produces a printable string format for this employee.
        """
        return (self.gender.rjust(5)
                + ": "
                + str(self.comments_received)
                + " sexist comments received")


def print_employee_list(lst):
    """
    Given a list of employees, this method will print the details of each employee
    by using the print() method
    """
    for emp in lst:
        print(emp)


def create_employees(total_num):
    """
    Takes in the number of employees to make, builds and returns a list that contains
    that many employees. It ensures that ~80% are men and the rest women.
    """
    if total_num <= 0:
        return []

    num_men = round(total_num * 0.8)
    num_women = total_num - num_men

    employees = []
    # default will_comment=False; create_commenters() will set 20% later
    for _ in range(num_men):
        employees.append(Employee("Man", False))
    for _ in range(num_women):
        employees.append(Employee("Woman", False))

    random.shuffle(employees)  # randomize order a bit
    return employees


def create_commenters(lst):
    """
    Given a list of employees, make 20% of each gender be sexist employees. This
    method should not return anything.
    """
    # Split by gender
    men = [e for e in lst if e.gender == "Man"]
    women = [e for e in lst if e.gender == "Woman"]

    # First, set everyone to not comment, then flip 20% to True
    for e in lst:
        e.will_comment = False

    def activate_twenty_percent(group):
        if not group:
            return
        k = max(1, math.floor(len(group) * 0.20)) if len(group) > 0 else 0
        # If group is very small (e.g., 1–4), floor could be 0; ensure at least 1 if group exists
        chosen = random.sample(group, k=min(k, len(group)))
        for e in chosen:
            e.will_comment = True

    activate_twenty_percent(men)
    activate_twenty_percent(women)


def generate_comments(lst):
    """
    Given a list of employees, have each sexist employee give one sexist comment to
    another employee of the opposite gender, chosen randomly. This method should
    not return anything
    """
    # Precompute targets by gender
    men = [e for e in lst if e.gender == "Man"]
    women = [e for e in lst if e.gender == "Woman"]

    for e in lst:
        if not e.will_comment:
            continue
        if e.gender == "Man":
            targets = women
        else:
            targets = men

        if not targets:
            continue  # no opposite-gender targets available

        target = random.choice(targets)
        target.comments_received += 1


def average_comments(lst):
    """
    Returns a tuple that represents the average amount of comments received for men and women
    respectively. Return statement will be in the form (<avg_for_men>, <avg_for_women>)
    """
    men_comments = 0
    men_count = 0
    women_comments = 0
    women_count = 0

    for e in lst:
        if e.gender == "Man":
            men_comments += e.comments_received
            men_count += 1
        elif e.gender == "Woman":
            women_comments += e.comments_received
            women_count += 1

    men_avg = men_comments / men_count if men_count else 0.0
    women_avg = women_comments / women_count if women_count else 0.0

  
    return (round(men_avg, 2), round(women_avg, 2))


def main():
    """
    Print out information about the average comments
    received by men and women after a simulation has been run
    """
    num_employees_to_generate = 100
    num_comment_rounds = 50

    employee_list = create_employees(num_employees_to_generate)
    create_commenters(employee_list)
    for rounds in range(num_comment_rounds):
        generate_comments(employee_list)

    (men_avg, women_avg) = average_comments(employee_list)
    print("  Men received on average ",   men_avg, "sexist comments")
    print("Women received on average ", women_avg, "sexist comments")


if __name__ == "__main__":
    "<----- Test code for print_employee_list ----->"
    lst = [Employee('Man', True),
           Employee('Man', False),
           Employee('Woman', True),
           Employee('Woman', False)]
    print_employee_list(lst)

    "<----- Test code for create_employees ----->"
    employees = create_employees(10)
    print_employee_list(employees)

    "<----- Test code for create_commenters ----->"
    create_commenters(employees)
    print_employee_list(employees)

    "<----- Test code for generate_comments ----->"
    generate_comments(employees)
    print_employee_list(employees)

    "<----- Test code for average_comments ----->"
    print(average_comments(employees))

    "<----- Run the simulation ----->"
    # main()  # <-- KEEP THIS, Uncomment it after implementing all the functions
