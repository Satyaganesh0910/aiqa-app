#!/usr/bin/env python3
"""
AIQA Deployment Script
Helps deploy the backend to Render.com
"""

import os
import subprocess
import sys
import webbrowser
import time

def check_git_status():
    """Check if git repository is ready"""
    print("🔍 Checking Git repository...")
    
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git repository found")
            return True
        else:
            print("❌ Git repository not found")
            return False
    except FileNotFoundError:
        print("❌ Git not installed. Please install Git first.")
        return False

def create_github_repo():
    """Guide user to create GitHub repository"""
    print("\n📝 GitHub Repository Setup:")
    print("1. Go to https://github.com")
    print("2. Click 'New repository'")
    print("3. Name it: aiqa-app")
    print("4. Make it public")
    print("5. Don't initialize with README")
    print("6. Click 'Create repository'")
    
    input("\nPress Enter when you've created the repository...")
    
    # Get the repository URL
    username = input("Enter your GitHub username: ")
    repo_url = f"https://github.com/{username}/aiqa-app.git"
    
    return repo_url

def setup_git_remote(repo_url):
    """Setup git remote and push code"""
    print(f"\n🚀 Setting up Git remote: {repo_url}")
    
    try:
        # Add remote
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        print("✅ Remote added")
        
        # Push to GitHub
        subprocess.run(['git', 'branch', '-M', 'main'], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
        print("✅ Code pushed to GitHub")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False

def deploy_to_render():
    """Guide user to deploy to Render.com"""
    print("\n🌐 Render.com Deployment:")
    print("1. Go to https://render.com")
    print("2. Sign up/Login with GitHub")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Configure the service:")
    print("   - Name: aiqa-backend")
    print("   - Root Directory: backend")
    print("   - Environment: Python 3")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT")
    print("   - Plan: Free")
    
    input("\nPress Enter when you've configured Render...")
    
    # Open Render.com
    webbrowser.open("https://render.com")
    
    return input("\nEnter your Render backend URL (e.g., https://aiqa-backend.onrender.com): ")

def update_frontend_config(backend_url):
    """Guide user to update frontend configuration"""
    print(f"\n🔧 Frontend Configuration:")
    print(f"Backend URL: {backend_url}")
    print("\n1. Go to your Vercel dashboard")
    print("2. Find your AIQA frontend project")
    print("3. Go to Settings → Environment Variables")
    print("4. Update REACT_APP_API_URL to:")
    print(f"   {backend_url}")
    
    input("\nPress Enter when you've updated the frontend...")

def test_deployment(backend_url):
    """Test the deployed backend"""
    print(f"\n🧪 Testing deployment: {backend_url}")
    
    try:
        import requests
        response = requests.get(f"{backend_url}/")
        if response.status_code == 200:
            print("✅ Backend is working!")
            return True
        else:
            print(f"⚠️ Backend responded with status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend test failed: {e}")
        return False

def main():
    """Main deployment process"""
    print("🚀 AIQA Deployment to Render.com")
    print("=" * 40)
    
    # Check git status
    if not check_git_status():
        return
    
    # Create GitHub repository
    repo_url = create_github_repo()
    
    # Setup git remote
    if not setup_git_remote(repo_url):
        return
    
    # Deploy to Render
    backend_url = deploy_to_render()
    
    # Update frontend
    update_frontend_config(backend_url)
    
    # Test deployment
    if test_deployment(backend_url):
        print("\n🎉 Deployment successful!")
        print(f"Frontend: https://aiqa-frntend-js2op2nnj-ganeshs-projects-d35a5ce0.vercel.app")
        print(f"Backend: {backend_url}")
        print("\nYour AIQA application is now fully functional!")
    else:
        print("\n⚠️ Deployment may need some time to complete.")
        print("Check the Render dashboard for deployment status.")

if __name__ == "__main__":
    main()
