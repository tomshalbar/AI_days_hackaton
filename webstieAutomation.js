// Function to fetch JSON data and populate the table
async function populateTable() {
    try {
        // Fetch the JSON file
        const response = await fetch('../processedData.json');
        const data = await response.json();

        // Extract data arrays
        const titles = data.all_disasters_keys;
        const contents = data.all_disaster_content;

        // Reference to the table body
        const tableBody = document.querySelector('.table__body');

        // Clear existing rows (optional)
        tableBody.innerHTML = '';

        // Loop through the data and create table rows
        for (let i = 0; i < titles.length; i++) {
            const row = document.createElement('tr');
            row.classList.add('table__row');

            // Checkbox cell
            const checkboxCell = document.createElement('td');
            checkboxCell.classList.add('table__cell', 'table__cell--checkbox', 'table__cell--no-wrap');
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkboxCell.appendChild(checkbox);

            // Title cell
            const titleCell = document.createElement('td');
            titleCell.classList.add('UserTable__name', 'table__cell', 'table__cell--no-wrap');
            titleCell.textContent = titles[i];

            // Content cell
            const contentCell = document.createElement('td');
            contentCell.classList.add('table__cell', 'table__cell--remainder');
            contentCell.textContent = contents[i];

            // Append cells to the row
            row.appendChild(checkboxCell);
            row.appendChild(titleCell);
            row.appendChild(contentCell);

            // Append row to the table body
            tableBody.appendChild(row);
        }
    } catch (error) {
        console.error("Error loading or parsing JSON file:", error);
    }
}

// Call the populateTable function when the page loads
window.addEventListener('DOMContentLoaded', populateTable);

// fetch("../processedData.json")
//     .then(res => res.json()) 
//     .then(data => {
//         data.forEach(key => {
            
//         });
//     }

// console.log(value)



// function generateContent() {
//     var output = document.getElementById('disaster-title');
//     output.innerHTML = 'new content';
// }

