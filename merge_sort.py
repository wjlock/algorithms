def merge(arr1, arr2):
    output = []
    start_length_arr1 = len(arr1)
    start_length_arr2 = len(arr2)
    target_output_length = start_length_arr1 + start_length_arr2

    while len(output) < target_output_length:
        print(output)

        if len(arr1) == 0:
            output += arr2
            arr2 = []

        if len(arr2) == 0:
            output += arr1
            arr1 = []

        elif arr1[0] < arr2[0]:
            output.append(arr1[0])
            arr1 = arr1[1:]
        else:
            output.append(arr2[0])
            arr2 = arr2[1:]

    return output


print(merge([2], [4]))  # ==> [2,4]
