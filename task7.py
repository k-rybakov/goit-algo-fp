import random
import matplotlib.pyplot as plt
import numpy as np

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    sums = [0] * 13  # Індекси від 0 до 12, щоб зручно зберігати суму від 2 до 12
    for _ in range(num_rolls):
        sum_roll = roll_dice() + roll_dice()
        sums[sum_roll] += 1
    return sums

def calculate_probabilities(sums, num_rolls):
    probabilities = [0] * 13
    for i in range(2, 13):
        probabilities[i] = (sums[i] / num_rolls) * 100
    return probabilities

def plot_probabilities(probabilities, analytical_probabilities):
    sums = list(range(2, 13))
    plt.bar(sums, probabilities[2:], label='Monte Carlo', alpha=0.7, color='blue')
    plt.plot(sums, analytical_probabilities[2:], label='Analytical', color='red', marker='o')
    
    plt.xlabel('Сума')
    plt.ylabel('Імовірність (%)')
    plt.title('Ймовірності сум при киданні двох кубиків')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    num_rolls = 1000000
    sums = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(sums, num_rolls)
    
    analytical_probabilities = [0, 0, 2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

    print("Сума\tІмовірність (Монте-Карло)\tІмовірність (Аналітична)")
    for i in range(2, 13):
        print(f"{i}\t{probabilities[i]:.2f}%\t\t\t{analytical_probabilities[i]:.2f}%")
    
    plot_probabilities(probabilities, analytical_probabilities)

if __name__ == "__main__":
    main()
