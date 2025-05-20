# NeuroGPT

<style>
/* Reduce header height */
.cl-header {
    height: 48px !important;
    min-height: 48px !important;
    box-sizing: border-box; /* Ensure padding doesn't add to height */
}

/* Hide specific elements in the header */
/* Target the text elements displaying the component names in the left header */
/* Assuming they are within specific divs or spans that are NOT the logo */
.cl-header-left span,
.cl-header-left div:not(:has(.cl-logo)) {
    display: none !important;
}

/* Target the New Chat button and Profile/Settings button in the right header */
/* These are likely buttons or divs containing icons */
.cl-header-right button,
.cl-header-right > div:not(:has(.cl-logo)) {
    display: none !important;
}

/* Ensure the Chainlit logo remains visible */
.cl-header-left .cl-logo,
.cl-header-left > a:first-child,
.cl-header-left > div:first-child:has(.cl-logo) {
    display: flex !important; /* Adjust display property if needed */
    visibility: visible !important; /* Ensure visibility */
    color: initial !important; /* Reset color in case it was set to transparent */
}

/* Hide the placeholder text in the input box and replace */
.cl-text-input::placeholder {
    color: transparent !important;
}
.cl-text-input {
    position: relative;
}
/* Use ::before or ::after for the custom placeholder */
.cl-text-input::after {
    content: "Type here...";
    color: #aaa; /* Placeholder text color */
    position: absolute;
    left: 12px; /* Adjust positioning as needed */
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none; /* Allows clicking through to the input */
}
/* Hide any other potential placeholder elements */
.cl-text-container .cl-placeholder,
.cl-input-container .cl-placeholder-text { /* Common classes for placeholder containers/text */
    display: none !important;
}

/* Hide the watermark text below the input box */
/* Target various potential elements that might contain the watermark */
.cl-chat-bottom-actions > div,
.cl-chat-bottom-actions > span,
.cl-chat-bottom-actions p,
.cl-chat-bottom-actions small, /* Sometimes watermarks are small text */
.cl-chat-bottom-actions .cl-watermark { /* Speculative watermark class */
    display: none !important;
}

/* Adjust chat container padding to create more space for messages */
.cl-chat-container {
    padding-top: 10px !important; /* Reduced top padding */
    padding-bottom: 10px !important; /* Reduced bottom padding */
    flex-grow: 1; /* Allow it to take available space */
    overflow-y: auto; /* Ensure scrolling within the message area */
}

/* Reduce vertical space between messages slightly */
.cl-message-group {
    margin-bottom: 6px !important; /* Reduced space between message groups */
}

/* Ensure message content takes available width and has reduced internal padding if needed */
.cl-message-content {
    max-width: 100%;
    padding: 4px 8px !important; /* Example: Reduced internal message padding */
}

/* Make input area more compact (footer) and position it below chat container */
.cl-input-container {
    padding: 8px !important; /* Reduced padding around input */
    margin-top: auto; /* Push the input container down */
    flex-shrink: 0; /* Prevent it from shrinking */
}

/* Remove unnecessary margins/padding from main chat area if any */
.cl-chat {
    margin: 0 !important;
    padding: 0 !important;
    display: flex; /* Use flexbox to manage chat and input layout */
    flex-direction: column; /* Stack chat container and input vertically */
    height: 100%; /* Ensure the chat area takes full height */
}

.cl-chat-content {
    padding: 0 !important;
    margin: 0 !important;
}

/* Ensure the main body/html allows flexbox to manage height */
html, body, #root {
    height: 100%;
    margin: 0;
    padding: 0;
}

/* Hide long component names in header and replace with short names */
.cl-header-left a, .cl-header-left button, .cl-header-left span {
    color: transparent !important;
    position: relative;
}
.cl-header-left a[href*="chat"]::after {
    content: "Chat";
    color: #e91e63;
    position: absolute;
    left: 0;
    top: 0;
}
.cl-header-left a[href*="readme"]::after {
    content: "Readme";
    color: #555;
    position: absolute;
    left: 0;
    top: 0;
}
.cl-header-right button, .cl-header-right a {
    color: transparent !important;
    position: relative;
}
.cl-header-right button[aria-label*="newChat"], .cl-header-right a[href*="newChat"] {
    color: transparent !important;
    position: relative;
}
.cl-header-right button[aria-label*="newChat"]::after, .cl-header-right a[href*="newChat"]::after {
    content: "New Chat";
    color: #e91e63;
    position: absolute;
    left: 0;
    top: 0;
}

/* Input placeholder hack */
.cl-text-input::placeholder {
    color: transparent !important;
}
.cl-text-input {
    position: relative;
}
.cl-text-input::after {
    content: "Type here...";
    color: #aaa;
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none;
}
</style>

This is an AI assistant powered by NeuroGPT. Feel free to ask any questions!

## Features
- Natural language conversation
- Context-aware responses
- Real-time interaction

## How to use
1. Type your question in the input box below
2. Press Enter or click the send button
3. Wait for NeuroGPT's response

## Note
The conversation history is maintained for context, but only the last 5 messages are used to keep responses relevant.

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Make messages collapsible
    document.querySelectorAll('.cl-message').forEach(message => {
        message.addEventListener('click', function() {
            this.classList.toggle('collapsed');
        });
    });

    // Make input container collapsible
    const inputContainer = document.querySelector('.cl-input-container');
    if (inputContainer) {
        inputContainer.addEventListener('click', function(e) {
            if (e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
                this.classList.toggle('collapsed');
            }
        });
    }

    // Make welcome message collapsible
    const welcomeMessage = document.querySelector('.cl-welcome-message');
    if (welcomeMessage) {
        welcomeMessage.addEventListener('click', function() {
            this.classList.toggle('collapsed');
        });
    }
});
</script> 