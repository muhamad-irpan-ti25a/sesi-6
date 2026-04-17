whislist_gunung = ["rinjani", "merbabu", "prau", "gede", "pangrango", "lawu", "ciremai", "sindoro", "jaya wijaya", "krinci", "raung", "slamet", "merapi", "papandayan", "patuha", "sunan ibu", "sumbing"]


i = 0

while i < len(whislist_gunung):
    if  (whislist_gunung[i] == "krinci"):
        print("krinci sudah ketemu")
        break
    print(whislist_gunung[i])
    i+=1


for i in range(20):
    if (i==0 or i%3 !=0):
        continue
    print(i, end=" ")



    
