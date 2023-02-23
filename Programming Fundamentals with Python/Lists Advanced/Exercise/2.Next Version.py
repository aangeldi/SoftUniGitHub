sw_version = [int(x) for x in input().split(".")]

for i in range(len(sw_version) - 1, -1, -1):
    if sw_version[i] == 9:
        sw_version[i] = 0
        # sw_version[i - 1] = sw_version[i - 1] + 1
    else:
        sw_version[i] = sw_version[i] + 1
        break

sw_version = [str(x) for x in sw_version]
sw_version = ".".join(sw_version)
print(sw_version)
