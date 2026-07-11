#!/bin/bash

# Setup script for Macron AI on Replit

echo "🚀 Setting up Macron AI Application..."

# Create necessary directories
mkdir -p scripts
mkdir -p backend/logs
mkdir -p frontend/dist

# Make scripts executable
chmod +x scripts/post-merge.sh
chmod +x .replit-run.sh
chmod +x setup.sh

# Backend setup
echo "📦 Installing backend dependencies..."
cd backend
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Backend dependencies installed"
cd ..

# Frontend setup
echo "📦 Installing frontend dependencies..."
cd frontend
pnpm install
echo "✅ Frontend dependencies installed"
cd ..

# Create .env if it doesn't exist
if [ ! -f backend/.env ]; then
  echo "🔧 Creating backend .env configuration..."
  cp backend/.env.example backend/.env
  echo "⚠️  Please add your OPENAI_API_KEY to backend/.env"
fi

echo ""
echo "✨ Setup completed! To start the application:"
echo "   Run: pnpm dev"
echo ""
echo "📝 Make sure to set your OPENAI_API_KEY in the Secrets tab"
echo "🌐 Your app will be available at: https://{your-replit-url}.replit.dev"
