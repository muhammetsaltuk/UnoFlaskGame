# 🃏 UNO Kart Oyunu - Flask Web Uygulaması

Bu proje, yazılım mühendisliği öğrencisi olarak geliştirdiğim, **Flask** ve **Socket.IO** teknolojileri kullanılarak oluşturulmuş çok oyunculu bir **UNO kart oyunu** web uygulamasıdır.

## 🎯 Proje Hakkında

UNO, dünya çapında popüler olan bir kart oyunudur. Bu proje, klasik UNO oyununu modern web teknolojileri ile birleştirerek, arkadaşlarınızla online olarak oynayabileceğiniz interaktif bir platform sunar.

### ✨ Özellikler

- **Gerçek Zamanlı Oyun**: Socket.IO ile anlık iletişim
- **Çok Oyunculu Destek**: 4 kişiye kadar aynı anda oynayabilme
- **Oda Sistemi**: Özel oda kodları ile oyun oluşturma ve katılma
- **Görsel Arayüz**: CSS ile tasarlanmış modern oyun arayüzü
- **Kart Animasyonları**: Etkileşimli kart görselleri
- **Oyun Kuralları**: Standart UNO kurallarına uygun oynanış

## 🛠️ Teknolojiler

### Backend
- **Python 3.x**
- **Flask** - Web framework
- **Flask-SocketIO** - Gerçek zamanlı iletişim
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Sayfa yapısı
- **CSS3** - Stil ve animasyonlar
- **JavaScript (ES6+)** - Oyun mantığı
- **jQuery** - DOM manipülasyonu
- **Socket.IO Client** - Sunucu iletişimi

### Oyun Mantığı
- **UNO Kart Sistemi**: 108 kart (4 renk × 13 değer + özel kartlar)
- **Oyun Durumu Yönetimi**: Oda, kullanıcı ve oyun verilerinin senkronizasyonu
- **Kart Kuralları**: Skip, Reverse, Draw Two, Wild, Wild Draw Four

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
```bash
Python 3.7+
pip
```

### Adım 1: Projeyi İndirin
```bash
git clone <repository-url>
cd UnoFlaskGame
```

### Adım 2: Gerekli Paketleri Yükleyin
```bash
pip install flask flask-socketio flask-cors
```

### Adım 3: Uygulamayı Çalıştırın
```bash
python index.py
```

### Adım 4: Tarayıcıda Açın
```
http://127.0.0.1:8080
```

## 🎮 Nasıl Oynanır

### 1. Oyun Oluşturma
- Ana sayfada kullanıcı adınızı girin
- "Yeni Oyun Oluştur" butonuna tıklayın
- Sistem size 8 haneli bir oyun kodu verecek

### 2. Oyuna Katılma
- Kullanıcı adınızı girin
- "Oyuna Katıl" butonuna tıklayın
- Oyun kodunu girin
- Mevcut odalar listesinden birini seçin

### 3. Oyun Kuralları
- Her oyuncuya 7 kart dağıtılır
- Ortaya bir kart açılır
- Sırayla uygun kartları atın
- Özel kartların güçlerini kullanın
- İlk elindeki kartları bitiren oyuncu kazanır

## 📁 Proje Yapısı

```
UnoFlaskGame/
├── index.py              # Ana Flask uygulaması
├── uno.py                # UNO oyun mantığı
├── templates/            # HTML şablonları
│   ├── index.html       # Oyun sayfası
│   └── login.html       # Giriş sayfası
├── public/              # Statik dosyalar
│   ├── assets/          # Oyun görselleri
│   ├── css/             # Stil dosyaları
│   └── js/              # JavaScript dosyaları
└── README.md            # Bu dosya
```

## 🔧 Teknik Detaylar

### Socket.IO Event'leri
- `connect` - Kullanıcı bağlantısı
- `join_room` - Odaya katılma/oluşturma
- `send_cart` - Kart atma
- `get_deck_cart` - Kart çekme
- `exit_room` - Odadan çıkma

### Oyun Durumu Yönetimi
- **Oda Sistemi**: Her oda benzersiz kod ve hash ile tanımlanır
- **Kullanıcı Yönetimi**: Maksimum 4 oyuncu per oda
- **Oyun Senkronizasyonu**: Tüm oyuncular için gerçek zamanlı güncelleme

### Güvenlik Özellikleri
- **Hash Doğrulama**: Oda kodları SHA-256 ile şifrelenir
- **Oda Erişim Kontrolü**: Sadece geçerli hash ile odaya erişim

## 🎨 Görsel Tasarım

- **Responsive Tasarım**: Farklı ekran boyutlarına uyumlu
- **Kart Görselleri**: PNG formatında yüksek kaliteli kart tasarımları
- **Renk Teması**: UNO oyununun karakteristik renkleri (kırmızı, mavi, yeşil, sarı)
- **Animasyonlar**: Hover efektleri ve kart etkileşimleri

## 🚧 Geliştirme Notları

Bu proje, yazılım mühendisliği eğitimi sırasında öğrenilen temel kavramları pratiğe dökme amacıyla geliştirilmiştir:

- **Web Development**: Flask framework kullanımı
- **Real-time Communication**: Socket.IO ile anlık veri transferi
- **Game Logic**: Oyun kurallarının programatik implementasyonu
- **Frontend-Backend Integration**: Modern web uygulaması mimarisi
- **User Experience**: Kullanıcı dostu arayüz tasarımı

---

---

# 🃏 UNO Card Game - Flask Web Application

This project is a **multiplayer UNO card game** web application developed as a software engineering student, built using **Flask** and **Socket.IO** technologies.

## 🎯 About the Project

UNO is a popular card game worldwide. This project combines the classic UNO game with modern web technologies, providing an interactive platform where you can play online with your friends.

### ✨ Features

- **Real-time Gaming**: Instant communication with Socket.IO
- **Multiplayer Support**: Play with up to 4 players simultaneously
- **Room System**: Create and join games with private room codes
- **Visual Interface**: Modern game interface designed with CSS
- **Card Animations**: Interactive card graphics
- **Game Rules**: Gameplay following standard UNO rules

## 🛠️ Technologies

### Backend
- **Python 3.x**
- **Flask** - Web framework
- **Flask-SocketIO** - Real-time communication
- **Flask-CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Page structure
- **CSS3** - Styles and animations
- **JavaScript (ES6+)** - Game logic
- **jQuery** - DOM manipulation
- **Socket.IO Client** - Server communication

### Game Logic
- **UNO Card System**: 108 cards (4 colors × 13 values + special cards)
- **Game State Management**: Synchronization of room, user, and game data
- **Card Rules**: Skip, Reverse, Draw Two, Wild, Wild Draw Four

## 🚀 Installation and Setup

### Requirements
```bash
Python 3.7+
pip
```

### Step 1: Download the Project
```bash
git clone <repository-url>
cd UnoFlaskGame
```

### Step 2: Install Required Packages
```bash
pip install flask flask-socketio flask-cors
```

### Step 3: Run the Application
```bash
python index.py
```

### Step 4: Open in Browser
```
http://127.0.0.1:8080
```

## 🎮 How to Play

### 1. Creating a Game
- Enter your username on the main page
- Click "Create New Game" button
- The system will give you an 8-digit game code

### 2. Joining a Game
- Enter your username
- Click "Join Game" button
- Enter the game code
- Select one from the existing rooms list

### 3. Game Rules
- Each player is dealt 7 cards
- One card is opened in the center
- Take turns playing appropriate cards
- Use the power of special cards
- The first player to run out of cards wins

## 📁 Project Structure

```
UnoFlaskGame/
├── index.py              # Main Flask application
├── uno.py                # UNO game logic
├── templates/            # HTML templates
│   ├── index.html       # Game page
│   └── login.html       # Login page
├── public/              # Static files
│   ├── assets/          # Game graphics
│   ├── css/             # Style files
│   └── js/              # JavaScript files
└── README.md            # This file
```

## 🔧 Technical Details

### Socket.IO Events
- `connect` - User connection
- `join_room` - Join/create room
- `send_cart` - Play card
- `get_deck_cart` - Draw card
- `exit_room` - Exit room

### Game State Management
- **Room System**: Each room is defined with unique code and hash
- **User Management**: Maximum 4 players per room
- **Game Synchronization**: Real-time updates for all players

### Security Features
- **Hash Verification**: Room codes are encrypted with SHA-256
- **Room Access Control**: Access only with valid hash

## 🎨 Visual Design

- **Responsive Design**: Compatible with different screen sizes
- **Card Graphics**: High-quality card designs in PNG format
- **Color Theme**: UNO game's characteristic colors (red, blue, green, yellow)
- **Animations**: Hover effects and card interactions

## 🚧 Development Notes

This project was developed to put into practice the fundamental concepts learned during software engineering education:

- **Web Development**: Using Flask framework
- **Real-time Communication**: Instant data transfer with Socket.IO
- **Game Logic**: Programmatic implementation of game rules
- **Frontend-Backend Integration**: Modern web application architecture
- **User Experience**: User-friendly interface design








