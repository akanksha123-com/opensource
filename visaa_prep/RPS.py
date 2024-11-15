def determine_winner(vignesh, charan):
    if vignesh == charan:
        return "NULL"
    elif (vignesh == "R" and charan == "S") or (vignesh == "S" and charan == "P") or (vignesh == "P" and charan == "R"):
        return "Vignesh"
    else:
        return "Charan"
vignesh, charan = input().split()
print(determine_winner(vignesh, charan))
