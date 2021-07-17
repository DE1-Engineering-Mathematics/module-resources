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

    if (style === 'block') {
        document.getElementById('showAnswerButton').style.display = "none";
        document.getElementById('hideAnswerButton').style.display = "block";
    }
    else if (style === 'none') {
        document.getElementById('showAnswerButton').style.display = "block";
        document.getElementById('hideAnswerButton').style.display = "none";
    }

}

function displayAnswers(style) {
    for (let i = 0; i < answers.length; i++) {
        answers.item(i).style.display = style;
    }

    if (style === 'block') {
        document.getElementById('showAnswers').style.display = "none";
        document.getElementById('hideAnswers').style.display = "block";
    }
    else if (style === 'none') {
        document.getElementById('showAnswers').style.display = "block";
        document.getElementById('hideAnswers').style.display = "none";
    }

}

// For printing - adding whitespace
function prepareForPrint(style) {
    for (let i = 0; i < whitespace.length; i++) {
        whitespace.item(i).style.display = style;
    }

    if (style === 'block') {
        document.getElementById('showPrint').style.display = "none";
        document.getElementById('hidePrint').style.display = "block";
    }
    else if (style === 'none') {
        document.getElementById('showPrint').style.display = "block";
        document.getElementById('hidePrint').style.display = "none";
    }
}