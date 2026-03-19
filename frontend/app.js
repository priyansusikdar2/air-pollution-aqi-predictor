function getAQICategory(aqi) {
    if (aqi <= 50) return ["Good 🌿", "#2ecc71"];
    if (aqi <= 100) return ["Moderate 🙂", "#f1c40f"];
    if (aqi <= 150) return ["Unhealthy for Sensitive 😷", "#e67e22"];
    if (aqi <= 200) return ["Unhealthy 🚫", "#e74c3c"];
    if (aqi <= 300) return ["Very Unhealthy ☠️", "#8e44ad"];
    return ["Hazardous 💀", "#2c3e50"];
}

async function predictAQI() {

    const resultBox = document.getElementById("resultBox");
    const aqiValue = document.getElementById("aqiValue");
    const aqiCategory = document.getElementById("aqiCategory");
    const errorBox = document.getElementById("error");

    resultBox.classList.add("hidden");
    errorBox.innerText = "";

    try {

        // ✅ GET RAW VALUES
        const pm25 = document.getElementById("pm25").value;
        const pm10 = document.getElementById("pm10").value;
        const no2 = document.getElementById("no2").value;
        const so2 = document.getElementById("so2").value;
        const co = document.getElementById("co").value;

        console.log("🚨 INPUT:", pm25, pm10, no2, so2, co);

        // ✅ STRICT VALIDATION (CRITICAL FIX)
        if (
            pm25 === "" ||
            pm10 === "" ||
            no2 === "" ||
            so2 === "" ||
            co === ""
        ) {
            throw new Error("Please fill all fields");
        }

        // ✅ SAFE PARSE AFTER VALIDATION
        const data = {
            pm2_5: parseFloat(pm25),
            pm10: parseFloat(pm10),
            no2: parseFloat(no2),
            so2: parseFloat(so2),
            co: parseFloat(co)
        };

        console.log("🚀 SENDING:", data);

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("API not responding");
        }

        const result = await response.json();

        console.log("📥 RESPONSE:", result);

        if (!result.predicted_aqi) {
            throw new Error("Invalid response from server");
        }

        const aqi = result.predicted_aqi;
        const [category, color] = getAQICategory(aqi);

        aqiValue.innerText = "AQI: " + aqi;
        aqiCategory.innerText = category;

        resultBox.style.background = color;
        resultBox.classList.remove("hidden");

    } catch (err) {
        console.error(err);
        errorBox.innerText = "❌ " + err.message;
    }
}