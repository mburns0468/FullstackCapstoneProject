document.getElementById('drink-search').addEventListener('submit', function(event) {
  event.preventDefault();

  // Get form data
  const searchInput = document.getElementById('dSearch').value;

  // setting API gateway endpoint to variable
  const apiGatewayEndpoint = 'https://15aw1pweoa.execute-api.us-east-1.amazonaws.com/drinksearchpost';

  // Make a POST request to Lambda through API gateway endpoint
  fetch(apiGatewayEndpoint, {
      method: 'POST',
      body: JSON.stringify({ searchInput }),
      headers: {
          'Content-Type': 'application/json',
          // Add any AWS authentication headers here if required
      }
  })
  .then(response => response.text())
  .then(htmlContent => {
  // Handle the API response here and update your web page with the data
      displayHTML(htmlContent);
  })    
  .catch(error => console.error(error));
  
  function displayHTML(htmlContent) {
          const apiResponseContainer = document.getElementById('resultContainer');
          apiResponseContainer.innerHTML = htmlContent;
      }
});
