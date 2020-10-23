print(*(letter for i, letter in enumerate(input())
        if letter == "и" and not i % 2-1 ),
      sep="\n")
