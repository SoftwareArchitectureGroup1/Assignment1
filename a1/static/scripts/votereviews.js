 $(document).ready(function() {
            $('.btn-upvote').on('click', function() {
                var reviewId = $(this).data('review-id');
                $.ajax({
                    url: '/upvote_review/' + reviewId + '/',
                    type: 'GET',
                    dataType: 'json',
                    success: function(data) {
                        $('#upvotes-' + reviewId).text(data.upvotes);
                        if (data.upvotes > 0) {
                            $('.btn-upvote[data-review-id="' + reviewId + '"] i').addClass('filled');
                        } else {
                            $('.btn-upvote[data-review-id="' + reviewId + '"] i').removeClass('filled');
                        }
                        location.reload()
                    }
                });
            });

            $('.btn-downvote').on('click', function() {
                var reviewId = $(this).data('review-id');
                $.ajax({
                    url: '/downvote_review/' + reviewId + '/',
                    type: 'GET',
                    dataType: 'json',
                    success: function(data) {
                        $('#downvotes-' + reviewId).text(data.downvotes);
                        if (data.downvotes > 0) {
                            $('.btn-downvote[data-review-id="' + reviewId + '"] i').addClass('filled');
                        } else {
                            $('.btn-downvote[data-review-id="' + reviewId + '"] i').removeClass('filled');
                        }
                        location.reload()
                    }
                });
            });
        });