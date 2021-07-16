let answerButtons;
let answers;
let whitespace;

window.addEventListener("DOMContentLoaded", (event) => {
    answers = document.getElementsByClassName("answer");

    for (let i = 0; i < answers.length; i++) {
        let answerButton = document.createElement("p");
        answerButton.textContent = "Toggle answer";
        answerButton.className = "answerButton";
        answerButton.onclick = function () {
            const answer = answers.item(i);
            if (answer.style.display === "block") {
                answer.style.display = "none";
            } else {
                answer.style.display = "block";
            }
        }

        let parent = answers.item(i).parentNode;

        parent.insertBefore(answerButton, answers.item(i));
    }

    answerButtons = document.getElementsByClassName("answerButton");
    whitespace = document.getElementsByClassName("workingout");

    for (let i = 0; i < whitespace.length; i++) {
        whitespace.item(i).style.display = "none";
    }

});


function displayAnswerButtons(style) {
    for (let i = 0; i < answerButtons.length; i++) {
        answerButtons.item(i).style.display = style;
    }

}

function displayAnswers(style) {
    for (let i = 0; i < answers.length; i++) {
        answers.item(i).style.display = style;
    }
}

// For printing - adding whitespace
function prepareForPrint(style) {
    for (let i = 0; i < whitespace.length; i++) {
        whitespace.item(i).style.display = style;
    }
}