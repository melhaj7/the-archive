document.addEventListener('DOMContentLoaded', function () {

    const booksearchInput = document.getElementById('booksearch');
    const searchButton = document.getElementById('search-button');
    const searchResultsContainer = document.getElementById('search-results');
  
    searchButton.addEventListener('click', function () {
      const query = booksearchInput.value.trim();
  
      if (query) {
        fetch(`/search?q=${encodeURIComponent(query)}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(response => response.json())  // Parse the JSON response
        .then(data => {
          searchResultsContainer.innerHTML = '';  // Clear previous results
          
          // Check if there are any books in the response
          if (data.docs && data.docs.length > 0) {
            // Loop through the results and display them
            data.docs.forEach(book => {
              const bookElement = document.createElement('div');
              bookElement.innerHTML = `
                <h3>${book.title}</h3>
                <p>Author: ${book.author_name ? book.author_name.join(', ') : 'N/A'}</p>
                <p>First Published: ${book.first_publish_year || 'Unknown'}</p>
              `;
              searchResultsContainer.appendChild(bookElement);
            });
          } else {
            searchResultsContainer.innerHTML = '<p>No results found.</p>';
          }
        })
        .catch(error => {
          searchResultsContainer.innerHTML = '<p>Error fetching data. Please try again later.</p>';
        });
      } else {
        searchResultsContainer.innerHTML = '<p>Please enter a search term.</p>';
      }
    });
  
  });
  