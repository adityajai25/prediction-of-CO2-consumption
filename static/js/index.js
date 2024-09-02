document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const predictionText = doc.getElementById('prediction-text');
        const resultClass = predictionText ? predictionText.querySelector('p').className : '';
        
        document.getElementById('prediction-text').innerHTML = doc.getElementById('prediction-text').innerHTML;
        document.getElementById('table').style.display = 'block';
        document.getElementById('info').style.display = 'none';
        document.querySelector('#prediction-text p').className = resultClass;
    });
});
