def calculator_system(first, second, operation):

    incorrect_statment = True

    while incorrect_statment:
        if operation.upper().__eq__("MULTIPLY") or operation.upper().__eq__("MULTIPLICATION"):
            result = float(first) * float(second)
            print("Result is: " + str(result))
            incorrect_statment = False

        elif operation.upper().__eq__("DIVIDE") or operation.upper().__eq__("DIVISION"):
            result = float(first) / float(second)
            print("Result is: " + str(result))
            incorrect_statment = False

        elif operation.upper().__eq__("ADD") or operation.upper().__eq__("ADDITION"):
            result = float(first) + float(second)
            print("Result is: " + str(result))
            incorrect_statment = False

        elif operation.upper().__eq__("MINUS") or operation.upper().__eq__("SUBTRACTION"):
            result = float(first) - float(second)
            print("Result is: " + str(result))
            incorrect_statment = False

        else:
            print("Next time please enter a valid value")
            print("Examples include, addition, subtraction, multiplication, and division")
