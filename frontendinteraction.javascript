document.getElementById("runButton").addEventListener("click", async () => {
    const code = document.getElementById("codeEditor").value;
    const response = await fetch("/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code })
    });
    const result = await response.json();
    document.getElementById("output").innerText = result.output;
});
