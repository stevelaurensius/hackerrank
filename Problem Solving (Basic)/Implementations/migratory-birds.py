def migratoryBirds(arr):
    type_list = sorted(arr)
    type_set = set(type_list)
    result = {x: type_list.count(x) for x in type_set}
    highest = max(result, key=result.get)
    for i in result:
        if i == highest:
            return i
