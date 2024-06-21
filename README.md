---
title: 'Your own Assistant 🔥'
tags: ['PDA']
---


# Your own Assistant 🔥

This folder contains a simple Chainlit application that integrates with the Huggingface declare-lab/flan-alpaca-large model to create an interactive chat experience .

## High-Level Description

The `app.py` script sets up a Chainlit chat interface that communicates with the Anthropic API. When a chat starts, it initializes a session and displays an avatar for Claude. As users interact with the chat, their queries are sent to the Anthropic API, which generates responses using the Claude model. The conversation history is maintained in the session to provide context for Claude's responses.

## Quickstart


 Install the required Python packages by running:
```shell
pip install -r requirements.txt
```
 Run the `app.py` script to start the Chainlit server.
```shell
chainlit run app.py
```

 Interact with Assistant through the Chainlit interface.

### Function Definitions

- `start_chat`: Initializes the chat session and sets up the avatar for Claude.
- `call_gpt`: Sends the user's query to the Anthropic API and streams the response back to the chat interface.
- `chat`: Receives messages from the user and passes them to the `call_gpt` function.
