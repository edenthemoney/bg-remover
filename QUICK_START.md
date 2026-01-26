# 🚀 Quick Start - Get Online in 30 Minutes

## Step 1: Update Your Domain (2 minutes)

Replace `freephototools.xyz` with your actual domain everywhere:

```bash
# From the project root, run:
find . -type f \( -name "*.html" -o -name "*.xml" \) -exec sed -i '' 's/yourdomain\.com/YOUR_ACTUAL_DOMAIN.com/g' {} +

# Example:
find . -type f \( -name "*.html" -o -name "*.xml" \) -exec sed -i '' 's/yourdomain\.com/bgremover.com/g' {} +
```

## Step 2: Add Your Ad Codes (5 minutes)

### Get Google AdMob Publisher ID:
1. Go to admob.google.com
2. Sign in with Google
3. Add your website
4. Copy your Publisher ID (looks like: ca-pub-1234567890123456)

### Replace in all files:
```bash
find . -type f -name "*.html" -exec sed -i '' 's/ca-pub-xxxxxxxxxxxxxxxx/YOUR_PUBLISHER_ID/g' {} +
```

## Step 3: Choose Your Hosting & Deploy

### Option A: Railway (Easiest - Recommended)
```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login to Railway
railway login

# 3. Create new project
railway init

# 4. Deploy
railway up

# 5. Go to railway.app dashboard
# - Find your project
# - Go to Settings → Domains
# - Add your Porkbun domain
```

### Option B: Render (Also Easy)
```bash
# 1. Go to render.com
# 2. Click "New +" → "Web Service"
# 3. Connect GitHub (push your code first)
# 4. Set build command: pip install -r requirements.txt
# 5. Set start command: gunicorn app:app
# 6. Deploy
# 7. Add custom domain in dashboard
```

### Option C: Vercel
```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Deploy
vercel

# 3. Follow prompts
# 4. Add domain in dashboard
```

## Step 4: Connect Your Porkbun Domain (5 minutes)

1. Log into Porkbun.com
2. Go to "Domain Management"
3. Click your domain
4. Find "DNS Settings" or "Nameservers"
5. Replace with your hosting provider's nameservers:

**Railway:**
- ns1.railway.app
- ns2.railway.app
- ns3.railway.app
- ns4.railway.app

**Render:**
- ns1.render.com
- ns2.render.com
- ns3.render.com
- ns4.render.com

**Vercel:**
- ns1.vercel.com
- ns2.vercel.com
- ns3.vercel.com
- ns4.vercel.com

6. Save and wait 24-48 hours for DNS propagation

## Step 5: Verify It's Working

1. Wait 5-10 minutes for deployment
2. Visit your domain: https://freephototools.xyz
3. Test upload functionality
4. Check that ads are loading

## Step 6: Submit to Google (Important for SEO!)

1. Go to search.google.com/search-console
2. Click "Add property"
3. Enter your domain
4. Verify ownership (choose DNS method)
5. Add DNS record from Porkbun
6. Submit sitemap: freephototools.xyz/sitemap.xml
7. Submit robots.txt: freephototools.xyz/robots.txt

## Step 7: Start Getting Traffic

### Immediate (Today):
- [ ] Post on Reddit (r/design, r/photography, r/ecommerce)
- [ ] Share on Twitter/X
- [ ] Share on LinkedIn

### This Week:
- [ ] Submit to ProductHunt
- [ ] Submit to Alternativeto.net
- [ ] Create YouTube tutorial
- [ ] Submit to tool directories

### This Month:
- [ ] Write blog posts
- [ ] Guest posts on design blogs
- [ ] Build backlinks
- [ ] Monitor Google Search Console

---

## Troubleshooting

### Domain not working?
- Wait 24-48 hours for DNS propagation
- Check nameservers are correct in Porkbun
- Clear browser cache (Ctrl+Shift+Delete)
- Try incognito window

### Ads not showing?
- Check Publisher ID is correct
- Wait 24 hours for Google to approve ads
- Check browser console for errors (F12)
- Ensure you're not blocking ads

### Upload not working?
- Check server logs in hosting dashboard
- Verify rembg is installed: `pip list | grep rembg`
- Check file permissions on uploads folder
- Try smaller file size

### Slow performance?
- Check server specs (upgrade if needed)
- Enable caching in hosting dashboard
- Compress images
- Minimize CSS/JS

---

## Next Steps for Revenue

1. **Monitor Analytics:** Set up Google Analytics to track traffic
2. **Optimize Ads:** Test different ad placements and sizes
3. **Add More Tools:** Create more niche pages (LinkedIn optimizer, etc.)
4. **Build Email List:** Add newsletter signup
5. **Create Content:** Write blog posts targeting keywords
6. **Build Backlinks:** Guest posts, directory submissions, partnerships

---

## Expected Timeline

- **Day 1:** Site goes live
- **Week 1:** First organic visitors
- **Month 1:** 100-500 daily visitors, $10-50/month
- **Month 3:** 500-2,000 daily visitors, $150-500/month
- **Month 6:** 2,000-10,000 daily visitors, $500-2,500/month

**Your goal: 10,000+ daily users = $3,000-10,000/month in passive income!**
