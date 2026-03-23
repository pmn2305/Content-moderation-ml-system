# Content Moderation ML 🛡️

AI-powered content moderation system with real-time text and image analysis.

## 🏗️ Architecture

- **Frontend**: React 19 + Vite + TailwindCSS (Vercel)
- **Backend**: FastAPI + Python ML Models (Railway)
- **Cache**: Redis (Railway)
- **Models**: Text Toxicity & Image Moderation

## 📦 Features

✅ Real-time text toxicity detection  
✅ Image policy violation detection  
✅ Enterprise-grade accuracy  
✅ Caching with Redis  
✅ Dark theme UI  
✅ Responsive design  

## 🛠️ Tech Stack

- **React 19.2.0** - Frontend framework
- **FastAPI** - Python backend
- **Redis** - Caching
- **TailwindCSS** - Styling
- **Docker** - Containerization

## 📊 Results

The system returns:
- `decision`: "allow" or "reject"
- `scores.text`: Toxicity level (0-1)
- `scores.image`: Violation risk (0-1)

## 🔗 Endpoints

```
POST /moderate
Content-Type: multipart/form-data

Body:
- text: string (required)
- image: file (optional)

Response:
{
  "decision": "allow|reject",
  "scores": {
    "text": 0.1234,
    "image": 0.5678
  }
}
```

## 🚀 Deploy Your Own

### Frontend (Vercel)
1. Fork repo on GitHub
2. Go to Vercel.com → Import project
3. Set root directory: `ui/moderation-ui`

### Backend (Railway)
1. Go to Railway.app → New project
2. Deploy from GitHub
3. Add Redis service
4. Set `REDIS_URL` environment variable

## 📝 License

MIT
