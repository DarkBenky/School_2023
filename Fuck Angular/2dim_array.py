def create_2_dim_array(rows, cols , value):
    arr = [[0 for x in range(cols)] for y in range(rows)]
    temp = 1
    for i in range(rows):
        if temp == value+1:
            temp = 1
        arr[i][0] = temp
        temp += 1
    
    for i in range(rows):
        temp = arr[i][0]
        for j in range(1, cols):
            if temp == value:
                arr[i][j] = 1
                temp = 1
            else:
                arr[i][j] = temp + 1
                temp += 1
    return arr

print(create_2_dim_array(5, 6, 7))

        