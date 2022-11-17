sayi1 = 53
sayi2 = 34
sayi3 = 28

if sayi1>sayi2 and sayi1>sayi3 and sayi2>sayi3:
    print(sayi1)
    print(sayi3)
elif sayi1>sayi2 and sayi1>sayi3 and sayi3>sayi2:
    print(sayi1)
    print(sayi2)
elif sayi2>sayi1 and sayi2>sayi3 and sayi1>sayi3:
    print(sayi2)
    print(sayi3)
elif sayi2>sayi1 and sayi2>sayi3 and sayi3>sayi1:
    print(sayi2)
    print(sayi1)
elif sayi3>sayi1 and sayi3>sayi2 and sayi1>sayi2:
    print(sayi3)
    print(sayi2)
elif sayi3>sayi1 and sayi3>sayi2 and sayi2>sayi1:
    print(sayi3)
    print(sayi1)
else:
    print()
