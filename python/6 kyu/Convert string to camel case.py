def to_camel_case(text):
    # your code here
    text = text.replace('-', '_')
    arr = text.split('_')

    first = arr.pop(0)
    for x in range(len(arr)):
        arr[x] = arr[x].title()

    return first + ''.join(arr)