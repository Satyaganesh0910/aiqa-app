# 🚀 AIQA Deployment Fix Guide

## Current Status
- ✅ **Frontend**: Deployed to Vercel (Working)
- ❌ **Backend**: Railway deployment failed due to account limitations

## 🔧 Quick Fix: Deploy Backend to Render.com

### Step 1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "New repository"
3. Name it: `aiqa-app`
4. Make it public
5. Don't initialize with README (we already have files)

### Step 2: Push Code to GitHub
```bash
# In your project directory (C:\Ai)
git remote add origin https://github.com/YOUR_USERNAME/aiqa-app.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy Backend to Render.com
1. Go to [Render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - **Name**: `aiqa-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

### Step 4: Update Frontend Configuration
Once Render deploys, you'll get a URL like: `https://aiqa-backend.onrender.com`

Update the frontend environment variable:
1. Go to your Vercel dashboard
2. Find your AIQA frontend project
3. Go to Settings → Environment Variables
4. Update `REACT_APP_API_URL` to your new Render backend URL

### Step 5: Test the Application
1. Visit your frontend: https://aiqa-frntend-js2op2nnj-ganeshs-projects-d35a5ce0.vercel.app
2. Create an account
3. Upload a document
4. Ask questions

## 🎯 Alternative: Deploy to Heroku

If Render.com doesn't work, try Heroku:

### Step 1: Install Heroku CLI
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Deploy to Heroku
```bash
cd backend
heroku create aiqa-backend
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Step 3: Update Frontend
Update `REACT_APP_API_URL` to your Heroku URL.

## 🔍 Troubleshooting

### Common Issues:
1. **Module not found errors**: Make sure all dependencies are in `requirements.txt`
2. **CORS errors**: Backend CORS is configured to allow all origins
3. **Database issues**: SQLite database will be created automatically

### Testing Backend:
```bash
# Test locally
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📱 Your Current Links

- **Frontend**: https://aiqa-frntend-js2op2nnj-ganeshs-projects-d35a5ce0.vercel.app
- **Backend**: https://aiqa-production-9ac6.up.railway.app (broken)

## 🎉 Expected Result

After fixing the backend deployment, you'll have:
- ✅ Working user authentication
- ✅ File upload functionality
- ✅ AI-powered Q&A
- ✅ Modern React UI
- ✅ Full-stack application

## 📞 Need Help?

If you encounter issues:
1. Check the deployment logs in Render/Heroku dashboard
2. Verify all environment variables are set
3. Test the backend endpoints directly
4. Check the frontend console for errors
