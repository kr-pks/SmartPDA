import time
import chainlit as cl
from transformers import pipeline

@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "prompt_history",
        "",
    )
    await cl.Avatar(
        name="SmartPDA",
        url="https://www.anthropic.com/images/icons/apple-touch-icon.png",
    ).send()

@cl.step(name="SmartPDA", type="llm", root=True)
async def call_gpt(query: str):
    prompt_history = cl.user_session.get("prompt_history")
    prompt = f"{prompt_history} Use above as chat history and try to respond on the below query \n {query}"

    pipe = pipeline(model="declare-lab/flan-alpaca-large")

    outputs = pipe(prompt, max_length=128, do_sample=True)

    print(outputs[0]["generated_text"])
    time.sleep(4)
    cl.user_session.set("prompt_history", prompt + cl.context.current_step.output)
    await cl.Message(content=outputs[0]["generated_text"]).send()


@cl.on_message
async def chat(message: cl.Message):
    await call_gpt(message.content)
