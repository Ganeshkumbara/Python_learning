weight = int(input('weight: '))
pound_or_KG = input('(L)bs or (K)g:')

if pound_or_KG.lower() == "l":
    KG = weight * 0.45
    print(f'you are {round(KG,2)} KG')
else:
    pound = weight / 0.45
    print(f'you are {round(pound,2)} lbs')

