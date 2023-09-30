def playing_domino(cards, deck):
    output = []
    sum_kartu = 0
    for i, sublist in enumerate(cards):
      for j, elemen in enumerate(sublist):
        if elemen in deck:
          if sum(cards[i]) > sum_kartu:
            sum_kartu = sum(cards[i])
            output.append(cards[i])
    return [elemen for sublist in output for elemen in sublist]

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []
