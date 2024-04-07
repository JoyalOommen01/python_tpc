li=[-1,-23,-453,-533,55,-677]
for i in li:
    for j in li:
        if i < j:
            break
    if j<i:
        break
print("maximum value=",i)
