# Trip Companion!

## Description
"Trip Companion" is a Streamlit web application that utilizes the Gemini Generative AI API to provide informative descriptions for uploaded images of historical places. It simulates a tour guide experience, generating details about architectural features, descriptions, directions, and more.

## Features
- Upload images of historical places or nature scenes.
- Receive informative descriptions like a tourist guide.
- Explore architectural features in a tabular or bulleted format.
- Get details on how to reach the place, timings, entry fees, and Google Maps direction links.

## Usage
1. Visit the application [here](https://trip-companion.streamlit.app/).
2. Upload an image of a historical place or a nature scene.
3. Click on the "Discover🔎" button.
4. Wait for the AI to process the image and provide information.
5. Review the generated content and explore the insights.

## Dependencies
- `dotenv`: For loading environment variables.
- `google.generativeai`: Wrapper for the Gemini Generative AI API.
- `streamlit`: Framework for creating web applications.
- `PIL`: Python Imaging Library for image processing.
- `time`: Used for adding a delay during processing.

## Configuration
1. Install dependencies using `pip install -r requirements.txt`.
2. Set up a `.env` file with your Gemini API key.

## How to Run
```python
streamlit run your_app_name.py
```

### Developed with ❤ by Ambarish.

