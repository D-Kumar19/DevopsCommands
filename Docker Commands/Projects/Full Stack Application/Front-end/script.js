document.getElementById('submission-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        dob: document.getElementById('dob').value
    };

    fetch('http://localhost:3000/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert('Submission successful!');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('There was an error with your submission.');
    });
});
