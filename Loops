#Carly's Clippers

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price

#checkpoint 3
average_price = total_price / len(prices)
print(average_price)

#checkpoint 4
new_prices = [price - 5 for price in prices]
print(new_prices)

#checkpoint 5
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)

#checkpoint 6
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#checkpoint 7 
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]< 30]
print(cuts_under_30)
