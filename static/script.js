document.getElementById("submit").addEventListener("click", function() {
    let hoursStudied=document.getElementById("hoursStudied").value;
    let previousMarks=document.getElementById("previousMarks").value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            hoursStudied: parseFloat(hoursStudied),
            previousMarks: parseFloat(previousMarks),
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("marksOutput").value = data.predictedMarks.toFixed(0);
    });
});
