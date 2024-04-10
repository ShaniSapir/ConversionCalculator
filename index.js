document.getElementById("conversionForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    const conversionType = document.getElementById("conversionType").value;
    const amount = document.getElementById("amount").value;

    fetch(`/convert/${conversionType}/${amount}`)
        .then(response => response.text())
        .then(result => {
            document.getElementById("result").textContent = result;
        })
        .catch(error => console.error('Error:', error));
});
