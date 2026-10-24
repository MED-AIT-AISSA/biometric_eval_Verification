import part1_calculations
import part2_distributions
import part3_curves


def run_part(choice):
    if choice == "1":
        print("Running Part 1: calculations and comparison table")
        part1_calculations.run()

    elif choice == "2":
        print("Running Part 2: score distributions")
        part2_distributions.run()

    elif choice == "3":
        print("Running Part 3: ROC, DET, EER and operating points")
        part3_curves.run()

    elif choice == "all":
        part1_calculations.run()
        part2_distributions.run()
        part3_curves.run()

    else:
        print("Unknown choice:", choice)


# Program starts here
while True:
    print()
    print("===== MENU =====")
    print("1) Part 1: calculations and comparison table (Questions 1-4)")
    print("2) Part 2: score distributions (Question 5)")
    print("3) Part 3: ROC, DET, EER, operating points (Questions 6-8)")
    print("all) Run everything")
    print("q) Quit")

    choice = input("Your choice: ")
    choice = choice.strip().lower()

    if choice == "q":
        break

    run_part(choice)
