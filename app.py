import chainlit as cl
import os
import requests
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Webhook configuration
WEBHOOK_URL = "https://podhealthn8n.4gd.ai/prod/v1/e1e0ee50-1d9f-41c1-8910-0d383bb8ddeb/chat"

@cl.on_chat_start
async def start():
    # Initialize session
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    cl.user_session.set("session_id", session_id)
    cl.user_session.set("context", [])
    
    # Welcome message
    await cl.Message(
        content="Welcome to NeuroGPT! How can I help you today?",
        author="NeuroGPT"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # Get session data
    session_id = cl.user_session.get("session_id")
    context = cl.user_session.get("context")
    
    # Add user message to context
    context.append({
        "role": "user",
        "content": message.content
    })
    
    # Keep only last 5 messages for context
    if len(context) > 5:
        context = context[-5:]
    
    # Update context in session
    cl.user_session.set("context", context)
    
    # Show loading message
    msg = cl.Message(
        content="Thinking...",
        author="NeuroGPT"
    )
    await msg.send()
    
    try:
        # Prepare payload
        payload = {
            "chatInput": message.content,
            "sessionId": session_id,
            "context": context,
            "userId": "user",  # You can customize this
            "timestamp": datetime.now().isoformat()
        }
        
        # Make request to webhook
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract just the message content from the response
            if isinstance(data, dict):
                # Try to get the actual message content
                message_content = (
                    data.get("output") or 
                    data.get("response") or 
                    data.get("message") or 
                    data.get("text") or 
                    data.get("content")
                )
                
                # If we found a message, use it; otherwise use the whole response
                if message_content:
                    formatted_response = message_content
                else:
                    formatted_response = str(data)
            else:
                formatted_response = str(data)
            
            # Add bot response to context
            context.append({
                "role": "assistant",
                "content": formatted_response
            })
            cl.user_session.set("context", context)
            
            # Update message with the response
            msg.content = formatted_response
            await msg.update()
            
        else:
            error_msg = f"Error: Failed to get response (Status {response.status_code})"
            msg.content = error_msg
            await msg.update()
            
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        msg.content = error_msg
        await msg.update() 