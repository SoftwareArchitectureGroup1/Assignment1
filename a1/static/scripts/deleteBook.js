$(document).ready(function () {
    $('.delete-book-btn').click(function () {
        console.log("entered");
        const bookId = $(this).data('book-id');
        if (confirm('Are you sure you want to delete this book?')) {
            const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                type: 'DELETE',
                url: `/book/delete/${bookId}`,
                headers: { 'X-CSRFToken': csrfToken },
                success: function (response) {
                    alert(response.message);
                    location.reload();
                },
                error: function (response) {
                    alert('Error deleting book.');
                }
            });
        }
    });
});
