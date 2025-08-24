#!/usr/bin/env python3
"""
Local Backend Test Script
Tests the AIQA backend locally before deployment
"""

import subprocess
import sys
import time
import requests
import os

def test_backend_locally():
    """Test the backend locally"""
    print("🧪 Testing AIQA Backend Locally...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("app/main.py"):
        print("❌ Error: Please run this script from the backend directory")
        print("   Current directory:", os.getcwd())
        return False
    
    # Check dependencies
    print("📦 Checking dependencies...")
    try:
        import fastapi
        import uvicorn
        import sqlalchemy
        print("✅ All required packages are installed")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("   Run: pip install -r requirements.txt")
        return False
    
    # Test importing the app
    print("🔧 Testing app import...")
    try:
        sys.path.append('.')
        from app.main import app
        print("✅ FastAPI app imported successfully")
    except Exception as e:
        print(f"❌ Failed to import app: {e}")
        return False
    
    # Test database
    print("🗄️ Testing database...")
    try:
        from app.database import engine
        from app.models import Base
        Base.metadata.create_all(bind=engine)
        print("✅ Database setup successful")
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False
    
    print("\n🎉 Local backend test passed!")
    print("   You can now deploy to Render.com or Heroku")
    return True

def start_local_server():
    """Start the local development server"""
    print("\n🚀 Starting local development server...")
    print("   The server will be available at: http://localhost:8000")
    print("   Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "start":
        start_local_server()
    else:
        test_backend_locally()
