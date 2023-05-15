// Close messages after 3 seconds - from CI_PP4_the_diplomat;
$(document).ready(function () {
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
});

// Changes color of create_box buttons when mouse on
$(".create_box").on("mouseenter", function () {
    $(".create_box").css("background-color", "#CCC731");
});

// Changes color of create_box buttons when mouse out
$(".create_box").on("mouseout", function () {
    $(".create_box").css("background-color", "#55D54E");
});

// Hihghlights items table row when mouse enters
$(".item_details").on("mouseenter", function () {
    $(this).addClass("row_highlight");
});

// Removes hihghlight of items table row when mouse leaves
$(".item_details").on("mouseout", function () {
    $(this).removeClass("row_highlight");
});
