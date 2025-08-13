#!/bin/bash

echo "🚀 Deploying AIQA to Railway..."

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Installing..."
    npm install -g @railway/cli
fi

# Login to Railway
echo "🔐 Logging into Railway..."
railway login

# Initialize Railway project (if not already done)
echo "📦 Initializing Railway project..."
cd backend
railway init

# Deploy the backend
echo "🚀 Deploying backend..."
railway up

# Get the backend URL
BACKEND_URL=$(railway status --json | jq -r '.url')
echo "✅ Backend deployed at: $BACKEND_URL"

# Update frontend API configuration
echo "🔧 Updating frontend API configuration..."
cd ../backend/frontend

# Create environment file for frontend
cat > .env << EOF
REACT_APP_API_URL=$BACKEND_URL
EOF

# Deploy frontend to Vercel
echo "🚀 Deploying frontend to Vercel..."
npm install -g vercel
vercel --prod

echo "✅ Deployment complete!"
echo "🌐 Your AIQA application is now live!"
