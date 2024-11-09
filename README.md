# IloveText Project

This project provides a web application built with Flask for performing various text processing tasks, such as text summarization and translation.

## Features

- **Text Summarization**: Automatically summarizes input text using the `facebook/bart-large-cnn` model.
- **Translation**: Translates text between different languages using the `facebook/m2m100_418M` model.
- **Language Detection**: Automatically detects the language of the input text and translates it to English for processing, if necessary.
- **Multilingual Support**: Supports multiple languages for input and output, offering automatic translations back to the original language after summarization.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmed151515/IloveText.git
   ```

````

2. Navigate to the project directory:

   ```bash
   cd IloveText
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python run.py
   ```

The application should now be accessible at `http://127.0.0.1:5000/`.

## Routes

- **`/`**: Home page that displays available routes.
- **`/summarize`**: Summarize a given text.
- **`/translate`**: Translate a given text into the selected language.

## How It Works

1. **Summarize**:

   - The user inputs a text.
   - The language of the text is detected. If it's not in English, it is translated to English.
   - The English text is summarized using the pre-trained BART model.
   - The summary is translated back to the original language if necessary.

2. **Translate**:
   - The user inputs a text and selects a target language.
   - The text is translated into the selected language using the pre-trained M2M100 model.
````
