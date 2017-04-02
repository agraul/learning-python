i = 0
numbers = []

def ongoing(i, end):
    while i < end:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now", numbers)
        print(f"At the bottom i is {i}")


        print("The numbers: ")

        for num in numbers:
            print(num)

ongoing(i, int(input("Set limit for loop: ")))
