document.getElementById("predictForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("resultado").classList.add("hidden");
    document.getElementById("error").classList.add("hidden");

    const divSelecionada = document.getElementById("division").value;

    const payload = {
        year: parseFloat(document.getElementById("year").value),
        max_temp: parseFloat(document.getElementById("max_temp").value),
        min_temp: parseFloat(document.getElementById("min_temp").value),
        max_wind_speed: parseFloat(document.getElementById("max_wind_speed").value),
        min_wind_speed: parseFloat(document.getElementById("min_wind_speed").value),
        precipitation: parseFloat(document.getElementById("precipitation").value),
        par: parseFloat(document.getElementById("par").value),
        root_soil_wetness: parseFloat(document.getElementById("root_soil_wetness").value),
        surface_soil_wetness: parseFloat(document.getElementById("surface_soil_wetness").value),
        humidity: parseFloat(document.getElementById("humidity").value),
        earth_skin_temp: parseFloat(document.getElementById("earth_skin_temp").value),
        div_chittagong: divSelecionada === "Chittagong",
        div_khulna: divSelecionada === "Khulna",
        div_rajshahi: divSelecionada === "Rajshahi",
        div_rangpur: divSelecionada === "Rangpur",
        div_sylhet: divSelecionada === "Sylhet"
    };

    try {
        const response = await fetch("http://localhost:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        
        const data = await response.json();
        document.getElementById("loading").classList.add("hidden");

        if (response.ok) {
            const elRes = document.getElementById("resultado");
            elRes.innerText = `Rendimento Estimado: ${data.crop_yield_previsto} Ton/Hectare`;
            elRes.classList.remove("hidden");
        } else {
            throw new Error(data.detail || "Erro de conexão com o servidor.");
        }
    } catch (err) {
        document.getElementById("loading").classList.add("hidden");
        const errDiv = document.getElementById("error");
        errDiv.innerText = err.message;
        errDiv.classList.remove("hidden");
    }
});