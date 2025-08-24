#!/usr/bin/env python3
"""
AIQA Auto-Deployment Script
Guides you through deployment with minimal manual steps
"""

import os
import subprocess
import sys
import webbrowser
import time
import requests

def print_banner():
    """Print welcome banner"""
    print("🚀 AIQA Auto-Deployment Helper")
    print("=" * 40)
    print("I'll guide you through deploying your AIQA app!")
    print("This will take about 10-15 minutes total.\n")

def check_prerequisites():
    """Check if everything is ready"""
    print("🔍 Checking prerequisites...")
    
    # Check if we're in the right directory
    if not os.path.exists("backend/app/main.py"):
        print("❌ Please run this script from the project root directory (C:\\Ai)")
        return False
    
    # Check if git is available
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        print("✅ Git is installed")
    except:
        print("❌ Git is not installed. Please install Git first.")
        return False
    
    print("✅ All prerequisites met!")
    return True

def step_1_github():
    """Step 1: GitHub Repository Setup"""
    print("\n📝 STEP 1: Create GitHub Repository")
    print("-" * 30)
    print("1. I'll open GitHub for you")
    print("2. Create a new repository named 'aiqa-app'")
    print("3. Make it public")
    print("4. Don't initialize with README")
    
    input("\nPress Enter when you're ready to open GitHub...")
    webbrowser.open("https://github.com/new")
    
    print("\n📋 Instructions:")
    print("- Repository name: aiqa-app")
    print("- Make it public")
    print("- Don't initialize with README")
    print("- Click 'Create repository'")
    
    input("\nPress Enter when you've created the repository...")
    
    # Get GitHub username
    username = input("Enter your GitHub username: ").strip()
    if not username:
        print("❌ Username is required!")
        return None
    
    repo_url = f"https://github.com/{username}/aiqa-app.git"
    print(f"✅ Repository URL: {repo_url}")
    return repo_url

def step_2_push_code(repo_url):
    """Step 2: Push code to GitHub"""
    print("\n🚀 STEP 2: Push Code to GitHub")
    print("-" * 30)
    
    try:
        # Add remote
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        print("✅ Remote added")
        
        # Push to GitHub
        subprocess.run(['git', 'branch', '-M', 'main'], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
        print("✅ Code pushed to GitHub successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error pushing code: {e}")
        return False

def step_3_render():
    """Step 3: Deploy to Render.com"""
    print("\n🌐 STEP 3: Deploy to Render.com")
    print("-" * 30)
    print("1. I'll open Render.com for you")
    print("2. Sign up/Login with GitHub")
    print("3. Create a new Web Service")
    print("4. Connect your repository")
    
    input("\nPress Enter to open Render.com...")
    webbrowser.open("https://render.com")
    
    print("\n📋 Render.com Configuration:")
    print("- Click 'New +' → 'Web Service'")
    print("- Connect your GitHub repository")
    print("- Configure the service:")
    print("  • Name: aiqa-backend")
    print("  • Root Directory: backend")
    print("  • Environment: Python 3")
    print("  • Build Command: pip install -r requirements.txt")
    print("  • Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT")
    print("  • Plan: Free")
    
    input("\nPress Enter when you've configured Render...")
    
    # Get the Render URL
    render_url = input("Enter your Render backend URL (e.g., https://aiqa-backend.onrender.com): ").strip()
    if not render_url:
        print("❌ Render URL is required!")
        return None
    
    return render_url

def step_4_update_frontend(render_url):
    """Step 4: Update frontend configuration"""
    print("\n🔧 STEP 4: Update Frontend Configuration")
    print("-" * 40)
    
    # Update vercel.json
    vercel_config_path = "backend/frontend/vercel.json"
    if os.path.exists(vercel_config_path):
        with open(vercel_config_path, 'r') as f:
            content = f.read()
        
        # Replace the placeholder URL
        updated_content = content.replace(
            "https://your-new-backend-url.onrender.com",
            render_url
        )
        
        with open(vercel_config_path, 'w') as f:
            f.write(updated_content)
        
        print(f"✅ Updated vercel.json with backend URL: {render_url}")
    
    print("\n📋 Frontend Update Instructions:")
    print("1. Go to Vercel Dashboard: https://vercel.com/dashboard")
    print("2. Find your AIQA frontend project")
    print("3. Go to Settings → Environment Variables")
    print("4. Update REACT_APP_API_URL to:")
    print(f"   {render_url}")
    print("5. Save and redeploy")
    
    input("\nPress Enter when you've updated the frontend...")

def step_5_test_deployment(render_url):
    """Step 5: Test the deployment"""
    print("\n🧪 STEP 5: Test Deployment")
    print("-" * 25)
    
    print(f"Testing backend: {render_url}")
    
    try:
        response = requests.get(f"{render_url}/", timeout=10)
        if response.status_code == 200:
            print("✅ Backend is working!")
            return True
        else:
            print(f"⚠️ Backend responded with status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend test failed: {e}")
        print("This is normal if deployment is still in progress.")
        return False

def main():
    """Main deployment process"""
    print_banner()
    
    if not check_prerequisites():
        return
    
    # Step 1: GitHub
    repo_url = step_1_github()
    if not repo_url:
        return
    
    # Step 2: Push code
    if not step_2_push_code(repo_url):
        return
    
    # Step 3: Render
    render_url = step_3_render()
    if not render_url:
        return
    
    # Step 4: Update frontend
    step_4_update_frontend(render_url)
    
    # Step 5: Test
    print("\n⏳ Waiting for deployment to complete...")
    print("This may take 5-10 minutes. You can check the Render dashboard for progress.")
    
    time.sleep(30)  # Wait 30 seconds
    
    if step_5_test_deployment(render_url):
        print("\n🎉 DEPLOYMENT SUCCESSFUL!")
        print("=" * 30)
        print("Your AIQA application is now fully functional!")
        print(f"Frontend: https://aiqa-frntend-js2op2nnj-ganeshs-projects-d35a5ce0.vercel.app")
        print(f"Backend: {render_url}")
        print("\n🚀 You can now:")
        print("1. Visit your frontend URL")
        print("2. Create an account")
        print("3. Upload documents")
        print("4. Ask AI-powered questions!")
    else:
        print("\n⚠️ Deployment may still be in progress.")
        print("Check the Render dashboard and try again in a few minutes.")

if __name__ == "__main__":
    main()
