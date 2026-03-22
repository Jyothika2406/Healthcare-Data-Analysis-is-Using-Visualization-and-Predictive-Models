# Vercel Deployment Guide - Healthcare Data Analysis

## Prerequisites

1. **Vercel Account**: Create a free account at [vercel.com](https://vercel.com)
2. **GitHub Account**: Push your code to GitHub
3. **MongoDB Atlas Account**: Ensure your MongoDB cluster is set up with proper IP whitelist

## Step-by-Step Deployment

### 1. Prepare Your Project

Ensure you have these files in your project root:
- `app.py` (main Flask app)
- `requirements.txt` (with all dependencies)
- `vercel.json` (Vercel configuration)
- `api/index.py` (WSGI entry point)

### 2. Update MongoDB Atlas Cluster

Your MongoDB Atlas cluster needs to allow connections from Vercel's servers:

1. Go to MongoDB Atlas Dashboard
2. Click **Network Access** (under Security)
3. Click **+ ADD IP ADDRESS**
4. Select **ALLOW ACCESS FROM ANYWHERE** (0.0.0.0/0)
   - Note: This is required because Vercel's IP addresses are dynamic
   - Alternatively, add these IP ranges if available:
     - Vercel's deployment node IPs (check Vercel documentation)

5. Your MONGO_URI should look like:
   ```
   mongodb+srv://username:password@cluster0.mongodb.net/healthcare_db?retryWrites=true&w=majority&appName=Cluster0
   ```

### 3. Push Code to GitHub

```bash
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

### 4. Deploy to Vercel

#### Option A: Using Vercel Dashboard (Recommended)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **Import Project**
3. Paste your GitHub repository URL
4. Click **Continue**
5. **Configure Project:**
   - Framework Preset: **Other**
   - Build Command: (leave empty)
   - Install Command: `pip install -r requirements.txt`
   - Output Directory: (leave empty)
6. Click **Deploy**

#### Option B: Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Follow the prompts
```

### 5. Set Environment Variables

After deploying, set your environment variables in Vercel:

1. Go to your Vercel project dashboard
2. Click **Settings** → **Environment Variables**
3. Add these variables:

| Variable | Value |
|----------|-------|
| `MONGO_URI` | Your MongoDB Atlas connection string |
| `SECRET_KEY` | A secure random string (e.g., generate with `python -c "import secrets; print(secrets.token_hex(32))"`) |
| `FLASK_ENV` | `production` |

**Example MONGO_URI:**
```
mongodb+srv://svljyothikanookala_db_user:Health_user@cluster0.kricsn.mongodb.net/healthcare_db?retryWrites=true&w=majority&appName=Cluster0
```

4. Click **Save** after each variable

### 6. Redeploy with Environment Variables

After setting environment variables:

1. Go to **Deployments** tab
2. Click the three dots (...) on the latest deployment
3. Click **Redeploy**
4. Click **Redeploy** again to confirm

## Troubleshooting

### Issue: "Database not available" error

**Solutions:**
1. Verify MongoDB Atlas IP whitelist includes `0.0.0.0/0` (Allow All)
2. Verify `MONGO_URI` environment variable is set correctly
3. Check MongoDB connection string format:
   - Must include: `mongodb+srv://`
   - Must include database name at the end
   - Must include credentials
4. Test connection by viewing Vercel logs:
   - Go to **Deployments** → Click deployment → **Logs**

### Issue: "Module not found" error

**Solution:**
Ensure all dependencies are in `requirements.txt`:
```bash
pip freeze > requirements.txt
```

Then redeploy.

### Issue: Static files not loading

**Solution:**
Static files are in the `static/` directory. Vercel automatically serves them. If issues persist:

1. Verify `static/` folder exists in root directory
2. Ensure Flask is serving static files correctly
3. Check paths in HTML templates use `{{ url_for('static', ...) }}`

### Issue: Timeouts or slow responses

**Solutions:**
1. Increase function timeout in `vercel.json`:
   ```json
   "functions": {
     "api/index.py": {
       "maxDuration": 60
     }
   }
   ```
2. Optimize MongoDB queries
3. Add caching for static content

## Production Checklist

- [ ] Set `FLASK_ENV` to `production`
- [ ] Update `SECRET_KEY` to a secure random value
- [ ] Configure MongoDB Atlas IP whitelist
- [ ] Test all forms and authentication flows
- [ ] Enable HTTPS (Vercel does this automatically)
- [ ] Monitor error logs in Vercel dashboard
- [ ] Test predictions and data analysis features
- [ ] Verify email notifications work (if applicable)
- [ ] Set up custom domain (optional)
- [ ] Enable automatic deployments from GitHub

## Custom Domain (Optional)

1. Purchase domain from provider (GoDaddy, Namecheap, etc.)
2. In Vercel dashboard: **Settings** → **Domains**
3. Add your domain
4. Follow DNS configuration instructions
5. Wait for DNS propagation (up to 48 hours)

## Updating Your App

After deployment, any changes you push to your GitHub repository will automatically redeploy:

1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```
3. Vercel automatically detects and deploys changes (watch the **Deployments** tab)

## Monitoring and Logs

1. Go to **Deployments** in your Vercel project
2. Click on a deployment to see:
   - Build logs
   - Runtime logs
   - Error messages
   - Performance metrics

## Important Notes

- **Cold starts**: First request may be slower (typical for serverless)
- **Session storage**: Use MongoDB for persistent session storage (recommended for production)
- **File uploads**: Use cloud storage (not recommended for Vercel's ephemeral filesystem)
- **Scheduled tasks**: Consider using external services (e.g., MongoDB Atlas Triggers)

---

**Need Help?**
- Vercel Docs: https://vercel.com/docs
- Flask on Vercel: https://vercel.com/guides/deploying-flask-with-vercel
- MongoDB Atlas Help: https://docs.mongodb.com/
