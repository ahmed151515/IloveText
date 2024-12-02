# IloveText Project

A powerful Flask-based web application for advanced text processing, featuring translation, summarization, and content moderation capabilities using state-of-the-art AI models.

## Features

- **Text Summarization**: 
  - Automatically summarizes long texts using the `facebook/bart-large-cnn` model
  - Supports multilingual input with automatic translation
  - Maintains original language in output
  
- **Translation**: 
  - High-quality translations using the `facebook/m2m100_418M` model
  - Supports multiple language pairs
  - Handles long texts through automatic chunking
  
- **Content Moderation**:
  - Automatic toxicity detection for input text
  - Prevents processing of inappropriate content
  - Uses the `martin-ha/toxic-comment-model`

- **Language Processing**:
  - Automatic language detection using `langid`
  - Smart handling of non-English inputs
  - Seamless translation pipeline

## Prerequisites

- Python 3.7+
- Hugging Face API key
- Internet connection for API access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ahmed151515/IloveText.git
```

2. Navigate to the project directory:
```bash
cd IloveText
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Hugging Face API key:
```
AUTH=your_huggingface_api_key_here
```

5. Run the Flask app:
```bash
python run.py
```

The application will be accessible at `http://127.0.0.1:5000/`

## Project Structure

```
IloveText/
├── src/
│   ├── functions.py    # Core text processing functions
│   ├── routes.py       # Flask routes and endpoints
│   ├── forms.py        # Form handling and validation
│   ├── templates/      # HTML templates
│   └── static/         # Static assets
├── run.py             # Application entry point
├── requirements.txt   # Project dependencies
└── .env              # Environment variables
```

## Routes

- **`/`**: Home page displaying available routes and features
- **`/summarize`**: Text summarization interface
- **`/translate`**: Text translation interface with language selection

## Technical Details

### Text Processing Pipeline

1. **Translation**:
   - Content moderation check
   - Text tokenization and chunking
   - API-based translation using M2M100
   - Chunk reassembly

2. **Summarization**:
   - Language detection
   - Translation to English (if needed)
   - Content moderation
   - Text summarization using BART
   - Translation back to original language

### API Integration

The project uses Hugging Face's Inference API for accessing various models:
- M2M100 for translation
- BART-CNN for summarization
- Toxic Comment Model for content moderation

## Error Handling

- Toxicity detection with user feedback
- API error handling
- Large text processing through chunking
- Language detection confidence reporting

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
