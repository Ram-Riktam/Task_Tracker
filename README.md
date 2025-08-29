# MyApp – Fullstack Project

This project contains both the **frontend** (Vite + Svelte) and **backend** (Python + Aiohttp).  
The backend provides APIs, and the frontend consumes them for the user interface.


## 🚀 Getting Started

### 1. Backend (Python + Aiohttp)

**Setup**
```sh
cd backend
python3 -m venv venv
source venv/bin/activate

```

Install dependencies (including aiohttp):
```sh
pip install aiohttp
pip install -r requirements.txt

```


If you don’t have a requirements.txt yet, you can generate one after installing packages:
```sh

pip freeze > requirements.txt

```


Run Development Server
```sh

python mai.py
Backend runs at: http://localhost:8000

```

Run Tests
```sh
pytest
```
### 2.Frontend (Vite + Svelte+svelte kit)

**Setup**
```sh

cd frontend
npm install
```
Run Development Server
```sh
npm run dev
Frontend runs at: http://localhost:5173
```
Build for Production
```sh
npm run build
```
Preview Production Build
```sh
npm run preview
```
Run Tests
```sh

npm run test
```

## Running Frontend & Backend Together (Local Dev)

## Start Backend
```sh
cd backend
source venv/bin/activate
python run.py


→ runs at http://localhost:8000
```

## Start Frontend (in a new terminal)
```sh
cd frontend
npm run dev


→ runs at http://localhost:5173

Access Application
Open browser at http://localhost:5173
.
The frontend will call APIs from the backend at http://localhost:8000.
```
