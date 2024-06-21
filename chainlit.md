# Your own Assistant 🔥

A simple Chainlit application that integrates with the Huggingface declare-lab/flan-alpaca-large model to create an interactive chat experience .

## High-Level Description

The `app.py` script sets up a Chainlit chat interface that communicates with the Anthropic API. When a chat starts, it initializes a session and displays an avatar for Claude. As users interact with the chat, their queries are sent to the Anthropic API, which generates responses using the Claude model. The conversation history is maintained in the session to provide context for Claude's responses.


