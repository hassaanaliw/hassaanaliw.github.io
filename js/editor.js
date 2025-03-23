document.addEventListener('DOMContentLoaded', () => {
    const content = document.querySelector('.about-me .content');
    
    // Handle focus
    content.addEventListener('focus', () => {
        // Remove syntax highlighting when focused
        content.classList.add('editing');
    });

    // Handle blur
    content.addEventListener('blur', () => {
        content.classList.remove('editing');
        
        // If content is empty, restore original
        if (!content.textContent.trim()) {
            content.innerHTML = content.dataset.original;
        }
    });

    // Handle keydown
    content.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            content.blur();
            content.innerHTML = content.dataset.original;
        }
    });
}); 