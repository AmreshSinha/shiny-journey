# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    arr = []
    arr1 = []
    arr2 = []
    n = int(input())

    # For Making Arrays of [name,score] , [name], [score]
    for _ in range(n):
        name = str(input())
        score = float(input())
        arr.append([name,score])
        arr1.append(name)
        arr2.append(score)

    # Removing Duplicate Values From Score List arr2

    i = 0.0
    arr2_dups_removed = []
    for i in arr2:
        if i not in arr2_dups_removed:
            arr2_dups_removed.append(i)
    
    # print(arr2_dups_removed)

    # Now Minimum Value

    sorted_arr2 = (sorted(arr2_dups_removed))
    # print(sorted_arr2)

    # Second Minimum Value in Score
    sec_min = sorted_arr2[1]
    # print(sec_min)



    # Making a List of i
    req_i = []
    for i in range(n):
        if arr2[i] == sec_min:
            req_i.append(i)
    # print(req_i)

    # Finalising Names with Alphabetical Sorting
    names_list = []
    for k in req_i:
        if arr1[k] not in names_list:
            names_list.append(arr1[k])
    # print(names_list)

    # Sorting Names
    names_list = sorted(names_list)
    for names in names_list:
        print(names)