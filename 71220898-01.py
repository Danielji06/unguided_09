def tribonacci(a,b,c,n):
    hasil = [a,b,c]
    awal = 2
    panjang = n-3
    for i in range(panjang):
        next = hasil[start-2] + hasil[start-1] + hasil[start]
        hasil.append(next)
        start += 1
    return hasil

a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
c = int(input("Masukkan c: "))
n = int(input("Masukkan n: "))
hasil = tribonacci(a, b, c, n)
print(hasil)