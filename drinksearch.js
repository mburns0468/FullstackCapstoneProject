document.getElementById('drink-search').addEventListener('submit', function (event) {
    event.preventDefault();
    searchCocktail();
  });
  
  async function searchCocktail() {
    const searchTerm = document.getElementById('dSearch').value;
    
    const url = `https://the-cocktail-db.p.rapidapi.com/search.php?s=${searchTerm}`;
    const options = {
      method: 'GET',
      headers: {
        'X-RapidAPI-Key': '29c38d7341msh7a15b3f6f2fbf49p192425jsn6de4d45dc56e',
        'X-RapidAPI-Host': 'the-cocktail-db.p.rapidapi.com'
      }
    };
  
    try {
      const response = await fetch(url, options);
      const data = await response.json();
  
      displayResults(data);
    } catch (error) {
      console.error(error);
    }
  }
  
  function displayResults(data) {
    const resultsContainer = document.getElementById('cocktail-results');
    resultsContainer.innerHTML = '';
  
    if (data.drinks) {
      data.drinks.forEach(drink => {
        const drinkDetails = `
          <h2>${drink.strDrink}</h2>
          <p><strong>Instructions:</strong> ${drink.strInstructions}</p>
          <p><strong>Glass:</strong> ${drink.strGlass}</p>
          <p><strong>Ingredients:</strong></p>
          <ul>
            ${getIngredientsList(drink)}
          </ul>
          <hr>
        `;
        resultsContainer.innerHTML += drinkDetails;
      });
    } else {
      resultsContainer.innerHTML = '<p>No results found.</p>';
    }
  }
  
  function getIngredientsList(drink) {
    let ingredientsList = '';
    for (let i = 1; i <= 15; i++) {
      const ingredient = drink[`strIngredient${i}`];
      const measure = drink[`strMeasure${i}`];
  
      if (ingredient && measure) {
        ingredientsList += `<li>${measure} ${ingredient}</li>`;
      } else if (ingredient) {
        ingredientsList += `<li>${ingredient}</li>`;
      }
    }
    return ingredientsList;
  }