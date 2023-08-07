$(document).ready(function () {
    $('.delete-review-btn').click(function () {
        console.log("entered");
        const reviewId = $(this).data('review-id');
        if (confirm('Are you sure you want to delete this review?')) {
            const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                type: 'DELETE',
                url: `/deletereview/${reviewId}/`,
                headers: { 'X-CSRFToken': csrfToken },
                success: function (response) {
                    alert(response.message);
                    location.reload();
                },
                error: function (response) {
                    alert('Error deleting review.');
                }
            });
        }
    });
});