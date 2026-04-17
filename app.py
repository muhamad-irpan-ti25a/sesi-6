a = 1

for i in range(20):
    print(f"{a}.saya suka naik gunung")
    a += 1

for index, value in enumerate(range(20), start = 1) :
    print(f"{index}. saya ingin naik gunung rinjani")

gunung = {"merbabu", "rinjani", "gede", "pangrango", "lawu", 'sindoro'}

for i, nama in enumerate(gunung):
    print(f"{i+1}. {nama}")