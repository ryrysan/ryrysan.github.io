function toggleHelpContent() {
  const helpContent = document.getElementById('help-content');
  window.open('ask_help.html', '_blank');
  
  }

function submitHelpQuestion() {
  const helpQuestion = document.getElementById('help-question').value;

  // You can implement the logic here to handle the submitted question, such as sending it to a server or displaying it on the page.
  // For this example, let's display an alert with the submitted question.
  alert(`Question submitted:\n\n${helpQuestion}`);

  // Clear the textarea
  document.getElementById('help-question').value = '';

  // Show the "Back to Quiz" button
  document.getElementById('back-to-quiz-container').style.display = 'block';
}

function backToQuiz() {
  // Close the "Ask a Question" tab
  window.close();
}