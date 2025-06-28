# Email Security Pipeline (FastAPI + Temporal + MySQL)

## 📦 Project Setup

### 1️⃣ Clone Repository and Install Dependencies

```bash
git clone <repo-url>
cd email_security_pipeline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Initialize MySQL Database

* Ensure Docker is running.
* Start MySQL container using `docker-compose up -d`.
* Connect to MySQL:

```bash
docker exec -it email_security_pipeline-db-1 mysql -u root -p
```

* Create database and tables:

```sql
CREATE DATABASE email_signal_processing;
USE email_signal_processing;

CREATE TABLE emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(255),
    subject VARCHAR(255),
    timestamp DATETIME,
    links TEXT
);

CREATE TABLE signals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email_id INT,
    domain_reputation VARCHAR(50),
    url_entropy FLOAT,
    sender_spoof_check BOOLEAN
);
```

### 3️⃣ Run Services

```bash
docker-compose up --build
```

### 4️⃣ Test the Pipeline

Send a POST request:

```bash
curl -X POST http://localhost:8000/ingest \
    -H "Content-Type: application/json" \
    -d '{"sender":"test@example.com","subject":"Testing","timestamp":"2025-06-28T12:00:00Z","links":"http://example.com"}'
```

### 5️⃣ Manage Temporal Workflows

List workflows:

```bash
docker exec -it temporal tctl --address temporal:7233 workflow list --query "ExecutionStatus='Running'"
```

Terminate a stuck workflow:

```bash
docker exec -it temporal tctl --address temporal:7233 workflow terminate \
    --workflow_id <workflow_id> \
    --reason "Cleaning stuck workflow"
```

---

✅ You now have a **clean, working README** for your `email_security_pipeline` with MySQL table initialization, Temporal workflow management, and clear testing instructions.
