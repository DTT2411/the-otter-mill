document.addEventListener('DOMContentLoaded', function() {
    // Confirmation check for delete button(s)
    document.querySelectorAll('form.delete-reservation').forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!confirm('Are you sure you want to delete this booking?')) {
                event.preventDefault();
            }
        });
    });
    // Confirmation check for edit button(s)
    document.querySelectorAll('a.edit-reservation').forEach(function(link) {
        link.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to change this booking?')) {
                event.preventDefault();
            }
        });
    });
});
