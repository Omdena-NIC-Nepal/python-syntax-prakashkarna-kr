def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return(f"My name is {name} and I am {age} years old")

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number == 10:
        return(f"Equal")
    elif number > 10:
        return(f"Greater")
    else:
        return(f"Lesser")


def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    count = 0
    sum = 0
    while count <= n:
        sum += count
        count += 1
    return sum


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum = 0
    for i in numbers:
        sum += i

    numbers.sort()
    max = numbers[-1]
    min = numbers[0]

    return (sum, max, min)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    student_list = []

    for name in students_dict:
        if students_dict[name] > 80:
            student_list.append(name)

    return student_list



def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    set_1 = set(list1)
    set_2 = set(list2)

    common_elements = set_1 & set_2
    return common_elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    sum = a + b
    difference = a - b
    product = a * b
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = 0


    dict = {
        'sum' : sum,
        'difference' : difference,
        'product' : product,
        'quotient' : quotient
    }
    return dict

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    op_and = x and y
    op_or = x or y
    op_not = not(x)

    bool_dict = {
        'and' : op_and,
        'or' : op_or,
        'not_x' : op_not,
    }
    return bool_dict

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    bw_and = a & b
    bw_or = a | b
    bw_xor = a ^ b

    bw_dict = {
        'and' : bw_and,
        'or' : bw_or,
        'xor' : bw_xor,
    }
    return bw_dict