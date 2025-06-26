document.addEventListener('DOMContentLoaded', function() {
    // Add confirmation for delete buttons
    document.querySelectorAll('form.delete-reservation').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!confirm('Are you sure you want to delete this booking?')) {
                event.preventDefault();
            }
    // Add confirmation for edit buttons
    document.querySelectorAll('a.edit-reservation').forEach(function(link) {
        link.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to edit this booking?')) {
                event.preventDefault();
            }
        });
    });
});
    });
});
