$(document).ready(function () {
    $('.delete-sale-btn').click(function () {
        console.log("entered");
        const saleId = $(this).data('sale-id');
        if (confirm('Are you sure you want to delete this sale?')) {
            const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                type: 'DELETE',
                url: `/deletesale/${saleId}/`,
                headers: { 'X-CSRFToken': csrfToken },
                success: function (response) {
                    alert(response.message);
                    location.reload();
                },
                error: function (response) {
                    alert('Error deleting sale.');
                }
            });
        }
    });
});