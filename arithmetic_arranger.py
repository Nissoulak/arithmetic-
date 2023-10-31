def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = []
    answers = []  # Added for storing answers

    for problem in problems:
        num1, operator, num2 = problem.split()
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'"
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits"
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"

        width = max(len(num1), len(num2)) + 2
        arranged_problems.append(f"{num1.rjust(width)}")
        arranged_problems.append(f"{operator} {num2.rjust(width - 2)}")
        arranged_problems.append('-' * width)

        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))  # Store the answers

    arranged = "\n".join(arranged_problems)

    if show_answers:
        answers_line = "    ".join(answers)
        arranged += "\n" + answers_line

    return arranged
