#Tom's tax Calculator
Cost = int(input("How much money do you earn? "))
if Cost < 12570:
    print(Cost)
elif Cost  < 50270 and Cost > 12571:
    print(Cost-(Cost//20))
elif Cost  < 125140 and Cost > 50271:
    print(Cost-(Cost//40))
elif Cost > 125140:
    print(Cost-(Cost//45))