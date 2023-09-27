let dragged = null;
const fetchTenses = async () => {
    try {
        let response = await fetch(apiUrl);
        if (response.ok) {
            let data = await response.json();
            //console.log("data fetched: " + `${data}`);
            return data;
        } else {
            console.error("Failed to fetch data:", response.status, response.statusText);
        }
    } catch (error) {
        console.error("Error while fetching data:", error);
    }
}

let apiUrl = "";

// Confirm the tense selected
const tensesList = document.querySelector("#tenses");

// Create a function to update APIUrl to which we add the tense selected
const updateApiUrl = (selectedTense) => {
    apiUrl = "/tenses/" + `${selectedTense}`;
}

tensesList.addEventListener("change", (event) => {
    if(event.target.value !== "default"){  
        const selectedTense = event.target.value;
        updateApiUrl(selectedTense);
    }

    // Call the function to fetch data when the tense is selected
    fetchTenses()
        .then((result) => {

            
            // Access the "choices" and "questions" properties from the resolved object
            const choicesSelected = result.choices;
            const questionsSelected = result.questions;


            //console.log(choicesSelected);
            //console.log(questionsSelected);

            //create variables 
            let displayedQuestion = 0;
            let currentTotalPoints = 0;

            //define behavior of startButton 
            const startButton = document.querySelector("#start-button")                       
            startButton.addEventListener("click", (event) =>{
                event.preventDefault();
                startQuiz();
            });

            //Create variables of different html elements and event listeners and set behavior
            const instructions = document.querySelector("#instructions");
            const containerQuiz = document.querySelector(".container-quiz");
            const questionContainer = document.querySelector("#question-container");
            const nextButton = document.querySelector("#next-button");
            nextButton.addEventListener("click", () => {
                event.preventDefault();
                setNextQuestion(displayedQuestion);
            });
            const text_before = document.querySelector(".text_before");
            const text_after = document.querySelector(".text_after");
            const blank = document.querySelector('.blank');
            const choices = document.querySelector('.choices');
            const tensesMenu = document.querySelector('.tenses-menu');
            
            const startQuiz = () => {
                questionContainer.classList.remove("hide");
                console.log("Quiz started");
                startButton.classList.add("hide");                      
                tensesMenu.classList.add("hide");
                setNextQuestion(displayedQuestion);
                points.textContent = "Points: " + 0 + "/" + questionsSelected.length;
            }

            const setNextQuestion = () => {
                // Clear previous questions and choices
                text_before.textContent = '';
                text_after.textContent = '';
                choices.innerHTML = '';
                blank.innerHTML = '';
                answerFeedback.innerHTML = '';
                submitClicked = false;

                // Reset state
                blank.className = 'blank';
                nextButton.classList.add("hide");
                tensesMenu.classList.add("hide");
                submit.classList.remove("hide");
                answerFeedback.classList.remove("feedback-wrong");
                answerFeedback.classList.remove("feedback-correct");

                if (displayedQuestion < questionsSelected.length) {
                    // Set the question text
                    text_before.textContent = questionsSelected[displayedQuestion].question_number + ". " + questionsSelected[displayedQuestion].question_text_before;
                    text_after.textContent = questionsSelected[displayedQuestion].question_text_after;

                    // Select choices for the current question
                    let choicesDisplayed = choicesSelected.filter((item) => {
                        return item.question_number === displayedQuestion + 1;
                    });

                    // Display choices
                    choicesDisplayed.forEach((choiceItem) => {
                        const span = document.createElement("span");
                        span.className = "choice";
                        span.id = choiceItem.choice;
                        span.textContent = choiceItem.choice;
                        span.draggable = true;
                        span.is_correct = choiceItem.is_correct;
                        span.addEventListener('click', (e) => {
                            if(!submitClicked){
                                dragged = e.target;
                                
                                //console.log("choice tapped:" + dragged + "choice correctness: " + e.target.is_correct);
                                handleChoiceClick(dragged);
                            }
                        });
                        choices.appendChild(span);
                    });

                    // Increment the displayedQuestion
                    displayedQuestion++;
                } else {
                    // Handle end of questions
                    choices.classList.add("hide");
                    submit.classList.add("hide");
                    instructions.classList.add("hide");
                    blank.classList.add("hide");
                    document.querySelector(".quiz-completed-message").classList.remove("hide");
                    document.querySelector(".quiz-score").textContent = "Your Score: " +  (currentTotalPoints * 100 / questionsSelected.length) + "%";
                    console.log("Quiz completed!");                            
                }
            }

            //dragged will be the element that is dragged from the choices list
            //when the drag starts we can set the data from the element so we can get it when the user drops it.
            choices.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('is_correct', e.target.is_correct);
                dragged = e.target;
                //console.log(dragged);
            });

            //Add effects for the blank zone when the user drags the element over it
            blank.addEventListener('dragover', (e) => {
                e.preventDefault();
                if (blank.firstChild) {
                    e.dataTransfer.dropEffect = 'none';
                } else {
                    e.target.classList.add('hover');
                }
            });
            
                            
            //Remove effects when leaves the blank zone
            blank.addEventListener('dragleave', (e) => {
                e.target.classList.remove('hover');
            });

            //Remove the hover effect from blank. Blank gets the data from the item and allows drop
            blank.addEventListener('drop', (e) => {
                e.target.classList.remove('hover');
                const is_correct = e.dataTransfer.getData('is_correct');
                if (e.target.className === 'blank' && !blank.firstChild){
                    e.target.appendChild(dragged);
                    blank.classList.add("dropped"); 
                    blank.firstChild.classList.add("dropped");
                    const allChoices = document.querySelectorAll('.choice');
                    allChoices.forEach((choice) => {
                            choice.draggable = false;
                    });
                    dragged.draggable = true;
                }
            });

            //reverse process if the user wants to change the answer before submitting
            blank.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('is_correct', e.target.is_correct);
                dragged = e.target;
            });

            choices.addEventListener('dragover', (e) => {
                e.preventDefault();
                e.target.classList.add('hover');
            });

            choices.addEventListener('dragleave', (e) => {
                e.target.classList.remove('hover');
            });

            choices.addEventListener('drop', (e) => {
                e.target.classList.remove('hover');
                e.dataTransfer.getData('is_correct');
                if (e.target.className === 'choices'){
                    e.target.appendChild(dragged);
                    blank.classList.remove("dropped"); 
                    dragged.classList.remove("dropped");
                    const allChoices = document.querySelectorAll('.choice');
                    allChoices.forEach((choice) => {
                        choice.draggable = true;
                    });
                };
            });
            let submitClicked = false;   

            // Function to handle a choice being tapped
            function handleChoiceClick(choiceElement) {
                //let isCorrect = choiceElement.is_correct;
                //console.log("choice correctness: " + isCorrect);
                
                if (!blank.firstChild){
                    blank.appendChild(choiceElement);
                    blank.classList.add("dropped"); 
                    blank.firstChild.classList.add("dropped");
                    const allChoices = document.querySelectorAll('.choice');
                    allChoices.forEach(choice => {
                            choice.draggable = false;
                    });
                dragged.draggable = true;
                }
            

                // Enable the change of answers before submission
               else {
                const allChoices = document.querySelectorAll('.choice');
                allChoices.forEach(choice => {
                        choice.draggable = false;
                });
                    blank.firstChild.classList.remove("dropped");
                    choices.appendChild(blank.firstChild);
                    
            
                    blank.appendChild(dragged);
                    blank.classList.add("dropped"); 
                    blank.firstChild.classList.add("dropped");
                    dragged.draggable = true;
                }

            }

            //create constants and variables to validate answers and update points
            const points = document.querySelector('#points')
            const answerFeedback = document.querySelector('#answerFeedback');
            const submit = document.querySelector('#submit');

            //When the button submit is clicked prevent the page from refreshing
            //Validate answer by checking the is_correct value
            //Provide feedback and update the points
            submit.addEventListener("click", (e) => {
                e.preventDefault();
                //console.log(dragged.is_correct);
                if (blank.firstChild) {
                    if(dragged.is_correct === 1){
                        answerFeedback.classList.add("feedback-correct");
                        answerFeedback.textContent = '¡Muy bien!';
                        const allChoices = document.querySelectorAll('.choice');
                        allChoices.forEach((choice) => {
                                if(choice == dragged){
                                    choice.classList.add("dragged-correct");
                                }
                        });
                        currentTotalPoints++;
                        points.textContent = "Points: " + currentTotalPoints + "/" + questionsSelected.length;

                    }
                    else{
                        answerFeedback.classList.add("feedback-wrong");
                        answerFeedback.textContent = '¡Uy, casi!';
                        const allChoices = document.querySelectorAll('.choice');
                        allChoices.forEach((choice) => {
                                if(choice == dragged){
                                    choice.classList.add("dragged-wrong");
                                }
                        });          
                    }
                    submitClicked = true;
                    dragged.draggable = false;
                    nextButton.classList.remove("hide");
                    submit.classList.add("hide");
                }
            });

        })
        .catch(error => {
            console.error(error);
        });
});