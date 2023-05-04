def hitung_vote(vote):
    n = len(vote)
    for candidate in vote:
        if vote.count(candidate) > n/2:
            return candidate
    return None

input_vote = []
n = int(input("Jumlah vote: "))
for i in range(n):
    vt = input("Masukkan vote: ")
    input_vote.append(vt)

hasil = hitung_vote(input_vote)
print(hasil)