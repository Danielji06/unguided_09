def hapus_index_genap(list_input):
    while len(list_input) > 1:
        list_input = [list_input[i] for i in range(len(list_input)) if i % 2 != 0]
    return list_input[0]

input_n = int(input("Masukkan n: "))
list_input = []
for i in range(input_n):
    angka = int(input("Masukkan angka: "))
    list_input.append(angka)
print(hapus_index_genap(list_input))
