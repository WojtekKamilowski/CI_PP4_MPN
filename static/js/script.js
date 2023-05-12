// Close messages after 3 seconds - from CI_PP4_the_diplomat;
$(document).ready(function () {
    setTimeout(function () {
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
});

// Changes color of create_list button when mouse on
$("#create_list").on("mouseenter", function () {
    $("#create_list").css("background-color", "#CCC731");
});

// Changes color of create_list button when mouse out
$("#create_list").on("mouseout", function () {
    $("#create_list").css("background-color", "#55D54E");
});

// Changes color of create_storage button when mouse on
$("#create_storage").on("mouseenter", function () {
    $("#create_storage").css("background-color", "#CCC731");
});

// Changes color of create_storage button when mouse out
$("#create_storage").on("mouseout", function () {
    $("#create_storage").css("background-color", "#55D54E");
});

// Changes color of create_item button when mouse on
$("#create_item").on("mouseenter", function () {
    $("#create_item").css("background-color", "#CCC731");
});

// Changes color of create_item button when mouse out
$("#create_item").on("mouseout", function () {
    $("#create_item").css("background-color", "#55D54E");
});
