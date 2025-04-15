
```markdown
# Note-Taking Microservices

This repository contains microservices for a note-taking application. Each microservice (add, delete, get, update) is containerized with Docker.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed
- A [Docker Hub](https://hub.docker.com/) account
- Logged into Docker on your terminal using:

```bash
docker login
```

## Microservices

Each microservice has its own folder. Follow the steps below for each one.

---

### 1. **Add Note**

```bash
cd addNote
docker build -t <your-docker-username>/add-note:latest .
docker push <your-docker-username>/add-note:latest
cd ..
```

---

### 2. **Delete Note**

```bash
cd deleteNote
docker build -t <your-docker-username>/delete-note:latest .
docker push <your-docker-username>/delete-note:latest
cd ..
```

---

### 3. **Get Note**

```bash
cd getNote
docker build -t <your-docker-username>/get-note:latest .
docker push <your-docker-username>/get-note:latest
cd ..
```

---

### 4. **Update Note**

```bash
cd updateNote
docker build -t <your-docker-username>/update-note:latest .
docker push <your-docker-username>/update-note:latest
cd ..
```

---

## Notes

- Ensure the `Dockerfile`, `requirements.txt`, and source code (`*.py`) are present in each service directory.
- If using private Docker Hub repositories, ensure access permissions are configured correctly.

---

## License

MIT
```