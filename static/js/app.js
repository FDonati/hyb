const scenInputBtn = document.querySelector('#ScenInputTables');

const hybInputBtn = document.querySelector('#HybTables');

const scenTabDiv = document.querySelector("#scenarios")
const chartTabDiv = document.querySelector("#charts")
const hybTabDiv = document.querySelector("#HybTables")

scenInputBtn.onclick = function() {
    if (scenTabDiv.style.display !== 'none') {
        scenTabDiv.style.display = 'none';
    }
    else {
        scenTabDiv.style.display = 'block';
    }
};

hybInputBtn.addEventListener('click', function () {
    if (hybTabDiv.style.display == "none") {
        hybTabDiv.style.display = "";
    } 
})