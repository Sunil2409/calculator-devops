# DevOps Calculator

A stateful calculator application designed for deploying and testing infrastructure pipelines (Docker, Kubernetes, Ansible, Terraform, and AWS).

## Architecture
* **Backend:** FastAPI, SQLAlchemy, SQLite (Phase 1)
* **Frontend:** React.js (via Vite), Axios
* **Infrastructure:** (Upcoming) Docker, Kubernetes, Terraform, AWS

## Local Development Setup

### Prerequisites
* Python 3.x
* Node.js & npm (≥ 20.19.0)

### 1. Backend Setup
Navigate to the backend directory, set up the virtual environment, and start the FastAPI server:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn main:app --reload
```
The backend API will be available at `http://localhost:8000`.

### 2. Frontend Setup
Open a new terminal, navigate to the frontend directory, install dependencies, and start the Vite server:

```bash
cd frontend
npm install
npm run dev
```
The frontend UI will be available at `http://localhost:5173`.
