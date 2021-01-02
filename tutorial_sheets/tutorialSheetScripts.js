let answerButtons;
let answers;


// Set default options for new desmos graphs
let defaultGraphOptions = {
    keypad: false, 
    expressions: false,
    settingsMenu: false,
    yAxisLabel: "f(x)",
    yAxisArrowMode: Desmos.AxisArrowModes.POSITIVE
};

let piOptions = {
    keypad: false, 
    expressions: false,
    settingsMenu: false,
    xAxisStep: 3.141592653589793,
    yAxisStep: 3.141592653589793,
    yAxisLabel: "f(x)",
    yAxisArrowMode: Desmos.AxisArrowModes.POSITIVE
};


function makeSimpleGraph(element_id, latex, options){
    let elt = document.getElementById(element_id);
    let calculator = Desmos.GraphingCalculator(elt, options);
    calculator.setExpression({ 
        id: 'graph1', 
        latex: latex 
    });

    return calculator;
}

window.addEventListener("DOMContentLoaded", (event) => {
    answers = document.getElementsByClassName("answer");

    for(let i = 0; i < answers.length; i++) {
        let answerButton = document.createElement("p");
        answerButton.textContent = "Toggle answer";
        answerButton.className = "answerButton";
        answerButton.onclick = function() {
            answer = answers.item(i);
            if (answer.style.display == "block") {
                answer.style.display = "none";
            } else {
                answer.style.display = "block";
            }
        }

        let parent = answers.item(i).parentNode;

        parent.insertBefore(answerButton, answers.item(i));
    }

    answerButtons = document.getElementsByClassName("answerButton");
});


function displayAnswerButtons(style){
    for(let i = 0; i < answerButtons.length; i++) {
        answerButtons.item(i).style.display = style;
    }
}

function displayAnswers(style){
    for(let i = 0; i < answers.length; i++) {
        answers.item(i).style.display = style;
    }
}