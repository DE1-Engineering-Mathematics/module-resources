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