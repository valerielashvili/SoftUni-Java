budget = int(input())
season = input()
num_fisherman = int(input())

price = 0
discount = 0

if season == 'Spring':
    price = 3000

    if num_fisherman <= 6:
        discount = price * 0.10
        price -= discount

elif season == 'Summer' or season == 'Autumn':
    price = 4200
    
    if 7 <= num_fisherman <= 11:
        discount = price * 0.15
        price -= discount

elif season == 'Winter':
    price = 2600
    
    if num_fisherman >= 12:
        discount = price * 0.25
        price -= discount

if num_fisherman % 2 == 0 and season != 'Autumn':
    discount = price * 0.05
    price -= discount

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
