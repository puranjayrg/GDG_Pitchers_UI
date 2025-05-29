This repository contains the resources and code for a talk I was invited to give at **Data & GenAI Nexus 5.0** hosted by Google Developer Groups (GDG) Noida. 

You can access the UI by running the code locally on your system using the instructions below, or you can play around with an already hosted version on streamlit cloud here: [GDG Pitchers](https://gdgpitchers.streamlit.app/)

Please keep in mind that the UI has been optimized for dark mode and may not be rendered perfectly in case you are using light mode. 

Please feel free to star the repository if you found it useful :)

---

# 💼 GDG Pitchers

Transform any business idea into a compelling, professional pitch in seconds using the power of AI!

## 🌟 What is GDG Pitchers?

GDG Pitchers is an AI-powered business pitch generator that takes your raw business ideas (even the silly ones!) and transforms them into structured, investor-ready presentations. Whether you're brainstorming for a hackathon, preparing for a startup competition, or just having fun with creative ideas, GDG Pitchers has you covered.

## ✨ Features

- **🤖 AI-Powered Analysis**: Uses Llama 3.3 via Groq API for intelligent business analysis
- **🎨 Logo Generation**: Creates custom logos using Google's Gemini AI (with fallback to generated logos)
- **📊 Viability Scoring**: Get realistic assessments of your business idea's potential
- **🎯 Complete Pitch Deck**: Generates business name, tagline, elevator pitch, target market, features, and more
- **🌙 Dark Mode Optimized**: Beautiful, modern UI designed for extended use
- **⚡ Lightning Fast**: Generate complete pitches in under 30 seconds

## 🚀 Getting Started

### Option 1: Use the Deployed App (Recommended)

1. Visit the deployed Streamlit app (link will be provided after deployment)
2. Get your free API keys:
   - **Groq API Key** (required): [Get it here](https://console.groq.com/)
   - **Gemini API Key** (optional): [Get it here](https://aistudio.google.com/)
3. Enter your API keys in the sidebar
4. Start generating pitches!

### Option 2: Run Locally

#### Prerequisites

- Python 3.8 or higher
- pip package manager

#### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd GDG_Pitchers_UI
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit groq google-genai pillow
   ```

3. **Set up API keys** (Optional for local development)
   
   Create a `.streamlit/secrets.toml` file:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   GEMINI_API_KEY = "your_gemini_api_key_here"
   ```

4. **Run the application**
   ```bash
   streamlit run pitch_perfecter.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 🎯 How to Use

### Step 1: Enter Your Business Idea
- Type any business concept in the input field
- Don't worry about being formal - even silly ideas work great!
- Examples: "Dating app for pets" or "Subscription service for left socks only"

### Step 2: Add Context (Optional)
- Provide additional details about your target market
- Mention special features or constraints
- Add any specific requirements

### Step 3: Generate Your Pitch
- Click the "✨ Generate Pitch!" button
- Wait for the AI to analyze your idea
- Get a complete business pitch with:
  - Creative business name and tagline
  - Professional logo
  - Elevator pitch
  - Target market analysis
  - Key features breakdown
  - Marketing strategy
  - Viability score (1-10)
  - Fun facts and projected valuation

### Step 4: Iterate and Improve
- Use the "♻️ Generate Another Pitch" button to try different approaches
- Experiment with the example ideas in the sidebar
- Try different AI models for varied results

## 🔧 Configuration Options

### AI Models Available
- **Llama 3.3 70B Versatile** (Default) - Most capable, best results
- **Llama 3.3 8B Versatile** - Faster responses, good quality
- **Llama 4 Maverick 17B** - Experimental, creative outputs

### API Keys
- **Groq API Key**: Required for pitch generation
  - Free tier available with generous limits
  - Sign up at [console.groq.com](https://console.groq.com/)
- **Gemini API Key**: Optional for AI-generated logos
  - Falls back to simple generated logos if not provided
  - Get yours at [aistudio.google.com](https://aistudio.google.com/)

## 📝 Example Ideas to Try

Get inspired with these sample business concepts:

- "Dating app that matches people based on their refrigerator contents"
- "Smart umbrella that predicts when it will rain"
- "Service that translates what your pet is thinking"
- "Restaurant where robots cook while performing stand-up comedy"
- "A retail store selling only pencil sharpeners"

## 🛠️ Technical Details

### Built With
- **Streamlit**: Web application framework
- **Groq API**: LLM inference for business analysis
- **Google Gemini**: AI image generation for logos
- **PIL (Pillow)**: Image processing and fallback logo generation
- **Custom CSS**: Dark mode optimized styling

### File Structure
```
GDG_Pitchers_UI/
├── pitch_perfecter.py    # Main application file
├── .streamlit/
│   └── secrets.toml            # API keys (local only)
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

## 🔒 Privacy & Security

- API keys are handled securely and never logged
- No business ideas are stored or transmitted beyond the AI APIs
- All processing happens in real-time
- Local deployment option available for sensitive ideas

## 🐛 Troubleshooting

### Common Issues

**"Groq API key not found"**
- Ensure you've entered your API key in the sidebar
- Check that your API key is valid and active

**"JSON parsing error"**
- This is usually temporary - try generating again
- The app has fallback mechanisms to handle parsing issues

**"Error generating logo"**
- Gemini API might be temporarily unavailable
- The app will automatically use a generated logo instead

**Slow performance**
- Try switching to the 8B model for faster responses
- Check your internet connection

### Getting Help

If you encounter issues:
1. Check the sidebar for API key status indicators
2. Try refreshing the page
3. Verify your API keys are correctly entered
4. Switch to a different AI model

## 🤝 Contributing

This project was created for the Google Developer Groups (GDG) community. Feel free to:
- Report bugs or issues
- Suggest new features
- Submit improvements
- Share your generated pitches!

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Credits

Created with ❤️ for the GDG community using:
- Groq's lightning-fast LLM inference
- Google's Gemini AI for creative logo generation
- Streamlit's amazing web app framework

---

**Ready to turn your wildest business ideas into professional pitches? Let's get started! 🚀**