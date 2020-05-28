for i in range(5):
    for j in range(5):
        if j == 3:
            break    # terminate the for j loop
        print(i,j)

print()

for i in range(5):
    for j in range(5):
        print(i,j)
    if j == 3:       # does not matter since in the end j always == 4 
        break    

print()      

for i in range(5):
    for j in range(5):
        if j == 3:
            continue  # continue the for j loop
        print(i,j)
