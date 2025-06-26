document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('form.delete-reservation').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!confirm('Are you sure you want to delete this booking?')) {
                event.preventDefault();
            }
        });
    });
});
