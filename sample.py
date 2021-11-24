arr = [{12: 0}, {11: 0}, {13: 0}, {5: 0}, {6: 0}]
arr[0].update({12:1})
print(arr[0].values())
print(arr[0])
print(list(arr[0].keys())[0]> list(arr[1].keys())[0])
