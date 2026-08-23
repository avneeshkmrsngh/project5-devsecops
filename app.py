import ast


APP_INSTRUCTIONS = "You are a helpful AI assistant."


def calculate(user_input):
    return ast.literal_eval(user_input)


def main():
    user_input = input("Enter expression: ")

    try:
        result = calculate(user_input)
        print("Result:", result)
    except (ValueError, SyntaxError):
        print("Invalid expression")


if __name__ == "__main__":
    main()