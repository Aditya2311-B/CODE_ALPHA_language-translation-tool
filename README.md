# Language Translation Tool

A modern, production-ready multilingual translation application built with Python and Streamlit. Translate text between 50+ languages instantly with auto-detection, text-to-speech capabilities, and a beautiful glassmorphism UI.
WEBSITE LINK : https://codealphalanguage-translation-tool-bwfrs62ghaszrejz72fywb.streamlit.app/
<img width="2070" height="1606" alt="image" src="https://github.com/user-attachments/assets/e6393865-0796-4b19-bfe5-e4925fa06e58" />

## Features

- **Multi-language Translation**: Support for 50+ languages including English, Spanish, French, German, Chinese, Japanese, Hindi, and many more
- **Auto Language Detection**: Automatically detects the source language when "Auto Detect" is selected
- **Text-to-Speech**: Convert translated text to audio and download as MP3
- **Download Translations**: Save translated text as a .txt file
- **Translation History**: View and manage your recent translations (last 5)
- **Real-time Metrics**: Character and word count for input text
- **Language Swap**: Quickly swap source and target languages with one click
- **Modern UI**: Beautiful glassmorphism design with dark theme inspired by Gemini
- **Responsive Design**: Optimized for various screen sizes
<img width="808" height="1544" alt="image" src="https://github.com/user-attachments/assets/cc9fbdc6-b5fb-44af-89d1-3a356d72521a" />

## Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit 1.28+**: Web application framework
- **Deep Translator 1.11+**: Translation engine (Google Translate API)
- **gTTS 2.4+**: Google Text-to-Speech for audio generation
- **LangDetect 1.0.9**: Language detection library

## Installation Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Local Setup

1. **Clone or download the project**
   ```bash
   cd /path/to/CODE_ALPHA_TASK1
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run Locally

1. **Activate your virtual environment** (if you created one)

2. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser**
   The application will automatically open at `http://localhost:8501`

## Deployment on Streamlit Cloud

This application is fully compatible with Streamlit Cloud deployment:

### Prerequisites

- A GitHub account with the project pushed to a repository
- A Streamlit Cloud account (free tier available)

### Deployment Steps

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select the repository and branch
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Your app will be live** at a URL like `https://your-app-name.streamlit.app`

### Deployment Notes

- The application uses temporary files for audio generation, ensuring compatibility with Streamlit Cloud's read-only filesystem
- All dependencies are specified in `requirements.txt`
- No additional environment variables or API keys are required

## Project Structure

```
CODE_ALPHA_TASK1/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Future Enhancements

Potential improvements for future versions:

- **Batch Translation**: Upload and translate multiple files at once
- **Document Translation**: Support for PDF, DOCX, and other document formats
- **API Integration**: Add support for other translation services (DeepL, Microsoft Translator)
- **User Authentication**: Save translation history across sessions
- **Offline Mode**: Cache translations for offline access
- **Mobile App**: React Native or Flutter mobile application
- **Collaborative Features**: Share translations with other users
- **Translation Quality Score**: Display confidence scores for translations
- **Custom Language Pairs**: Save frequently used language combinations
- **Voice Input**: Add speech-to-text for input
- **Translation Memory**: Learn from user corrections

## Troubleshooting

### Common Issues

**Issue**: "ModuleNotFoundError" when running the app
- **Solution**: Ensure you've installed all dependencies: `pip install -r requirements.txt`

**Issue**: Audio download not working
- **Solution**: Check your internet connection (gTTS requires internet access)

**Issue**: Language detection inaccurate for short text
- **Note**: This is a known limitation of the langdetect library. Detection improves with longer text (3+ words recommended)

## License

This project is open source and available for educational and personal use.

## Credits

Built by Aditya Batri using Python, Streamlit, and Deep Translator.

## Support

For issues or questions, please open an issue on the GitHub repository.
