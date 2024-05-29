# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return chosen_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Всі можливі страви
    item_names = list(items.keys())
    n = len(item_names)
    
    # Створюємо таблицю для динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Визначаємо обрані страви
    w = budget
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]['cost']
    
    total_calories = dp[n][budget]
    total_cost = budget - w
    
    return chosen_items, total_calories, total_cost


budget = 100

# Жадібний алгоритм
chosen_items_greedy, total_calories_greedy, total_cost_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", chosen_items_greedy)
print("Загальна калорійність:", total_calories_greedy)
print("Загальна вартість:", total_cost_greedy)

# Динамічне програмування
chosen_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Обрані страви:", chosen_items_dp)
print("Загальна калорійність:", total_calories_dp)
print("Загальна вартість:", total_cost_dp)
