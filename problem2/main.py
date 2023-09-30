def maximum_buy_product(money, product_price):
    nilai_max = max(product_price)
    count = [0] * (nilai_max + 1)
    for i in range(len(product_price)):
        count[product_price[i]] += 1
  
    idx_sorted = 0
    for i in range(nilai_max + 1):
        for j in range(count[i]):
            product_price[idx_sorted] = i
            idx_sorted += 1

    jml_brg = 0
    sum = 0
    for i in (product_price):
        if sum <= money:
            sum += i
            jml_brg += 1
    return jml_brg - 1

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0
