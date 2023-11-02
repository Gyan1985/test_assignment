
    const searchInput = document.getElementById('searchInput');
    const clickInput =document.getElementById('searchIcon');
    const dataTable = document.getElementById('data-table');

    const tbody = dataTable.querySelector('tbody');

    clickInput.addEventListener('click', function() {
        fetchData(searchInput.value);
    });

    async function fetchData(searchValue) {
        let value = searchValue !== undefined ?searchValue:""
        try {
            const response = await fetch(`http://0.0.0.0:8000/api/inventory?search=${value}`); // Replace with your API URL
            const data = await response.json();

            tbody.innerHTML = '';

            data.forEach(item => {
                const row = document.createElement('tr');
                row.onclick = function () {
                    window.location.href = `http://0.0.0.0:8000/inventory/${item.id}`
                }
                row.innerHTML = `
                    <td>${item.name}</td>
                    <td>${item.availability}</td>
                    <td>${item.supplier.name}</td>
                `;
                tbody.appendChild(row);
            });
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    fetchData();

