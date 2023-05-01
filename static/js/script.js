// Close messages after 3 seconds - from CI_PP4_the_diplomat;
$(document).ready(function () {
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
});
