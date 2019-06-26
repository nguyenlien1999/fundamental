prices={"banana": 4, "apple": 2, "orange": 1.5,"pear": 3}
stock ={"banana": 6, "apple": 0, "orange": 32, "pear": 15}
for key in stock:
    print(key)
    print("prices :", prices[key])
    print("stock :", stock[key])

total=0
for key in stock:
    money=prices[key]*stock[key]
    total+=money
print("money",money)
print("total",total)
