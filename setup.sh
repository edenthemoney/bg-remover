#!/bin/bash

# Background Remover - Quick Setup Script
# This script helps you set up your background remover for deployment

echo "🚀 Background Remover - Setup Script"
echo "===================================="
echo ""

# Check if domain is provided
if [ -z "$1" ]; then
    echo "Usage: ./setup.sh yourdomain.com [publisher-id]"
    echo ""
    echo "Example:"
    echo "  ./setup.sh bgremover.com ca-pub-1234567890123456"
    echo ""
    exit 1
fi

DOMAIN=$1
PUBLISHER_ID=${2:-"ca-pub-xxxxxxxxxxxxxxxx"}

echo "📝 Configuration:"
echo "  Domain: $DOMAIN"
echo "  Publisher ID: $PUBLISHER_ID"
echo ""

# Update domain in all HTML files
echo "🔄 Updating domain in HTML files..."
find . -type f -name "*.html" -exec sed -i '' "s/yourdomain\.com/$DOMAIN/g" {} +
find . -type f -name "*.xml" -exec sed -i '' "s/yourdomain\.com/$DOMAIN/g" {} +

# Update publisher ID in all HTML files
echo "🔄 Updating Google AdMob Publisher ID..."
find . -type f -name "*.html" -exec sed -i '' "s/ca-pub-xxxxxxxxxxxxxxxx/$PUBLISHER_ID/g" {} +

echo ""
echo "✅ Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Push to GitHub: git add . && git commit -m 'Setup for deployment' && git push"
echo "2. Deploy to Railway/Render/Vercel (see QUICK_START.md)"
echo "3. Connect your Porkbun domain"
echo "4. Submit to Google Search Console"
echo "5. Start promoting on Reddit, Twitter, ProductHunt"
echo ""
echo "For detailed instructions, see QUICK_START.md"
