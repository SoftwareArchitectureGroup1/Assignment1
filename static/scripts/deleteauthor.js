
    $(document).ready(function () {
    $('.delete-author-btn').click(function () {
        console.log("entered");
        const authorId = $(this).data('author-id');
        if (confirm('Are you sure you want to delete this author?')) {
            const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                type: 'POST',
                url: `/indexauthors`,
                headers: { 'X-CSRFToken': csrfToken },
                data: {
                author_id: authorId
                },
                success: function (response) {
                    alert(response.message);
                    location.reload();
                },
                error: function (response) {
                    alert('Error deleting author.');
                }
            });
        }
    });
});
