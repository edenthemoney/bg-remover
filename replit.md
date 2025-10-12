# Free Background Remover - AI Photo Background Eraser

## Overview
A Flask-based web application that uses AI to automatically remove backgrounds from photos. The app provides a free alternative to paid services like Canva, with no signup required and no watermarks.

## Recent Changes (October 12, 2025)
- Imported project from GitHub and configured for Replit environment
- Installed Python 3.11 and all required dependencies (Flask, rembg, Pillow, gunicorn)
- Created missing template files (about.html, sitemap.xml)
- Updated app.py to run on port 5000 with host 0.0.0.0
- Configured workflow to run Flask app with gunicorn on port 5000
- Set up deployment configuration for autoscale deployment
- **Updated from GitHub with new features:**
  - Added Image Resizer tool with preset and custom dimensions
  - Added Bulk Background Remover for processing multiple images
  - Implemented ZIP download for bulk processed images
  - Added navigation menu across all pages
  - Enhanced monetization with additional ad placements
  - Created resize.html and bulk.html templates

## Project Architecture

### Tech Stack
- **Backend**: Flask 3.0.0 (Python web framework)
- **AI Processing**: rembg 2.0.50 (AI background removal library)
- **Image Processing**: Pillow 10.1.0
- **Web Server**: gunicorn 21.2.0
- **Python Version**: 3.11

### Project Structure
```
.
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html        # Main page with upload interface
│   ├── about.html        # About page
│   └── sitemap.xml       # SEO sitemap
├── uploads/              # Temporary storage for processed images
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── replit.md            # This documentation
```

### Key Features
- **Background Removal**: AI-powered background removal using rembg library
- **Image Resizer**: Resize images with preset dimensions (Instagram, Facebook, HD, etc.) or custom sizes
- **Bulk Processor**: Process multiple images at once and download as ZIP
- Drag-and-drop file upload interface
- Real-time image processing with preview
- Automatic cleanup of files older than 1 hour
- Responsive design with dark luxury theme
- Navigation menu for easy access to all tools
- SEO optimized with meta tags and sitemap
- Enhanced Google AdSense integration with multiple ad placements

### Routes
- `GET /` - Main background remover page
- `GET /resize` - Image resizer tool page
- `GET /bulk` - Bulk background remover page
- `GET /about` - About page
- `GET /sitemap.xml` - XML sitemap for SEO
- `POST /remove-background` - API endpoint for background removal
- `POST /resize-image` - API endpoint for image resizing
- `POST /bulk-remove` - API endpoint for bulk background removal
- `GET /download/<job_id>` - Download processed image
- `GET /download-zip/<job_id>` - Download bulk processed images as ZIP
- `GET /preview/<job_id>` - Preview processed image

## Running the Application

### Development
The application runs automatically via the configured workflow using gunicorn:
```bash
gunicorn app:app --bind 0.0.0.0:5000 --timeout 120 --workers 1
```

The application is accessible on port 5000.

### Deployment
Configured for autoscale deployment using gunicorn. The deployment will automatically scale based on traffic.

## Configuration

### Environment Variables
No environment variables required for basic functionality.

### Port Configuration
- Frontend/Backend: Port 5000 (single Flask application)
- Host: 0.0.0.0 (accepts all connections)

### File Cleanup
- Processed images are automatically deleted after 1 hour
- Cleanup runs automatically when new files are processed

## Security & Privacy
- Images are stored temporarily in the `uploads/` directory
- Automatic deletion after 1 hour ensures user privacy
- No permanent storage of user images

## SEO & Monetization
- Comprehensive meta tags for search engine optimization
- Structured data and sitemap for better indexing
- Google AdSense integration with multiple ad placements
- Keywords targeting: "remove background", "background remover", "free background eraser"

## User Preferences
None configured yet.

## Notes
- The application uses synchronous processing for image uploads
- Single worker configuration is used to manage resource usage
- The AI model (rembg) is downloaded automatically on first use
- AdSense errors in browser console are normal and don't affect functionality
