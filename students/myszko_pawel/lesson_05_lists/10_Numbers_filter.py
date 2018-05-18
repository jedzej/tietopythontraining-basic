# Using list comprehensions write a function that casts list of strings
# to list of integers and filters numbers within supplied range. Example data:
# list_of_strings = ['2', '0', '8', '3']
# to_filter_range = range(3)
# expected_output = [8, 3]

def range_and_convert(lista_str, filter_range):
    lista_int = [int(x) for x in lista_str if int(x) >= filter_range]
    return lista_int

def main():
    lista_str = []
    print("Enter the size of the list:")
    N = int(input())
    print("Enter list elements one by one:")
    for x in range(N):
        x = input("")
        lista_str.append(x)
        lista_str.sort()

    print(lista_str)
    print("Enter filter range for list:")
    filter_range = int(input())
    print(range_and_convert(lista_str, filter_range))

if __name__ == "__main__":
    main()
