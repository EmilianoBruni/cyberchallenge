title: Docker vs Docker Compose
author:
  name: Emiliano Bruni
output: docker-vs-compose.html
controls: true
theme: white

--

# Docker vs Docker Compose

## Una guida pratica ai container

--

## Cos'è Docker?

Docker è una piattaforma di containerizzazione che isola le applicazioni in **container** — processi leggeri e portabili che condividono il kernel del sistema operativo host.

A differenza delle macchine virtuali (VM), i container evitano l'overhead di un intero OS, rendendoli **più veloci** ed **efficienti** nelle risorse.

--

## Perché Usare Docker?

- ✅ **Consistenza**: Elimina il problema del "funziona sulla mia macchina".
- ✅ **Portabilità**: I container girano in modo identico su Linux, Windows o macOS.
- ✅ **Ecosistema**: Accesso a oltre 100.000 immagini su Docker Hub (es. Nginx, Redis, PostgreSQL).

--

## Architettura di Docker

- **Docker Engine**: Il nucleo (daemon, REST API, CLI).
- **Immagini**: Template in sola lettura (es. `python:3.9-slim`).
- **Container**: Istanze eseguibili delle immagini.
- **Volumi**: Storage persistente per i dati (es. database).

> Fonte: https://docs.docker.com/get-started/overview/

--

## Comandi Principali di Docker

```bash
# Costruisce un'immagine dal Dockerfile
docker build -t myapp:latest .

# Avvia un container in modalità detached
docker run -d --name myapp myapp:latest

# Crea una rete personalizzata per i container
docker network create app_net
```

--

## Esempio: Avviare un Container Redis

```bash
docker run -d --name redis_server -p 6379:6379 redis:alpine
```

- **`-d`**: Modalità detached (esecuzione in background).
- **`-p 6379:6379`**: Mappa la porta 6379 dell'host a quella del container.
- Accedi a Redis tramite `localhost:6379`.

--

## Cos'è Docker Compose?

Docker Compose è uno strumento per **definire ed eseguire applicazioni multi-container** tramite un file YAML dichiarativo (`docker-compose.yml`).

Automatizza networking, dipendenze e scaling per app complesse (es. web app con database, cache e code).

--

## Perché Usare Docker Compose?

- ✅ **Setup Dichiarativo**: Definisci servizi, reti e volumi in un unico file.
- ✅ **Gestione delle Dipendenze**: Avvia i servizi in ordine (es. database prima dell'app).
- ✅ **Sviluppo Locale**: Replica ambienti simili alla produzione sulla tua macchina.

--

## Anatomia di un File docker-compose.yml

```yaml
version: '3.8'
services:
  web:
    build: .               # Usa il Dockerfile nella directory corrente
    ports:
      - "8000:8000"
    volumes:
      - .:/app             # Ricaricamento live del codice
    depends_on:
      - db
      - redis
  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: mysecretpassword
    volumes:
      - pg_data:/var/lib/postgresql/data
  redis:
    image: redis:alpine
volumes:
  pg_data:                 # Volume named per PostgreSQL
```

--

## Comandi Principali di Docker Compose

```bash
# Costruisce le immagini e avvia i container in modalità detached
docker compose up -d --build

# Visualizza i log in tempo reale del servizio web
docker compose logs -f web

# Ferma i container ed elimina i volumi
docker compose down -v
```

--

## Docker vs Docker Compose: Differenze Principali

| Caratteristica       | Docker               | Docker Compose              |
|----------------------|----------------------|-----------------------------|
| Scope                | Singolo container    | Multi-container             |
| Configurazione       | CLI / Dockerfile     | `docker-compose.yml`        |
| Networking           | Manuale              | Automatico                  |
| Dipendenze           | Non gestite          | `depends_on`                |
| Caso d'uso tipico    | Build / Deploy       | Sviluppo locale / Stack     |

--

## Quando Usare Docker

- Testare un **singolo servizio** (es. eseguire uno script Python in un container).
- Usare strumenti effimeri:
  ```bash
  docker run --rm curlimages/curl curl https://api.example.com
  ```
- Costruire immagini personalizzate per il deployment.

--

## Quando Usare Docker Compose

- Sviluppare un'app **full-stack** (es. React + Node.js API + PostgreSQL).
- Gestire le **dipendenze** (es. assicurarsi che il database parta prima dell'app).
- Replicare **ambienti di produzione** in locale.
