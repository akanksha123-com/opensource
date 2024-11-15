X, Y, Z = map(int,(input().split()))
available_weight_for_mangoes = Z-Y
max_mangoes= available_weight_for_mangoes // X
print(max_mangoes)
