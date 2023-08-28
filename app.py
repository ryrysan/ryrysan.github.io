pip install flask
pip install chatterbot

from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a new chatbot instance
chatbot = ChatBot('MyChatbot')

# Create and set up a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using English language data
trainer.train('chatterbot.corpus.english')

@app.route('/get_response', methods=['POST'])
def get_chatbot_response():
    user_input = request.json['user_input']
    response = chatbot.get_response(user_input).text
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)


<script>
// ...

function sendQuestion() {
  const userInput = document.getElementById('user-input').value;
  document.getElementById('user-input').value = ''; // Clear the input field

  if (!userInput.trim()) return;

  // Display the user's question in the chat history
  appendChatMessage('You', userInput);

  // Make API call to the ChatGPT API
  fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer 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', // Replace with your actual API key
    },
    body: JSON.stringify({
      prompt: `Math question: ${userInput}`,
      max_tokens: 150,
    }),
  })
  .then(response => response.json())
  .then(data => {
    // Extract the chatbot's response from the API response
    const chatbotResponse = data.choices[0].text.trim();

    // Display the chatbot's response in the chat history
    appendChatMessage('ChatGPT', chatbotResponse);
  })
  .catch(error => {
    console.error('Error fetching response from ChatGPT API:', error);
  });
}

function appendChatMessage(sender, message) {
  const chatHistory = document.getElementById('chat-history');
  const messageDiv = document.createElement('div');
  messageDiv.className = 'chat-message';
  messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatHistory.appendChild(messageDiv);
}
</script>
<!-- ... -->

<script>
// Existing JavaScript code here
// ...
</script>

<script>
// ...

function sendQuestion() {
  // The code for sending questions to the chatbot is fine and remains unchanged.
}

function appendChatMessage(sender, message) {
  // The code for appending chat messages is fine and remains unchanged.
}
</script>
</body>
</html>
<div id="chat-container">
<div id="chat-history">
  <!-- Chat messages will be appended here -->
</div>
<div id="chat-input">
  <input type="text" id="user-input" placeholder="Type your math question...">
  <button onclick="sendQuestion()" class="button">Send</button>
</div>
</div>

<!-- ... (your existing code) -->

<script>
// ... (your existing JavaScript code)

// Remove any duplicated or conflicting code here

function sendQuestion() {
  const userInput = document.getElementById('user-input').value;
  document.getElementById('user-input').value = ''; // Clear the input field

  if (!userInput.trim()) return;

  // Display the user's question in the chat history
  appendChatMessage('You', userInput);

  // Make API call to the ChatGPT APIaqw`
  // ... (your existing API code)
}

function appendChatMessage(sender, message) {
  const chatHistory = document.getElementById('chat-history');
  const messageDiv = document.createElement('div');
  messageDiv.className = 'chat-message';
  messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatHistory.appendChild(messageDiv);
}
</script>