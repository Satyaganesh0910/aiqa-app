# 🚀 Quick Deployment Guide - AIQA Application

## Your GitHub Repository
✅ **Repository**: https://github.com/Satyaganesh0910/aiqa-app
✅ **Code**: Successfully pushed and ready for deployment

## Step 1: Deploy Backend to Render.com (5 minutes)

1. **Visit**: https://render.com
2. **Sign up/Login** with GitHub
3. **Click "New +"** → **"Web Service"**
4. **Connect Repository**: `Satyaganesh0910/aiqa-app`
5. **Configure**:
   - **Name**: `aiqa-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: `Free`
6. **Click "Create Web Service"**

**Wait 5-10 minutes for deployment**

## Step 2: Update Frontend (2 minutes)

1. **Go to**: https://vercel.com/dashboard
2. **Find your AIQA frontend project**
3. **Settings** → **Environment Variables**
4. **Update `REACT_APP_API_URL`** to your Render backend URL

## Step 3: Your Public Links

- **Frontend**: https://aiqa-frntend-js2op2nnj-ganeshs-projects-d35a5ce0.vercel.app
- **Backend**: `https://your-app-name.onrender.com` (from Render)
- **API Docs**: `https://your-app-name.onrender.com/docs`

## 🎉 Success!

Your AIQA application will be fully functional and accessible to everyone!

## Features Available:
- ✅ User registration and login
- ✅ File upload (PDF, images, text)
- ✅ AI-powered Q&A about documents
- ✅ Modern responsive UI
- ✅ Secure API endpoints

## Need Help?
- Check Render deployment logs
- Verify environment variables
- Test API endpoints at `/docs` URL
