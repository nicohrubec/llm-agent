# llm-agent

A very simple LLM agent implementation from scratch with possibility to add tools. One tool is implemented as an example (file reading).

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up OpenAI API key

You need to set your OpenAI API key as an environment variable:

**On macOS/Linux:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**On Windows:**
```bash
set OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the main file to start chatting with ChatGPT:

```bash
python main.py
```

The application will start an interactive chat session with ChatGPT. You can use Ctrl+C to quit the chat.


