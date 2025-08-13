import requests
import json

def test_backend():
    """Test the backend API endpoints"""
    base_url = "https://aiqa-production-9ac6.up.railway.app"
    
    print("Testing AIQA Backend...")
    print(f"Base URL: {base_url}")
    
    # Test 1: Health check
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health Check: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Health Check Failed: {e}")
    
    # Test 2: Root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"Root Endpoint: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Root Endpoint Failed: {e}")
    
    # Test 3: Signup endpoint
    try:
        signup_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = requests.post(f"{base_url}/auth/signup", json=signup_data)
        print(f"Signup Test: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Signup Test Failed: {e}")

if __name__ == "__main__":
    test_backend()
