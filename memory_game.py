from random import randint


colours = {
  1 : "red",
  2 : "green",
  3 : "blue",
  4 : "yellow"
}

number_of_colours = 5
sequence = []


# generates a random number between 1 - 4.
def generator_number():
    x = randint(1,4)
    return x

# assigns a string from the dictionary to the random number generated and appends to a list.
for i in range(number_of_colours):
    var = generator_number()
    colour = colours[var]
    sequence.append(colour)

# prints item in 1st index, asks user for input, and repeats.
for j in range(number_of_colours):
    print(sequence[j])
    answer = input("> ")
    answer_list = answer.split()
    print(answer_list)
    if answer_list[j] == sequence[j]:
        print("Correct\n")
    else:
        print("Failed\n")
        print(f"\nGame Over! Your got {j} correct answers in the sequence!")
        break