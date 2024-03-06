// Global variables
let clonedSvg = null;
const selectedAnswers = {};


function fetchQuestions() {
    console.log('Attempting to fetch questions');
    fetch('questions.json')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(questions => {
        console.log('Questions fetched successfully', questions);
        setupQuestionnaire(questions);
      })
      .catch(error => console.error('Error loading questions:', error));
  }
  
function setupQuestionnaire(questions) {
const container = document.getElementById('questions-container');

questions.forEach((q, index) => {
    const questionSection = document.createElement('div');
    questionSection.classList.add('question-section', 'hidden');
    questionSection.id = `question${index + 1}`;

    const questionText = document.createElement('p');
    questionText.classList.add('question');
    questionText.textContent = q.question;

    const answersDiv = document.createElement('div');
    answersDiv.classList.add('answers');

    q.answers.forEach(answer => {
    const answerButton = document.createElement('button');
    answerButton.classList.add('answer-button');
    answerButton.textContent = answer;
    answerButton.dataset.answer = answer;
    answersDiv.appendChild(answerButton);
    });

    const nextButton = document.createElement('button');
    nextButton.classList.add('next-button');
    nextButton.textContent = 'Next';

    questionSection.appendChild(questionText);
    questionSection.appendChild(answersDiv);
    questionSection.appendChild(nextButton);

    container.appendChild(questionSection);
});

addEventListeners();
}

function addEventListeners() {
const startButton = document.getElementById('start-button');
if (startButton) {
    startButton.addEventListener('click', function() {
    document.getElementById('welcome-section').classList.add('hidden');
    const firstQuestion = document.getElementById('question1');
    if (firstQuestion) {
        firstQuestion.classList.remove('hidden');
    } else {
        console.error('First question section not found');
    }
    });
} else {
    console.error('Start button not found');
}

document.querySelectorAll('.next-button').forEach((button, index, buttons) => {
    button.addEventListener('click', function() {
    const currentSection = document.getElementById(`question${index + 1}`);
    const nextSection = document.getElementById(`question${index + 2}`);
    if (currentSection) {
        currentSection.classList.add('hidden');
    }
    if (nextSection) {
        nextSection.classList.remove('hidden');
    } else if (index + 1 === buttons.length) {
        console.log('End of the questionnaire');
    }
    });
});

document.querySelectorAll('.answer-button').forEach(button => {
    button.addEventListener('click', function() {
      // Remove 'selected' from all buttons in this answer group
      this.parentElement.querySelectorAll('.answer-button').forEach(btn => {
        btn.classList.remove('selected');
      });
      this.classList.add('selected');
  
      // Store the selected answer
      const questionIndex = this.closest('.question-section').id.replace('question', '');
      selectedAnswers[questionIndex] = this.dataset.answer;
  
      // Update the cloned SVG with the selected answer's color
      const selectedAnswer = this.dataset.answer;
      const mapping = answerMapping[selectedAnswer];
      if (mapping && clonedSvg) {
        colorSegment(mapping.elementId, mapping.color);
      } else {
        console.warn(`No color mapping found for answer: ${selectedAnswer}`);
      }
  
      // Show the current state of the disco ball
      showCurrentDiscoBall();
    });
  });
  
}

document.addEventListener('DOMContentLoaded', () => {
    fetchQuestions();

    fetch('../assets/DiscoBallSilver.svg') // Adjust the path to the SVG file
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(svgData => {
            const svgContainer = document.getElementById('svgContainer');
            svgContainer.innerHTML = svgData;
            // This is your original SVG now part of the DOM
            const originalSvg = svgContainer.querySelector('svg');
            
            // Assign a new ID to your original SVG if necessary
            originalSvg.id = 'originalSvgId'; 

            // Make a copy of the SVG for manipulation
            clonedSvg = originalSvg.cloneNode(true);
            // Assign a new ID to the cloned SVG to differentiate it
            clonedSvg.id = 'clonedSvgId';

            // Append the cloned SVG to the DOM if needed, or keep it off-DOM until needed
            // document.body.appendChild(clonedSvg); // Uncomment if you want to append it immediately

            // Continue with any additional initialization...
        })
        .catch(error => console.error('Error loading SVG:', error));
});


/**
 * Colors an SVG segment with the provided color.
 * @param {string} elementId - The ID of the SVG element to color.
 * @param {string} color - The color to apply to the element.
 */
function colorSegment(elementId, color) {
    const svgElement = clonedSvg.getElementById(elementId); // Use getElementById on the cloned SVG
    if (svgElement) {
      svgElement.style.fill = color;
    } else {
      console.warn(`Element with ID ${elementId} not found in the cloned SVG.`);
    }
  }
  // Example usage:
  // colorSegment('visualSegmentId', '#FF0000');

function showCurrentDiscoBall() {
    const svgDisplayContainer = document.getElementById('svgDisplayContainer'); // Replace with your actual container ID
    svgDisplayContainer.innerHTML = ''; // Clear any existing content
    svgDisplayContainer.appendChild(clonedSvg); // Append the cloned SVG
}

// ... call showCurrentDiscoBall() whenever you want to display the updated disco ball
// (e.g. after each question is answered)  
  

  