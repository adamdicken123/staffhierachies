__author__ = 'Adam.Dicken'


def get_common_manager(filename):
    """
    Takes a filename for a file containing
    - count of employees
    - employee A
    - employee B
    - A line for each relation ship of the form 'manager employee'

    Returns the lowest common manager shared by both employee A and employee B
    """
    # Get a dict of {emp: manager, }
    emp_manager_dict = {}

    # Read the file in
    with open(filename) as f:
        lines = f.read().splitlines()

        # get the fixed lines
        count = lines[0]
        emp_a = lines[1]
        emp_b = lines[2]

        # Get the hierachy of manager employee
        for line in lines[3:]:
            manager, emp = line.split(' ')
            emp_manager_dict[emp] = manager

    # Use function below to get the chain of command for each employee in question
    h1 = get_hierachy_for_emp(emp_a, emp_manager_dict)
    h2 = get_hierachy_for_emp(emp_b, emp_manager_dict)

    # Compare the arrays from top manager to employee
    # Keep a track of last match and stop when hierachies diverge
    match = None
    for i in range(0, min(len(h1), len(h2))):
        # If current employee in both chains is the same and not equal to either employee then record a match
        if h1[i] == h2[i] and h1[i] != emp_a and h2[i] != emp_b:
            match = h1[i]
        # else no match, break
        else:
            break

    return match


def get_hierachy_for_emp(emp, emp_manager_dict):
    """
    Returns the chain of command for any named employee as an array
    In order of high to low such that emp is the last in the array
    """
    # Initialise with leaf
    hierachy = [emp]
    has_manager = True
    _emp = emp
    # While a manager can be found keep climbing up the tree
    while has_manager:
        # If manager found set _emp = manager and continue
        if emp_manager_dict.has_key(_emp):
            _emp = emp_manager_dict[_emp]
            hierachy.insert(0, _emp)
        # If no manager found we have reacher the top of the rree so we stop
        else:
            has_manager = False
    return hierachy
