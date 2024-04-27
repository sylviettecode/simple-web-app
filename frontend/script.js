fetch('http://10.0.0.16:5000/products')           .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('table_body');
                data.forEach(product => {
                    const row = document.createElement('tr');

                    const idCell = document.createElement('td');
                    idCell.textContent = product.product_id;
                    row.appendChild(idCell);

                    const nameCell = document.createElement('td');
                    nameCell.textContent = product.product_name;
                    row.appendChild(nameCell);

                    const priceCell = document.createElement('td');
                    priceCell.textContent = product.product_price;
                    row.appendChild(priceCell);

                    const countCell = document.createElement('td');
                    countCell.textContent = product.product_count;
                    row.appendChild(countCell);

                    tableBody.appendChild(row);
                });
            })
            .catch(error => console.error('Error fetching data:', error));