# Box Document Generation using a Pydanthic AI, and the Box MCP Server

A demo showcasing how to build a Pydantic AI agent capable of interacting with the Box MCP server and generating a document.

## Overview

This project provides a command-line interface for interacting with Box's document generation features using an AI agent. It enables users to upload templates, process data files, and generate documents automatically through conversational prompts.

## Features

- **Box Authentication**: Same as the MCP server
- **File Upload & Management**: Upload local files to Box folders
- **Document Template Management**: Mark files as document generation templates
- **Automated Document Generation**: Create documents using templates and data files
- **AI-Powered Interactions**: Converse naturally with the agent to perform tasks

## Prerequisites

- Python 3.11 or higher
- Box account with appropriate permissions
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/box-community/doc-gen-pydantic-ai-box-mcp-server.git
   cd doc-gen-pydantic-ai-box-mcp-server
   ```

2. Create a virtual environment:
   ```bash
   uv lock
   uv sync
   ```

4. Create a `.env` file with your OpenAI API keys:
   ```
    OPENAI_API_KEY = sk-YOUR API KEY
   ```
5. In your Box account create a folder named `OpenAI Doc Gen`
## Usage

Run the demo script to see the agent in action:

```bash
uv run src/demo.py
```

This will:
1. Authenticate with Box
2. Show who you're logged in as
3. Upload a template file to a specified Box folder
4. Mark the file as a document generation template
5. Upload data in JSON format
6. Generate a new document based on the template and data

## Project Structure

```
.
├── data/                 # Data files and templates
│   ├── nda_template.docx # Example document template
│   └── NDA.json          # Example data for document generation
├── src/                  # Source code
│   ├── console_utils.py  # Utilities for console output
│   └── demo.py           # Main demo script
├── .env                  # Environment variables (create this)
└── README.md             # This file
```

## How It Works

The agent uses:
- **OpenAI's GPT models** to interpret user instructions
- **pydantic_ai** to handle the agent framework
- **Box MCP Server** to communicate with Box's API

The workflow typically involves:
1. Initializing the agent with access to Box tools
2. Processing user commands in natural language
3. Executing appropriate Box operations
4. Providing feedback on operations performed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)
