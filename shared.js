function showQuestion() {

    function showQuestion(quiz) {
        // Check if the quiz object is defined and has a 'question' property
        if (quiz && quiz.question) {
            console.log("Question:", quiz.question);
        } else {
            console.log("Quiz or question is undefined");
        }
    }
    
    const questionElement = document.getElementById('question');
    questionElement.textContent = currentQuestions[currentQuestion].question;
  }