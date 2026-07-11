#!/bin/bash

# Post-merge script for Replit
set -e

echo "Running post-merge setup..."

# Backend setup
echo "Setting up backend..."
cd backend
pip install -r requirements.txt
cd ..

# Frontend setup
echo "Setting up frontend..."
cd frontend
pnpm install
cd ..

echo "Post-merge setup completed!"
