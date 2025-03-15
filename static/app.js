document.getElementById('generate-btn').addEventListener('click', function () {
    const codeInput = document.getElementById('code-input').value;

    if (!codeInput) {
        alert('Please enter some code to generate comments.');
        return;
    }

    // Send the code to the backend API
    fetch('/generate_comment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: codeInput }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('commented-code').value = data.commented_code;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while generating comments.');
    });
});
