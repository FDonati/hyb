const scenInputBtn = document.querySelector('#ScenInputTables');

const hybInputBtn = document.querySelector('#HybTables');

const scenTabDiv = document.querySelector("#scenarios")
const chartTabDiv = document.querySelector("#charts")
const hybTabDiv = document.querySelector("#HybTables")

scenInputBtn.onclick = function () {
    if (scenTabDiv.style.display == "none") {
        scenTabDiv.style.display = "block";
        scenInputBtn.className = "is-active";
    } else {
        scenTabDiv.style.display = "none";
        scenInputBtn.className = "";
    }
};

hybInputBtn.addEventListener('click', function () {
    hybInputBtn.className = "is-active";
})