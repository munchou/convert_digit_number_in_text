numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

units = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
]

# and_print = "" # (used for testing)

print(
    """You can enter number with , and ., such as "5,658,456.65". Please note that commas' positions are checked, so a typo will lead to an error."""
)
print('Depending on the option about "and", the output will be:')
print(
    "Five million six hundred fifty-eight thousand four hundred fifty-six and sixty-five"
)
print("or")
print(
    "Five million six hundred and fifty-eight thousand four hundred and fifty-six and sixty-five"
)
print()


while True:
    user_and_input = input('Use "and" (like in "two hundred AND one")? (y/n): ')
    if user_and_input.casefold() == "y":
        and_print = " and"
        break
    elif user_and_input.casefold() == "n":
        and_print = ""
        break
    else:
        continue


def check_number_if_commas(number):
    number = number.split(",")
    for y in range(len(number)):
        if y == 0 and len(number[y]) > 3 or y > 0 and len(number[y]) != 3:
            return False


decimals = None

while True:
    user_input = input(
        f"\nPlease enter a positive number <= {'9'*(len(units)*3)} (999 {units[-1]}): "
    )

    if "." in user_input:
        if user_input.count(".") != 1:
            print('Error: There cannot be more than one "."')
            continue
        user_input_split = user_input.split(".")
        user_input = user_input_split[0]
        decimals = user_input_split[1]

        # print(user_input_split, user_input, decimals)

    if "," in user_input:
        if check_number_if_commas(user_input) is False:
            print(
                "There seems to be a problem with your input, please check if there isn't any typo."
            )
            continue
        user_input = user_input.replace(",", "")
    try:
        user_input = int(user_input)
        if user_input < 0:
            print("Please enter a number >= 0")
            continue
        if user_input > int("9" * (len(units) * 3)):
            print(f"Please enter a number <= {'9'*(len(units)*3)} (999 {units[-1]}).")
            continue
    except ValueError:
        print("That's not a valid number")
        continue
    user_input = str(user_input)

    while True:
        if user_input.startswith("0") and len(user_input) > 1:
            user_input = user_input[1:]
            continue
        break

    break


def chunk_of_digits(chunk):
    if len(chunk) >= 1:
        if chunk[-1]:
            unit = numbers[int(chunk[-1])]
        hundredth = tenth = ""

        if len(chunk) >= 2:
            if chunk[-1] == "0":
                unit = ""
            if chunk[-2] != "0" and unit == "":
                tenth = numbers[int(chunk[-2]) * 10]
            elif chunk[-2] != "0" and unit != "":
                if int(chunk[-2:]) < 20:
                    tenth = numbers[int(chunk[-2:])]
                    unit = ""
                else:
                    tenth = f"{numbers[int(chunk[-2]) * 10]}-"
            else:
                tenth = ""
            hundredth = ""

            if len(chunk) >= 3:
                if chunk[-3] != "0":
                    if chunk.endswith("00"):
                        hundredth = f"{numbers[int(chunk[-3])]} hundred"
                    else:
                        hundredth = f"{numbers[int(chunk[-3])]} hundred{and_print} "

    return f"{hundredth}{tenth}{unit}"


def digits_to_text(user_input):
    number_of_chunks = (len(user_input) - 1) // 3 + 1

    result_list = []
    result = ""
    pos_in_num = 0

    if user_input == decimals:
        while True:
            if user_input[0] == "0":
                result += "zero "
                user_input = user_input[1:]
                continue
            else:
                number_of_chunks = (len(user_input) - 1) // 3 + 1
                break

    for g in range(number_of_chunks):
        if g == 0:
            result_list.append(
                f"{chunk_of_digits(user_input[-len(user_input):])} {units[g]}"
            )
        else:
            if not user_input[-len(user_input) : pos_in_num].endswith("000"):
                result_list.append(
                    f"{chunk_of_digits(user_input[-len(user_input):pos_in_num])} {units[g]} "
                )

        pos_in_num -= 3

    for item in result_list[::-1]:
        result += item

    if user_input != decimals and user_input.endswith("000"):
        return result[:-2]

    return result[:-1]


(
    print(f"\nConversion of {user_input}:")
    if not decimals
    else print(f"\nConversion of {user_input}.{decimals}:")
)

if decimals:
    print(digits_to_text(user_input).capitalize(), "and", digits_to_text(decimals))
else:
    print(digits_to_text(user_input).capitalize())
