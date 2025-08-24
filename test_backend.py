#!/usr/bin/env python3
"""
Test script to verify AIQA backend deployment
"""

import requests
import sys

def test_backend(url):
    """Test if backend is working"""
    print(f"🧪 Testing backend: {url}")
    
    try:
        # Test root endpoint
        response = requests.get(f"{url}/")
        if response.status_code == 200:
            print("✅ Backend is responding!")
            return True
        else:
            print(f"⚠️ Backend responded with status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend test failed: {e}")
        return False

def test_api_docs(url):
    """Test API documentation"""
    try:
        response = requests.get(f"{url}/docs")
        if response.status_code == 200:
            print("✅ API documentation is available!")
            return True
        else:
            print(f"⚠️ API docs responded with status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API docs test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 AIQA Backend Deployment Test")
    print("=" * 40)
    
    # Get backend URL from user
    backend_url = input("Enter your Render backend URL (e.g., https://aiqa-backend.onrender.com): ").strip()
    
    if not backend_url:
        print("❌ No URL provided")
        return
    
    # Remove trailing slash if present
    backend_url = backend_url.rstrip('/')
    
    print(f"\n🔗 Testing: {backend_url}")
    
    # Test backend
    if test_backend(backend_url):
        # Test API docs
        test_api_docs(backend_url)
        
        print("\n🎉 Backend deployment successful!")
        print(f"📚 API Documentation: {backend_url}/docs")
        print(f"🔗 Backend URL: {backend_url}")
        print("\nNext step: Update your Vercel frontend with this backend URL!")
    else:
        print("\n❌ Backend deployment failed or not ready yet.")
        print("Check the Render dashboard for deployment status.")

if __name__ == "__main__":
    main()
