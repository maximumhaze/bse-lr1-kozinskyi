# Функція для розрахунку бюджету подорожі (FR-05). 
# Приймає: кількість днів, вартість готелю за день, витрати на їжу за день. 
# Повертає загальну суму.

def  calculate_travel_budget(days, hotel_cost_per_day, food_cost_per_day):
    total_hotel_cost = days * hotel_cost_per_day
    total_food_cost = days * food_cost_per_day
    total_budget = total_hotel_cost + total_food_cost
    return total_budget

# Тестування функції
budget = calculate_travel_budget(7, 100, 50)
print("Орієнтовний бюджет подорожі:", budget)