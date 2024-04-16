let defaultValues = {
    nSex: 0,
    nRestbp: 94,
    nThalach: 71,
    nCa: 0,
    nCp: 1,
    nSlope: 0,
    nThal: 0
};

const width = 100;
const height = 400;

const holder = d3.select(".child2")
.append("svg")
.attr("width", width)
.attr("height", height);

// draw a rectangle
const y0 = 20;
const height0 = 380;
holder.append("rect")
    .attr("x", 5)
    .attr("y", y0 + height0)
    .style("fill", "rgb(0,255,0)")
    .attr("height", 0)
    .attr("width", 90);

// draw a container rectangle
holder.append("rect")
    .attr("x", 5)
    .attr("y", y0)
    .style("fill", "none")
    .style("stroke", "lightblue")
    .style("stroke-width", 4)
    .attr("height", height0)
    .attr("width", 90);

// add text inside rectangle
holder.append("text")
    .text("0.00%")
    .attr("x", 12)
    .attr("y", y0 + height0 - 10)
    .attr("fill", "black")
    .attr("font-family", "Verdana")
    .attr("font-size", "20");

// initialize
let val01 = document.getElementById("nSex1").value;
let val02 = document.getElementById("nRestbp1").value;
let val03 = document.getElementById("nThalach1").value;
let val04 = document.getElementById("nCa1").value;
let val05 = document.getElementById("nCp1").value;
let val06 = document.getElementById("nSlope1").value;
let val07 = document.getElementById("nThal1").value;
updateOne(val01, 0);

// Check for changes in the inputs and update output bar
d3.select("#nSex1").on("input", function () {
    updateOne(+this.value, 1);
});
d3.select("#nSex2").on("input", function () {
    updateOne(+this.value, 1);
});
d3.select("#nRestbp1").on("input", function () {
    updateOne(+this.value, 2);
});
d3.select("#nRestbp2").on("input", function () {
    updateOne(+this.value, 2);
});
d3.select("#nThalach1").on("input", function () {
    updateOne(+this.value, 3);
});
d3.select("#nThalach2").on("input", function () {
    updateOne(+this.value, 3);
});
d3.select("#nCa1").on("input", function () {
    updateOne(+this.value, 4);
});
d3.select("#nCa2").on("input", function () {
    updateOne(+this.value, 4);
});
d3.select("#nCp1").on("input", function () {
    updateOne(+this.value, 5);
});
d3.select("#nCp2").on("input", function () {
    updateOne(+this.value, 5);
});
d3.select("#nSlope1").on("input", function () {
    updateOne(+this.value, 6);
});
d3.select("#nSlope2").on("input", function () {
    updateOne(+this.value, 6);
});
d3.select("#nThal1").on("input", function () {
    updateOne(+this.value, 7);
});
d3.select("#nThal2").on("input", function () {
    updateOne(+this.value, 7);
});

// Update the heart disease probability
function updateOne(value, index) {

    if (index === 1) {
        val01 = value;
    } else if (index === 2) {
        val02 = value;
    } else if (index === 3) {
        val03 = value;
    } else if (index === 4) {
        val04 = value;
    } else if (index === 5) {
        val05 = value;
    } else if (index === 6) {
        val06 = value;
    } else if (index === 7) {
        val07 = value;
    } else if (index === -1) {
        // Set everything back to default state:
        val01 = document.getElementById("nSex1").defaultValue;
        document.getElementById("nSex1").value = val01;
        document.getElementById("nSex2").value = val01;
        val02 = document.getElementById("nRestbp1").defaultValue;
        document.getElementById("nRestbp1").value = val02;
        document.getElementById("nRestbp2").value = val02;
        val03 = document.getElementById("nThalach1").defaultValue;
        document.getElementById("nThalach1").value = val03;
        document.getElementById("nThalach2").value = val03;
        val04 = document.getElementById("nCa1").defaultValue;
        document.getElementById("nCa1").value = val04;
        document.getElementById("nCa2").value = val04;
        val05 = document.getElementById("nCp1").defaultValue;
        document.getElementById("nCp1").value = val05;
        document.getElementById("nCp2").value = val05;
        val06 = document.getElementById("nSlope1").defaultValue;
        document.getElementById("nSlope1").value = val06;
        document.getElementById("nSlope2").value = val06;
        val07 = document.getElementById("nThal1").defaultValue;
        document.getElementById("nThal1").value = val07;
        document.getElementById("nThal2").value = val07;
    }

    // Standardize the continuous features:
    let srbp_val = (val02 - 131.7157) / 17.7478;
    let sthalach_val = (val03 - 149.3278) / 23.1211;
    let sca_val = (val04 - 0.6722) / 3.0;

    // Disentangle the categorical features:
    let cp_contr = 0.0;
    if (val05 === 1) {
        cp_contr = -2.2318;
    } else if (val05 === 2) {
        cp_contr = -1.2681;
    } else if (val05 === 3) {
        cp_contr = -2.1124;
    }
    let slope_contr = 0.0;
    if (val06 === 1) {
        slope_contr = -1.4726;
    }
    let thal_contr = 0.0;
    if (val07 === 1) {
        thal_contr = 1.5009;
    }

    // Compute log-odds, then probability:
    let scprod = 1.4361 * val01 + 0.4415 * srbp_val - 0.4431 * sthalach_val + 3.7984 * sca_val + cp_contr + slope_contr + thal_contr;
    let drec = 1.0 / (1.0 + Math.exp(-scprod));
    let drecs = height0 * drec;
    drec *= 100;

    // Update plot:
    let rcolor = percentToRGB(drec);
    holder.select("rect")
        .attr("y", y0 + height0 - drecs)
        .attr("height", drecs)
        .style("fill", rcolor);

    holder.select("text")
        .text(function () {
            return parseFloat(Math.round(drec * 100) / 100).toFixed(2) + "%";
        });

}

function percentToRGB(percent) {
    if (percent === 100) {
        percent = 99
    }
    let r, g, b;

    if (percent < 50) {
        // green to yellow
        r = Math.floor(255 * (percent / 50));
        g = 255;

    } else {
        // yellow to red
        r = 255;
        g = Math.floor(255 * ((50 - percent % 50) / 50));
    }
    b = 0;

    return "rgb(" + r + "," + g + "," + b + ")";
}

function updateSliderValue(value, targetId) {
    const sliderElement = document.getElementById(targetId);
    if (sliderElement) {
        if (sliderElement.value !== value) { // Check if the new value is different
            sliderElement.value = value;
            sliderElement.dispatchEvent(new Event('input', { bubbles: true }));
        }
    } else {
        console.error(`Slider element with ID ${targetId} not found.`);
    }
}

function updateNumberInputValue(value, targetId) {
    const inputElement = document.getElementById(targetId);
    if (inputElement) {
        if (inputElement.value !== value) { // Check if the new value is different
            inputElement.value = value;
            inputElement.dispatchEvent(new Event('input', { bubbles: true }));
        }
    } else {
        console.error(`Input element with ID ${targetId} not found.`);
    }
}


function resetValues() {
    for (const key in defaultValues) {
        document.getElementById(`${key}1`).value = defaultValues[key];
        document.getElementById(`${key}2`).value = defaultValues[key];
    }
}