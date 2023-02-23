electrons = int(input())
shells = []
used_electrons = 0
index = 0
while electrons >= used_electrons:
    index += 1
    used_electrons = 2 * (index ** 2)
    if used_electrons <= electrons:
        electrons -= used_electrons
        shells.append(used_electrons)
if electrons > 0:
    shells.append(electrons)
print(shells)
