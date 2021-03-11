const scenInputBtn = document.querySelector('#ScenInputTables');

const hybInputBtn = document.querySelector('#HybTables');

const scenTabDiv = document.querySelector("#scenarios")
const chartTabDiv = document.querySelector("#charts")
const hybTabDiv = document.querySelector("#HybTables")

scenInputBtn.addEventListener('click', function () {
        scenTabDiv.style.display = "block";
        chartTabDiv.style.display = "none";
})

hybInputBtn.addEventListener('click', function () {
    scenTabDiv.style.display = "none";
    chartTabDiv.style.display = "block";
})