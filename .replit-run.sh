#!/bin/bash

# Start both backend and frontend services

# Check if .env file exists
if [ ! -f backend/.env ]; then
  echo "Creating backend .env file..."
  cp backend/.env.example backend/.env
fi

echo "Starting Macron AI Application..."

# Start backend in background
echo "Starting FastAPI backend on port 8000..."
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Start frontend in background
echo "Starting React frontend on port 3000..."
cd frontend
pnpm dev &
FRONTEND_PID=$!
cd ..

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID
