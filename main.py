from naming_machine import Number


def input_number():
    user_input = int(input("Input the number in digits to be changed to words: "))
    # print(type(user_input))
    if type(user_input) is int:
        num = Number(user_input)
        print(num.final_name)
    else:
        print("invalid Input")
        continue_yes_no = input("do you which to retry(yes/no) :").lower()
        if continue_yes_no == "yes":
            input_number()


input_number()
