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

# and_print = ""

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

while True:
    user_input = input(
        "Please enter a positive number <= 999 999 999 999 999 (999 trillion): "
    )
    try:
        user_input = int(user_input)
        if user_input < 0:
            print("Please enter a number >= 0")
            continue
        if user_input > 999999999999999:
            print("Please enter a number <= 999 999 999 999 999 (999 trillion).")
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

trillionth = billionth = millionth = thousandth = hundredth = tenth = unit = ""


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


number_parts = (len(user_input) - 1) // 3 + 1
# print(f"Number of chunks: {number_parts}")

chunk5 = chunk4 = chunk3 = chunk2 = chunk1 = ""

if number_parts >= 1:
    chunk1 = chunk_of_digits(user_input[-len(user_input) :])
if number_parts >= 2:
    chunk2 = f"{chunk_of_digits(user_input[-len(user_input) :-3])} thousand "
if number_parts >= 3:
    chunk3 = f"{chunk_of_digits(user_input[-len(user_input) : -6])} million "
if number_parts >= 4:
    chunk4 = f"{chunk_of_digits(user_input[-len(user_input) : -9])} billion "
if number_parts >= 5:
    chunk5 = f"{chunk_of_digits(user_input[-len(user_input) : -12])} trillion "

print(f"{chunk5}{chunk4}{chunk3}{chunk2}{chunk1}".capitalize())
