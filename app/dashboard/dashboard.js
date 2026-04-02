async function loadData() {

    const report = await fetch("/ai/system-report");
    const reportData = await report.json();
    document.getElementById("systemReport").textContent =
        JSON.stringify(reportData, null, 2);

    const control = await fetch("/ai/control-center");
    const controlData = await control.json();
    document.getElementById("controlCenter").textContent =
        JSON.stringify(controlData, null, 2);

    const business = await fetch("/ai/business-intelligence");
    const businessData = await business.json();
    document.getElementById("businessIntel").textContent =
        JSON.stringify(businessData, null, 2);
}

loadData();