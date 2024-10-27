import random

iller = ["adana","adiyaman","afyon","agri","amasya","ankara","antalya","artvin","aydin","balikesir","bilecik",\
"bingol","bitlis","bolu","burdur","bursa","canakkkale","cankiri","corum","denizli","diyarbakir","edirne","elazig",\
"erzincan","erzurum","eskisehir","gaziantep","giresun","gumushane","hakkari","hatay","isparta","mersin(icel)","istanbul",\
"izmir","kars","kastamonu","kayseri","kirklareli","kirsehir","kocaeli","konya","kutahya","malatya","manisa","kahramanmaras",\
"mardin","mugla","mus","nevsehir","nigde","ordu","rize","sakarya","samsun","siirt","sinop","sivas","tekirdag","tokat","trabzon",\
"tunceli","sanliurfa","usak","van","yozgat","zonguldak","aksaray","bayburt","karaman","kirikkale","batman","sirnak","bartin",\
"ardahan","igdir","yalova","karabuk","kilis","osmaniye","duzce"]

plaka_sozlugu = {"adana":1,"adiyaman":2,"afyon":3,"agri":4,"amasya":5,"ankara":6,"antalya":7,"artvin":8,"aydin":9,"balikesir":10,"bilecik":11,\
"bingol":12,"bitlis":13,"bolu":14,"burdur":15,"bursa":16,"canakkkale":17,"cankiri":18,"corum":19,"denizli":20,"diyarbakir":21,"edirne":22,"elazig":23,\
"erzincan":24,"erzurum":25,"eskisehir":26,"gaziantep":27,"giresun":28,"gumushane":29,"hakkari":30,"hatay":31,"isparta":32,"mersin(icel)":33,"istanbul":34,\
"izmir":35,"kars":36,"kastamonu":37,"kayseri":38,"kirklareli":39,"kirsehir":40,"kocaeli":41,"konya":42,"kutahya":43,"malatya":44,"manisa":45,"kahramanmaras":46,\
"mardin":47,"mugla":48,"mus":49,"nevsehir":50,"nigde":51,"ordu":52,"rize":53,"sakarya":54,"samsun":55,"siirt":56,"sinop":57,"sivas":58,"tekirdag":59,"tokat":60,"trabzon":61,\
"tunceli":62,"sanliurfa":63,"usak":64,"van":65,"yozgat":66,"zonguldak":67,"aksaray":68,"bayburt":69,"karaman":70,"kirikkale":71,"batman":72,"sirnak":73,"bartin":74,\
"ardahan":75,"igdir":76,"yalova":77,"karabuk":78,"kilis":79,"osmaniye":80,"duzce":81}


a = random.choice(iller)

oyun_skoru = 0
yanlis_sayisi = 0

c = int(input("kac defa oynayacaksiniz:"))


print(f"{a} :")
b = int(input("tahmininiz :"))


if plaka_sozlugu[a] == b :
    print("TEBRİKLER ! Dogru")
    oyun_skoru += 1
else:
    print("Tahmininiz yanlis !")
    yanlis_sayisi += 1

for i in range( c - 1 ):
    a = random.choice(iller)
    print(f"{a} :")
    b = int(input("tahmininiz :"))

    if plaka_sozlugu[a] == b :
        print("TEBRİKLER ! Dogru")
        oyun_skoru += 1
        

    if plaka_sozlugu[a] != b:
        print("Tahmininiz yanlis !")
        yanlis_sayisi += 1
        
print(f"Dogru Sayisi:{oyun_skoru} || Yanlis Sayisi:{yanlis_sayisi}")
