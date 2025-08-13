# 🚀 AIQA Deployment Guide

This guide will help you deploy AIQA to get a public link where everyone can use it.

## 📋 Prerequisites

- GitHub account
- Railway account (free tier available)
- Vercel account (free tier available)
- Node.js and npm installed locally

## 🎯 Quick Deployment (Recommended)

### Step 1: Deploy Backend to Railway

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

4. **Initialize Railway project:**
   ```bash
   railway init
   ```

5. **Deploy the backend:**
   ```bash
   railway up
   ```

6. **Get your backend URL:**
   ```bash
   railway status
   ```
   Copy the URL (e.g., `https://your-app-name.railway.app`)

### Step 2: Deploy Frontend to Vercel

1. **Navigate to frontend directory:**
   ```bash
   cd backend/frontend
   ```

2. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

3. **Create environment file:**
   ```bash
   echo "REACT_APP_API_URL=https://your-backend-url.railway.app" > .env
   ```
   Replace `your-backend-url` with your actual Railway URL.

4. **Deploy to Vercel:**
   ```bash
   vercel --prod
   ```

5. **Follow the prompts:**
   - Link to existing project: No
   - Project name: aiqa-frontend (or any name)
   - Directory: ./
   - Override settings: No

## 🔧 Alternative: Manual Deployment

### Backend Deployment (Railway)

1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Choose "Deploy from GitHub repo"
4. Select your AIQA repository
5. Set the root directory to `backend`
6. Add environment variables if needed
7. Deploy

### Frontend Deployment (Vercel)

1. Go to [Vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Set the root directory to `backend/frontend`
5. Add environment variable:
   - Name: `REACT_APP_API_URL`
   - Value: Your Railway backend URL
6. Deploy

## 🌐 Your Public Links

After deployment, you'll have:

- **Frontend (Public):** `https://your-app-name.vercel.app`
- **Backend API:** `https://your-app-name.railway.app`
- **API Documentation:** `https://your-app-name.railway.app/docs`

## 🔍 Testing Your Deployment

1. Visit your Vercel frontend URL
2. Create a new account
3. Upload a test document (PDF, image, or text file)
4. Ask questions about the document
5. Verify everything works correctly

## 🛠️ Troubleshooting

### Common Issues:

1. **CORS Errors:**
   - Ensure your backend CORS settings allow your frontend domain
   - Check the `allow_origins` setting in `backend/app/main.py`

2. **Environment Variables:**
   - Verify `REACT_APP_API_URL` is set correctly in Vercel
   - Check that the backend URL is accessible

3. **File Upload Issues:**
   - Ensure the `uploads` directory exists in Railway
   - Check file size limits (Railway has limits)

4. **Database Issues:**
   - Railway uses ephemeral storage, so data may be lost on restarts
   - Consider using a persistent database like PostgreSQL

## 🔄 Updating Your Deployment

### Backend Updates:
```bash
cd backend
railway up
```

### Frontend Updates:
```bash
cd backend/frontend
vercel --prod
```

## 📊 Monitoring

- **Railway Dashboard:** Monitor backend performance and logs
- **Vercel Dashboard:** Monitor frontend performance and analytics
- **API Health Check:** Visit `/health` endpoint on your backend URL

## 💰 Cost Considerations

- **Railway:** Free tier includes 500 hours/month
- **Vercel:** Free tier includes unlimited deployments
- **Total Cost:** $0 for basic usage

## 🎉 Success!

Your AIQA application is now live and accessible to everyone! Share your Vercel URL with users to let them:

- Create accounts
- Upload documents
- Ask AI-powered questions
- Get intelligent responses

## 📞 Support

If you encounter issues:
1. Check the logs in Railway and Vercel dashboards
2. Verify all environment variables are set correctly
3. Test the API endpoints directly using the `/docs` URL
4. Ensure all dependencies are properly installed

---

**🎯 Your AIQA is now live at:** `https://your-app-name.vercel.app`
