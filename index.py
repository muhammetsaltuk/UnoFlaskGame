from flask import Flask, render_template, request, redirect, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import uno
import random

app = Flask(__name__, template_folder="./templates", static_folder="./public")
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

CORS(app)


@app.route('/')  # Oyun sayfası
def index():
    return render_template('index.html')


@app.route('/login')  # Login sayfası
def login():
    return render_template('login.html')


rooms = dict()  # Odaları ve odadaki oyun bilgilerini tutar


@socketio.on('connect')  # Bir kullanıcı bağlandığında çalışır
def connect():
    print("Bir Kullanıcı Bağlandı")
    # Odadaki verileri cliente günceller
    socketio.emit('rooms', {"rooms": rooms})




@socketio.on('disconnect') # Bir kullanıcı ayrıldığında çalışır
def disconnect():
    print("Bir Kullanıcı Ayrıldı")
    # Odadaki verileri cliente günceller
    socketio.emit('rooms', {"rooms": rooms})



@socketio.on('exit_room') # Kullamıcı çıkış yapmak istediğinde çalışır (Çıkış yap butonu)
def exit_room(data):
    users = rooms[str(data["code"])]["users"]
    del users[data["username"]]  # çıkış yapan kullanıcııyı odadan siler
    rooms[str(data["code"])]["users"] = users
    if len(rooms[str(data["code"])]["users"]) == 0:
        del rooms[str(data["code"])]  # son kullanıcı çıktığında odayı siler


@socketio.on('get_deck_cart') # Kullanıcı Kart çekme işlemi
def get_deck_cart(data):
    if rooms[str(data["code"])]["users"][data["username"]]["gamer"] == 1:
        deck = rooms[str(data["code"])]["game"]["deck"]
        if len(deck) > 0:
            rooms[str(data["code"])]["users"][data["username"]
                                              ]["carts"].append(deck[:1][0])
            rooms[str(data["code"])]["game"]["deck"] = deck[1:]
        else: 
            rooms[str(data["code"])]["game"]["deck"] = uno.buildDeck() # detede kart bittiyse yeni deste ekler
        # Odadaki verileri cliente günceller
        socketio.emit('rooms', {"rooms": rooms})


@socketio.on('get_rooms') # Odaları cliente yollar
def get_rooms(data):
    # Odadaki verileri cliente günceller
    socketio.emit('rooms', {"rooms": rooms})





@socketio.on('join_room') # Oda oluşturma ve katılma 
def join_room(data):
    if data["code"] not in rooms: 
        # Boyle bir oda yoksa oda oluşturur
        rooms[str(data["code"])] = {
            "hash": str(data["hash"]), # KULLANICININ BENZERSİZZ KİMLİĞİ
            "code": str(data["code"]), # oda kodu
            "users": dict({}), # Odadai kullanıcılar
            "game": dict({
                "deck": uno.buildDeck(), # Oyudaki deste
                "middle": [], # Ortaya atılan kartlar
                "color": "", # Son atılan kartın rengi
                "reverse": False, # Oyun turunun dönme yönü
                "status": 0 # Oyunun Bşlama durumu (1 Başlar- 0 Oyuncu bekler)
            })
        }

    # Odaya yeni kullanıcı girdiğinde odaya o kullanıcıyı ekler 
    # Oyun başlamamış ve 4 kişiden azsa Çalışır
    if str(data["username"]) not in rooms[str(data["code"])]["users"] and len(rooms[str(data["code"])]["users"]) < 4 and rooms[str(data["code"])]["game"]["status"] == 0:
        rooms[str(data["code"])]["users"][data["username"]] = {
            "username": data["username"],
            "carts": [],
            "gamer": 0
        }

    # Oyun Başlama | Oyun 4 kşiş olduğunda başlar
    if len(rooms[str(data["code"])]["users"]) == 4 and rooms[str(data["code"])]["game"]["status"] == 0:
        rooms[str(data["code"])]["game"]["status"] = 1 # Oyun durumunu değiştidi

        deck = rooms[str(data["code"])]["game"]["deck"] # Odadki deste
        users = rooms[str(data["code"])]["users"] # Odadki kullanıcılar

        i = False
        for x, y in users.items(): # Kullanıcılara kart dağıtır
            if i == False:
                i = True
                users[x]["gamer"] = 1
            users[x]["carts"] = deck[:7] # kullanıcıya 7 adet kart ver
            deck = deck[7:] # verilen kartı desteden SİLER
            rooms[str(data["code"])]["game"]["deck"] = deck # odadaki desteleri eşitler

        # Oyun başladığındaki ilk kart 
        starter_cart = list(
            filter(lambda x: not x == "wild" or not x == "wilddrawfour", deck))[0]
        
        rooms[str(data["code"])]["game"]["middle"].append(starter_cart) # Başlangıç kartı ortaya atılır
        rooms[str(data["code"])]["game"]["color"] = starter_cart.split("-")[0] # Başlangıç kartı rengi
        rooms[str(data["code"])]["game"]["deck"] = deck[1:] # Başlangıç kartı desteden silinir

        socketio.emit('game_start', {"rooms": rooms}) # Oyun başladığını cliente bildirir

    socketio.emit('rooms', {"rooms": rooms}) # Odadaki verileri cliente günceller


# Kullanıcının ortaya kart atması
@socketio.on('send_cart')
def send_cart(data):
    # Oyun yönünü çevirir
    reverse = rooms[str(data["code"])]["game"]["reverse"] # Oyun yönü
    if "reverse" in data["cartId"]:
        reverse = not reverse
        rooms[str(data["code"])]["game"]["reverse"] = reverse

    user_list = list(rooms[str(data["code"])]["users"].keys()) # kullanıcı listesi(sıralı)

    if reverse: # oyun terse döncek ise
        user_list = user_list[::-1] # kullanıcı listesi ters çevrilir

    color = data["cartId"].split("-")[0] # Atılan kartın rengi alınır

    if data["selectColor"]: # Jokerlerden sonra seçilen renk 
        color = data["selectColor"]


    if data["cartId"] in rooms[str(data["code"])]["users"][data["username"]]["carts"]: # atılan kart kullanıcının kartlarında varmı
        rooms[str(data["code"])]["game"]["middle"].append(data["cartId"]) # kartı ortaya at
        rooms[str(data["code"])]["game"]["color"] = color # ortadaki kart rengi(oyun rengi)

        index = rooms[str(data["code"])]["users"][data["username"]
                                                  ]["carts"].index(data["cartId"]) # kartın kartların içindeki konumu(index)
        rooms[str(data["code"])]["users"][data["username"]]["carts"].pop(index) # kartın kullanıcı destesinden silinmesi

        if len(rooms[str(data["code"])]["users"][data["username"]]["carts"]) == 1: # Elide 1 kart varsa UNO
            socketio.emit('alert', {"message": "UNO! ("+data["username"]+")"})
        if len(rooms[str(data["code"])]["users"][data["username"]]["carts"]) == 0: # Elide 0 kart varsa Bitti
            socketio.emit(
                'alert', {"message": "Oyun Bitti! Kazanan: "+data["username"], "ended": True})

    rooms[str(data["code"])]["users"][data["username"]]["gamer"] = 0 # Oyuncuların oyun sırasını durumu (1 ise sıra onda)
    for i in range(len(user_list)): # TÜM Oyuncuların oyun sırasını 0 yapar
        rooms[str(data["code"])]["users"][user_list[i]]["gamer"] = 0

    next_user = data["username"]
    for i in range(len(user_list)): # Bir sonraki kullanıcıyı bulur
        if str(user_list[i]) == data["username"]:
            if "skip" in data["cartId"]: # Ban kartı için
                _user_ = user_list[(i+2) % 4]
                rooms[str(data["code"])]["users"][_user_]["gamer"] = 1 # Sonraki kullanıcının oyun durumu 2 yapılur
                next_user = _user_
            else:
                _user_ = user_list[(i+1) % 4]
                rooms[str(data["code"])]["users"][_user_]["gamer"] = 1 # Sonraki kullanıcının oyun durumu 2 yapılur
                next_user = _user_

    if data["cartId"] == "wilddrawfour":
        data["username"] = next_user
        for i in range(4): # 4 tane kart çek
            get_deck_cart(data)

    if "drawtwo" in data["cartId"]:
        data["username"] = next_user
        for i in range(2): # 2 tane kart çek
            get_deck_cart(data)

    # Odadaki verileri cliente günceller
    socketio.emit('rooms', {"rooms": rooms})


# Flaskın Host kodu
if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=8080, debug=True)
