document.addEventListener("DOMContentLoaded", function () {
    const booksCountFilter = document.getElementById("books_count-filter");
    const avgScoreFilter = document.getElementById("average_score-filter");
    const totalSalesFilter = document.getElementById("total_sales-filter");
    const tableBody = document.querySelector("tbody");

    function updateTable() {
        const selectedBooksCount = booksCountFilter.value;
        const selectedAvgScore = avgScoreFilter.value;
        const selectedTotalSales = totalSalesFilter.value;
        const url = `/indexauthors/?books_count=${selectedBooksCount}&average_score=${selectedAvgScore}&total_sales=${selectedTotalSales}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Clear the table
                tableBody.innerHTML = "";

                data.forEach(author => {
                    const row = `<tr>
                        <td><a href="{% url 'detail-author-view' pk=author.id %}">${author.name}</a></td>
                        <td>${author.country}</td>
                        <td>${author.birthday}</td>
                        <td>${author.description}</td>
                        <td>${author.books_count}</td>
                        <td>${author.average_score}</td>
                        <td>${author.total_sales}</td>
                        <td>
                            <a href="{% url 'edit-author' author_id=author.id %}" class="btn btn-info btn-sm">Edit</a>
                        </td>
                        <td>
                            <button class="btn btn-danger btn-sm delete-author-btn" data-author-id="${author.id}">Delete</button>
                        </td>
                    </tr>`;
                    tableBody.innerHTML += row;
                });
            })
            .catch(error => console.error("Error fetching data:", error));
    }

    // Attach event listeners to the filters
    booksCountFilter.addEventListener("change", updateTable);
    avgScoreFilter.addEventListener("change", updateTable);
    totalSalesFilter.addEventListener("change", updateTable);

    updateTable();
});