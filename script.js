document.getElementById('imageForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const promptValue = document.getElementById('prompt').value;
    const stepsValue = document.getElementById('steps').value;

    fetch('/generate-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: promptValue,
            steps: parseInt(stepsValue)
        })
    })
    .then(response => response.json())
    .then(data => {
        const outputImage = document.getElementById('outputImage');
        outputImage.src = 'data:image/png;base64,' + data.image;
        outputImage.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
