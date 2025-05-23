import streamlit as st
import groq
import os
import time
# import random
# import requests
from PIL import Image, ImageDraw, ImageFont  # Import all PIL modules at once
from io import BytesIO
import json

# Import necessary libraries for Gemini
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# # Page setup
st.set_page_config(
    page_title="GDG Pitchers",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Optional: reset theme to default in `.streamlit/config.toml`


# Dark mode optimized styling
st.markdown("""
<style>
    /* Enhanced typography with consistent colors */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Roboto+Slab:wght@400;500;600&display=swap');
    
    /* Base heading styles */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
    }
    
    h1 {
        color: #BB86FC !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px !important;
    }
    
    h2 {
        color: #03DAC6 !important;
        font-size: 2rem !important;
        font-weight: 600 !important;
    }
    
    h3 {
        color: #CF6679 !important;
        font-size: 1.5rem !important;
        font-weight: 500 !important;
    }
    
    /* Section titles with consistent styling */
    .section-title {
        font-family: 'Poppins', sans-serif !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        color: #BB86FC !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.5rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Content cards with better focus */
    .content-card {
        background-color: rgba(30, 30, 30, 0.7) !important;
        border-left: 4px solid #03DAC6 !important;
        border-radius: 4px !important;
        padding: 15px !important;
        margin-bottom: 15px !important;
        transition: all 0.3s ease !important;
    }
    
    .content-card:hover {
        background-color: rgba(40, 40, 40, 0.8) !important;
        transform: translateX(3px) !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important;
    }
    
    /* Specific card types with different accent colors */
    .elevator-card {
        border-left-color: #BB86FC !important;
    }
    
    .target-card {
        border-left-color: #03DAC6 !important;
    }
    
    .features-card {
        border-left-color: #CF6679 !important;
    }
    
    .marketing-card {
        border-left-color: #FFAB40 !important;
    }
    
    .funfact-card {
        border-left-color: #69F0AE !important;
    }
    
    .valuation-card {
        border-left-color: #FF9E80 !important;
        background-color: rgba(40, 30, 30, 0.7) !important;
    }
    
    /* Consistent text styling */
    .elevator-pitch {
        font-family: 'Roboto Slab', serif !important;
        font-size: 1.2rem !important;
        font-style: italic !important;
        line-height: 1.6 !important;
        color: #e0e0e0 !important;
    }
    
    .content-text {
        font-family: 'Roboto', sans-serif !important;
        font-size: 1.1rem !important;
        line-height: 1.5 !important;
        color: #e0e0e0 !important;
    }
    
    /* Business name and tagline */
    .business-name {
        font-family: 'Poppins', sans-serif !important;
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #BB86FC !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 0 10px rgba(187, 134, 252, 0.3) !important;
    }
    
    .tagline {
        font-family: 'Roboto Slab', serif !important;
        font-size: 1.5rem !important;
        font-style: italic !important;
        color: #03DAC6 !important;
        margin-bottom: 2rem !important;
    }
    
    /* Valuation styling */
    .valuation {
        font-family: 'Poppins', sans-serif !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #FF9E80 !important;
        text-align: center !important;
    }
    
    .valuation-label {
        font-family: 'Roboto', sans-serif !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #BB86FC !important;
        text-align: center !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
    }
    
    /* Score and progress bar container */
    .score-container {
        display: flex !important;
        align-items: center !important;
        gap: 20px !important;
        margin-bottom: 20px !important;
        width: 100% !important;
    }

    /* Score value styling */
    .score-value {
        font-family: 'Poppins', sans-serif !important;
        font-size: 2.0rem !important;
        font-weight: 700 !important;
        color: #03DAC6 !important;
        /* text-align: center !important; */
        text-shadow: 0 0 10px rgba(3, 218, 198, 0.3) !important;
        background: rgba(3, 218, 198, 0.1) !important;
        border-radius: 50% !important;
            
        aspect-ratio: 1 / 1 !important; /* Force 1:1 aspect ratio */
        width: 100px !important; /* Fixed width */
        min-width: 80px !important; /* Prevent shrinking */
    
        /* width: 100px !important;
        height: 100px !important; */
        
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border: 2px solid #03DAC6 !important;
        margin: 0 auto !important;
            
        box-sizing: border-box !important;
        flex-shrink: 0 !important; /* Prevent shrinking */
    }

    /* Progress bar styling */
    .stProgress > div {
        height: 15px !important;
    }

    .stProgress > div > div{
        background-color: #03DAC6 !important; /* Background color */
        border-radius: 10px !important;
    }

    .stProgress > div > div > div > div{
        /* background-color: rgba(3, 218, 198, 0.2) !important;  Filled part color */
        background-image: linear-gradient(to right, #99ff99 , #00ccff);
        border-radius: 10px !important;
    }

    .progress-label {
        font-family: 'Roboto', sans-serif !important;
        font-size: 0.9rem !important;
        color: #e0e0e0 !important;
        margin-bottom: 5px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "idea_input" not in st.session_state:
    st.session_state.idea_input = ""
if "additional_context" not in st.session_state:
    st.session_state.additional_context = ""
# if "debug_mode" not in st.session_state:
#     st.session_state.debug_mode = False
# if "debug_info" not in st.session_state:
#     st.session_state.debug_info = {}

# App header
st.title("💼 GDG Pitchers")
st.subheader("Turn any idea into a compelling business pitch in seconds!")

# Initialize API keys from secrets or environment variables
try:
    groq_api_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))
except:
    groq_api_key = os.environ.get("GROQ_API_KEY", "")

try:
    gemini_api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
except:
    gemini_api_key = os.environ.get("GEMINI_API_KEY", "")

# Sidebar for API key and example ideas
with st.sidebar:
    st.header("Configuration")

    # Show API key inputs prominently if no keys are available
    if not groq_api_key or not gemini_api_key:
        st.warning("⚠️ API keys required for full functionality")
        
    # Always show API key inputs (not in expander) when keys are missing
    if not groq_api_key or not gemini_api_key:
        st.subheader("API Keys Required")
        groq_api_key = st.text_input("Groq API key (required for pitch generation)", 
                                    type="password", 
                                    value=groq_api_key,
                                    help="Get your free API key from https://console.groq.com/")

        gemini_api_key = st.text_input("Gemini API key (optional - for AI-generated logos)", 
                                      type="password", 
                                      value=gemini_api_key,
                                      help="Get your API key from https://aistudio.google.com/")
    else:
        # Use expander when keys are available (for local development)
        with st.expander("API Keys (Optional - defaults provided)"):
            groq_api_key = st.text_input("Groq API key (optional)", 
                                        type="password", 
                                        value=groq_api_key,
                                        help="Default key provided, but you can use your own")

            gemini_api_key = st.text_input("Gemini API key (optional)", 
                                          type="password", 
                                          value=gemini_api_key,
                                          help="Default key provided, but you can use your own")
    
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
    
    if gemini_api_key:
        os.environ["GEMINI_API_KEY"] = gemini_api_key

    # Add API key status indicators
    if groq_api_key:
        st.success("✅ Groq API key configured")
    else:
        st.error("❌ Groq API key missing")
        
    if gemini_api_key:
        st.success("✅ Gemini API key configured")
    else:
        st.info("ℹ️ Gemini API key missing (will use simple logos)")

    model_option = st.selectbox(
        "Select Model",
        ["llama-3.3-70b-versatile", "llama-3.3-8b-versatile", "meta-llama/llama-4-maverick-17b-128e-instruct"],
        index=0,
        help="Llama 3.3 70B is most capable, Llama 3.3 8B is faster, Mixtral is a good balance"
    )

    # Debug mode toggle
    # st.session_state.debug_mode = st.checkbox("Debug Mode", value=st.session_state.debug_mode)
    
    st.markdown("### How to use")
    st.markdown("""
    1. Enter your business idea in the input field
    2. Add any additional context (optional)
    3. Click "Generate Pitch!" to create your business pitch
    4. Get a complete pitch with name, tagline, logo, and analysis
    """)
    
    st.markdown("### Example Business Ideas")
    example_ideas = [
        "Dating app that matches people based on their refrigerator contents",
        "Smart umbrella that predicts when it will rain",
        "Service that translates what your pet is thinking",
        "Restaurant where robots cook while performing stand-up comedy",
        "A retail store selling only pencil sharpeners",
    ]
    
    for idea in example_ideas:
        if st.button(idea):
            st.session_state.idea_input = idea
            st.session_state.additional_context = ""
            # Clear any existing pitch data when selecting a new example
            if 'pitch_data' in st.session_state:
                del st.session_state.pitch_data
            st.rerun()

# Initialize Groq client
def get_groq_client():
    if not groq_api_key:
        st.error("Groq API key not found. Please enter it in the sidebar.")
        st.stop()
    return groq.Client(api_key=groq_api_key)

# Helper function for generating logos using Gemini
def generate_logo(business_name, business_concept, tagline=""):
    """Generate a logo using Google's Gemini API or fallback to a simple generated logo"""
    try:
        # Check if API key is available
        gemini_api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
        
        if not gemini_api_key:
            st.warning("Gemini API key not found. Using generated logo instead.")
            return create_simple_logo(business_name)
        
        # Initialize Gemini client
        client = genai.Client(api_key=gemini_api_key)

        # Create a prompt for the logo generation
        contents = (
            f"Create a simple, professional, modern business logo for '{business_name}' - {tagline}. "
            f"The business concept: {business_concept}. "
            "The logo should have a clean design, "
            "professional aesthetics, and visual elements that represent the business concept. "
            "Make it minimal and suitable for a business card or website."
        )

        # Generate the image
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
                
            # Process the response
            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    # Convert the image data to a PIL Image
                    image = Image.open(BytesIO(part.inline_data.data))
                    return image

            # If no image was found in the response
            st.warning("No image was generated by Gemini. Using generated logo instead.")
            return create_simple_logo(business_name)
            
        except Exception as e:
            st.warning(f"Error in Gemini API call: {e}")
            return create_simple_logo(business_name)
        
    except Exception as e:
        st.warning(f"Error generating logo with Gemini: {e}")
        return create_simple_logo(business_name)



# Simple logo generator that doesn't rely on external services
def create_simple_logo(business_name):
    """Create a simple colored logo with text"""
    try:
        # Create a blank image with a solid background
        width, height = 300, 200
        
        # Generate a color based on the business name
        # This ensures the same business always gets the same color
        first_char = business_name[0].lower() if business_name else 'a'
        hue = (ord(first_char) * 37) % 360  # 0-359
        
        # Convert HSL to RGB
        import colorsys
        h = hue / 360.0
        s = 0.7  # Saturation
        l = 0.5  # Lightness
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        
        # Convert to 0-255 range
        bg_color = (int(r * 255), int(g * 255), int(b * 255))
        
        # Create the image
        img = Image.new('RGB', (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Get initials from business name
        initials = "".join([word[0].upper() for word in business_name.split() if word])
        if not initials:
            initials = "BP"  # Default
        initials = initials[:2]  # Limit to 2 characters
        
        # Draw a white circle in the center
        circle_radius = min(width, height) // 4
        circle_center = (width // 2, height // 2)
        circle_bbox = (
            circle_center[0] - circle_radius,
            circle_center[1] - circle_radius,
            circle_center[0] + circle_radius,
            circle_center[1] + circle_radius
        )
        draw.ellipse(circle_bbox, fill=(255, 255, 255))
        
        # Draw the initials in the center
        # Use default font since custom fonts might not be available
        font = ImageFont.load_default()
        
        # Calculate text position
        text_width = font.getlength(initials) if hasattr(font, 'getlength') else len(initials) * 7
        text_x = width // 2 - text_width // 2
        text_y = height // 2 - 7  # Approximate font height
        
        # Draw text
        draw.text((text_x, text_y), initials, fill=bg_color)
        
        return img
        
    except Exception as e:
        st.warning(f"Error creating simple logo: {e}")
        # Last resort - create a solid color image
        return Image.new('RGB', (300, 200), color=(41, 128, 185))  # Blue

# Function to analyze business idea
def analyze_business_idea(idea, additional_context="", model_name="llama-3.3-70b-versatile"):
    system_message = """You are PitchBot, an expert business consultant with a sense of humor and a knack for creative naming. Your job is to transform business ideas into compelling, structured pitches.

CRITICAL INSTRUCTIONS:
1. You MUST respond with ONLY valid JSON - no markdown, no explanations, no extra text
2. Follow the exact JSON structure provided below
3. Be creative, concise, and add humor where appropriate
4. All string values must be properly escaped for JSON
5. Do not use line breaks within string values

RESPONSE FORMAT (copy this structure exactly):
{
    "business_name": "Creative, memorable name (2-4 words max)",
    "tagline": "Catchy slogan (5-8 words max)",
    "elevator_pitch": "Compelling 1-2 sentence summary that hooks investors",
    "target_market": "Specific demographic with size estimate",
    "key_features": [
        "Feature 1: Brief description",
        "Feature 2: Brief description",
        "Feature 3: Brief description",
        "Feature 4: Brief description"
    ],
    "marketing_strategy": "Primary marketing approach in 1-2 sentences",
    "viability_score": 8,
    "viability_reasoning": "Brief explanation of why this score (1-2 sentences)",
    "fun_fact": "Interesting/amusing fact related to this business domain",
    "projected_valuation": "Humorous but semi-realistic valuation estimate - don't always go for a billion/million, be more creative! Keep it short and sweet - MAX 15 words!)"
}

GUIDELINES:
- Business names should be brandable and memorable
- Taglines should be punchy and memorable
- Viability scores: Should be realistic - Do NOT bias towards pleasing the user! Assess actual viability. 1-3 (poor), 4-6 (moderate), 7-8 (good), 9-10 (excellent)
- Fun facts should be genuinely interesting or amusing
- Valuations can be playful but not completely absurd - should align with viability scores!
- Keep all text concise and engaging
- Add personality and humor where appropriate

Remember: Respond with ONLY the JSON object, nothing else."""
    
    user_message = f"""Analyze this business idea and create a structured pitch:

BUSINESS IDEA: {idea}"""

    if additional_context:
        user_message += f"\n\nADDITIONAL CONTEXT: {additional_context}"

    user_message += "\n\nGenerate a complete business pitch following the JSON structure specified in your system instructions. Make it creative, engaging, and add some personality to it."
    
    try:
        # Get Groq client
        client = get_groq_client()
        
        # Call the Groq API without json_mode
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            max_tokens=1024,
            temperature=0.7
        )
        
        # Extract the content from the response structure
        content = response.choices[0].message.content
        
        # Parse JSON response
        try:
            result = json.loads(content)
            
            # Handle field name differences if needed
            if "score_reasoning" in result and "viability_reasoning" not in result:
                result["viability_reasoning"] = result["score_reasoning"]
                
        except json.JSONDecodeError as e:
            # If JSON parsing fails, try to fix common issues
            st.warning(f"JSON parsing error: {e}. Attempting to fix...")
            
            # Try to extract just the JSON part using regex
            import re
            json_pattern = r'(\{[\s\S]*\})'
            match = re.search(json_pattern, content)
            
            if match:
                try:
                    result = json.loads(match.group(1))
                    # Handle field name differences if needed
                    if "score_reasoning" in result and "viability_reasoning" not in result:
                        result["viability_reasoning"] = result["score_reasoning"]
                except json.JSONDecodeError:
                    # If that fails, try to fix common JSON issues
                    fixed_content = content.replace('\n', ' ')
                    # Fix unescaped quotes in strings
                    fixed_content = re.sub(r'(?<!")(".*?)(?<!")(")', r'\1\\"', fixed_content)
                    
                    try:
                        result = json.loads(fixed_content)
                        # Handle field name differences if needed
                        if "score_reasoning" in result and "viability_reasoning" not in result:
                            result["viability_reasoning"] = result["score_reasoning"]
                    except json.JSONDecodeError:
                        # Last resort: manually construct a basic response
                        st.error("Could not parse JSON response. Using fallback data.")
                        result = {
                            "elevator_pitch": "A compelling business idea worth exploring further.",
                            "business_name": "Business Concept",
                            "tagline": "Innovation meets opportunity",
                            "target_market": "Potential customers interested in this solution",
                            "key_features": ["Feature 1", "Feature 2", "Feature 3"],
                            "marketing_strategy": "A multi-channel approach to reach target customers",
                            "viability_score": 5,
                            "viability_reasoning": "This idea has potential but needs further development",
                            "fun_fact": "Did you know? Businesses that start with a clear plan are 30% more likely to succeed!",
                            "projected_valuation": "$1M - $5M potential with the right execution"
                        }
            else:
                # If no JSON-like structure found, use fallback
                st.error("No JSON structure found in response. Using fallback data.")
                result = {
                    "elevator_pitch": "A compelling business idea worth exploring further.",
                    "business_name": "Business Concept",
                    "tagline": "Innovation meets opportunity",
                    "target_market": "Potential customers interested in this solution",
                    "key_features": ["Feature 1", "Feature 2", "Feature 3"],
                    "marketing_strategy": "A multi-channel approach to reach target customers",
                    "viability_score": 5,
                    "viability_reasoning": "This idea has potential but needs further development",
                    "fun_fact": "Did you know? Businesses that start with a clear plan are 30% more likely to succeed!",
                    "projected_valuation": "$1M - $5M potential with the right execution"
                }
        
        # Validate that all required keys are present
        required_keys = ["elevator_pitch", "business_name", "tagline", "target_market", 
                        "key_features", "marketing_strategy", "viability_score", 
                        "viability_reasoning", "fun_fact", "projected_valuation"]
        
        missing_keys = [key for key in required_keys if key not in result]
        if missing_keys:
            st.warning(f"Response is missing these required keys: {', '.join(missing_keys)}")
            # Add default values for missing keys
            for key in missing_keys:
                if key == "key_features":
                    result[key] = ["Feature information not provided"]
                elif key == "viability_score":
                    result[key] = "5"  # Default middle score
                elif key == "projected_valuation":
                    result[key] = "$1M - $5M potential with the right execution"
                else:
                    result[key] = "Information not provided"
        
        return result
        
    except Exception as e:
        st.error(f"Error analyzing business idea: {e}")
        if 'content' in locals():
            st.code(content, language="json")
        return None# Input area - use session state values if available
idea_input = st.text_input("Enter any business idea (even silly ones):", 
                         value=st.session_state.idea_input,
                         placeholder="e.g., 'Subscription service for left socks only' or 'AI-powered plant therapist'")

additional_context = st.text_area("Any additional context? (optional)", 
                                value=st.session_state.additional_context,
                                height=100, 
                                placeholder="Target market, special features, etc.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("✨ Generate Pitch!", use_container_width=True):
        if not idea_input:
            st.warning("Please enter a business idea first!")
        elif not groq_api_key:
            st.error("Please enter your Groq API key in the sidebar to generate pitches.")
            st.info("💡 Get your free API key from [Groq Console](https://console.groq.com/)")
        else:
            with st.spinner("Our AI business analysts are working their magic..."):
                # Add slight delay for dramatic effect
                time.sleep(1.5)
                
                # Call Groq API to analyze the idea
                pitch_data = analyze_business_idea(idea_input, additional_context, model_option)
                
                if pitch_data:
                    # Store the generated pitch in session state
                    st.session_state.pitch_data = pitch_data
                    st.session_state.idea = idea_input
                    st.rerun()

# Display debug information if debug mode is enabled
# if st.session_state.debug_mode and "debug_info" in st.session_state and st.session_state.debug_info:
#     with st.expander("Debug Information", expanded=True):
#         st.json(st.session_state.debug_info)

# Display the generated pitch if available
if 'pitch_data' in st.session_state:
    pitch_data = st.session_state.pitch_data
    idea = st.session_state.idea
    
    # Business name and tagline with enhanced styling
    st.markdown("""
<style>
    /* Business card container */
    .business-card {
        background: linear-gradient(135deg, rgba(30, 30, 40, 0.9) 0%, rgba(50, 50, 70, 0.9) 100%);
        border-radius: 12px;
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        border-left: 5px solid #BB86FC;
        position: relative;
        overflow: hidden;
    }
    
    /* Decorative element */
    .business-card::before {
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        width: 150px;
        height: 150px;
        background: radial-gradient(circle, rgba(187, 134, 252, 0.2) 0%, rgba(187, 134, 252, 0) 70%);
        border-radius: 0 0 0 100%;
        z-index: 0;
    }
    
    /* Business name */
    .business-name-container {
        margin-bottom: 15px;
        position: relative;
        z-index: 1;
    }
    
    .business-name {
        font-family: 'Poppins', sans-serif !important;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        color: #BB86FC !important;
        margin: 0 !important;
        line-height: 1.2 !important;
        letter-spacing: -0.5px !important;
        text-shadow: 0 0 15px rgba(187, 134, 252, 0.4) !important;
    }
    
    /* Tagline */
    .tagline-container {
        position: relative;
        z-index: 1;
    }
    
    .tagline {
        font-family: 'Roboto', sans-serif !important;
        font-size: 1.6rem !important;
        font-weight: 500 !important;
        font-style: normal !important;
        color: #03DAC6 !important;
        text-transform: uppercase;
        margin: 0 !important;
        padding-left: 2px !important;
        letter-spacing: 0.5px !important;
    }
</style>
""", unsafe_allow_html=True)

    # Display business name and tagline in a card-like container
    st.markdown(f"""
<div class="business-card">
    <div class="business-name-container">
        <h1 class="business-name">{pitch_data['business_name']}</h1>
    </div>
    <div class="tagline-container">
        <p class="tagline">{pitch_data['tagline']}</p>
    </div>
</div>
""", unsafe_allow_html=True)

    # Logo - more prominent, without the extra box
    st.markdown("<div class='section-title'>Company Logo</div>", unsafe_allow_html=True)
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)

    # Check if Gemini API key is available and generate logo
    if 'generated_logo' not in st.session_state or st.session_state.get('last_business_name') != pitch_data['business_name']:
        with st.spinner("Generating logo..."):
            # Get the tagline from pitch data
            tagline = pitch_data.get('tagline', '')
        
            # Generate logo with business name, concept, and tagline
            st.session_state.generated_logo = generate_logo(
                pitch_data['business_name'], 
                idea,
                tagline
            )
            st.session_state.last_business_name = pitch_data['business_name']

    # Display the cached logo
    st.image(st.session_state.generated_logo, width=400)
    st.markdown('</div>', unsafe_allow_html=True)

    # Projected Valuation - new fun element
    if 'projected_valuation' in pitch_data:
        st.markdown("<div class='valuation-label'>Projected Valuation</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='valuation'>{pitch_data['projected_valuation']}</div>", unsafe_allow_html=True)

    # Elevator pitch
    st.markdown("<div class='section-title'>Elevator Pitch</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='content-card elevator-card'><div class='elevator-pitch'>\"{pitch_data['elevator_pitch']}\"</div></div>", unsafe_allow_html=True)

    # Key details
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='section-title'>Target Market</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='content-card target-card'><div class='content-text'>{pitch_data['target_market']}</div></div>", unsafe_allow_html=True)
        
        st.markdown("<div class='section-title'>Key Features</div>", unsafe_allow_html=True)
        features_html = "<div class='content-card features-card'><ul class='feature-list'>"
        for feature in pitch_data['key_features']:
            features_html += f"<li class='content-text'>{feature}</li>"
        features_html += "</ul></div>"
        st.markdown(features_html, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='section-title'>Marketing Strategy</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='content-card marketing-card'><div class='content-text'>{pitch_data['marketing_strategy']}</div></div>", unsafe_allow_html=True)
        
        st.markdown("<div class='section-title'>Did You Know?</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='content-card funfact-card'><div class='content-text'>{pitch_data['fun_fact']}</div></div>", unsafe_allow_html=True)
    
    # Viability score with better formatting
    st.markdown("<div class='section-title'>Business Viability Score</div>", unsafe_allow_html=True)
    try:
        score = int(float(str(pitch_data['viability_score']).strip()))
        # Ensure score is within bounds
        score = max(1, min(10, score))
    except:
        score = 5  # Default if parsing fails

    # Use columns for layout with fixed width for score column
    score_col, progress_col = st.columns([1, 9])

    with score_col:
        # Center the score in its column with CSS
        st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; width: 100%;">
            <div class='score-value'>{}/10</div>
        </div>
        """.format(score), unsafe_allow_html=True)

    with progress_col:
        # Add some vertical spacing to align with the score
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
        
        # Add the label
        # st.markdown("<div class='progress-label'>Viability Rating</div>", unsafe_allow_html=True)
        
        # Single progress bar
        st.progress(score/10)

    # Add explanation below the score
    st.markdown("\n")
    st.markdown(f"<div class='content-card'><div class='content-text'><b>Analysis:</b> {pitch_data['viability_reasoning']}</div></div>", unsafe_allow_html=True)
    
    # Regenerate button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("♻️ Generate Another Pitch", use_container_width=True):
            del st.session_state.pitch_data
            st.session_state.idea_input = ""
            st.session_state.additional_context = ""
            st.rerun()

# Add a footerx
st.markdown("---")
st.caption("Pitch Perfecter powered by Llama 3.3 via Groq")
