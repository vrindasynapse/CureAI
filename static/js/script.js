console.log("Script Loaded!");

const chips = document.querySelectorAll(".chip");
const selectedBox = document.getElementById("selectedSymptoms");
const searchBox = document.getElementById("searchBox");
const select = document.getElementById("symptoms");

function updateSelected() {
    selectedBox.innerHTML = "";

    document.querySelectorAll(".chip.active").forEach(chip => {

        const tag = document.createElement("div");

        tag.className = "selected-chip";

        tag.innerText = chip.innerText;

        selectedBox.appendChild(tag);

    });
}

chips.forEach(chip => {

    chip.addEventListener("click", function () {

        this.classList.toggle("active");

        const value = this.dataset.value;

        const option = [...select.options].find(o => o.value === value);

        if (option) {
            option.selected = this.classList.contains("active");
        }

        updateSelected();

    });

});

searchBox.addEventListener("keyup", function () {

    const text = this.value.toLowerCase();

    chips.forEach(chip => {

        chip.style.display =
            chip.innerText.toLowerCase().includes(text)
                ? "inline-flex"
                : "none";

    });

});   