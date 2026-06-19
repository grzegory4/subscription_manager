# SubManager - Menedżer Subskrypcji

SubManager to nowoczesna aplikacja webowa do zarządzania subskrypcjami (Netflix, Spotify, Disney+, itp.). Pozwala użytkownikom śledzić wydatki, monitorować nadchodzące płatności oraz zarządzać okresami próbnymi (trial).

## 🚀 Technologie

### Backend
- **Django 5.0** & **Django REST Framework**
- **JWT (SimpleJWT)** - Autentykacja
- **PostgreSQL** - Baza danych (produkcyjna)
- **drf-spectacular** - Dokumentacja API (Swagger/OpenAPI)
- **django-money** - Obsługa wielu walut

### Frontend
- **Vue.js 3 (Composition API)**
- **Vite** - Narzędzie budowania
- **Tailwind CSS** - Framework CSS
- **PrimeVue** - Biblioteka komponentów UI
- **Pinia** - Zarządzanie stanem
- **Chart.js** - Wizualizacja danych (wykresy)

## ✨ Główne Funkcje

- 🔐 **Bezpieczne logowanie i rejestracja** przy użyciu tokenów JWT.
- 📊 **Panel główny (Dashboard)** z podsumowaniem miesięcznych i rocznych wydatków.
- 📈 **Wykres kołowy** przedstawiający rozkład wydatków na kategorie.
- 📅 **Zarządzanie subskrypcjami**: Dodawanie, edycja i usuwanie usług.
- ⏳ **Obsługa okresów próbnych**: Oznaczanie subskrypcji jako "trial" z przypomnieniem o dacie zakończenia.
- 💰 **Wielowalutowość**: Obsługa PLN, USD oraz EUR.
- 🌙 **Modern UI**: Ciemny interfejs z płynnymi animacjami i responsywnym designem.

## 🛠️ Uruchomienie i konfiguracja

Najprostszym i zalecanym sposobem na uruchomienie całego projektu (Backend, Frontend oraz Baza danych PostgreSQL) jest użycie **Dockera**.

### Wymagania
- Docker oraz Docker Compose

### Szybki start z Dockerem

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/grzegory4/subscription_manager.git
   cd subscription_manager
   ```

2. **Przygotuj plik konfiguracyjny `.env`:**
   Skopiuj szablon zmiennych środowiskowych do pliku `.env`:
   ```bash
   cp .env.template .env
   ```
   *(Opcjonalnie) Możesz edytować plik `.env`, aby zmienić domyślne hasła lub nazwy baz danych.*

3. **Uruchom projekt za pomocą Docker Compose:**
   ```bash
   docker-compose up --build
   ```

Po zakończeniu budowania i uruchomieniu kontenerów:
- **Frontend** jest dostępny pod adresem: [http://localhost:5173](http://localhost:5173)
- **Backend API** działa pod adresem: [http://localhost:8000](http://localhost:8000)

---

### 💻 Tradycyjne uruchomienie lokalne (opcjonalnie)

Jeśli wolisz uruchomić aplikację bez Dockera, wykonaj poniższe kroki (wymaga zainstalowanego Pythona 3.10+ oraz Node.js 18+):

#### 1. Backend (Django)
```bash
# Utwórz środowisko wirtualne i je aktywuj
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Zainstaluj zależności
pip install -r requirements.txt

# Przygotuj plik .env
cp .env.template .env

# Uruchom migracje bazy danych
python manage.py migrate

# Uruchom serwer deweloperski
python manage.py runserver
```

#### 2. Frontend (Vue)
```bash
cd frontend

# Zainstaluj zależności
npm install

# Uruchom serwer deweloperski
npm run dev
```

## 📖 Dokumentacja API

Po uruchomieniu serwera backendowego, dokumentacja API jest dostępna pod adresami:
- **Swagger UI:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **Redoc:** [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

---
*Projekt stworzony na potrzeby przedmiotu Praktyka Zawodowa.*
