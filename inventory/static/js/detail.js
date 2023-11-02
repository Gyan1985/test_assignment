window.onload = function() {
    const backButton = document.getElementById('back');
    backButton.addEventListener('click', function() {
        history.back();
    });
}