$(document).ready(function () {
// Insert new record
  $("#insert_confirm").on("click", function (event) {
    event.preventDefault();
    if ($("#username").val() == "") {
      alert("Name is required");
    } else if ($("#password").val() == "") {
      alert("Password is required");
    } else if ($("#email").val() == "") {
      alert("Email is required");
    } else {
      $.ajax({
        url: "/insert",
        method: "POST",
        data: {
          username: $("#_username").val(),
          password: $("#_password").val(),
          email: $("#_email").val(),
          role: $("#_role").val(),
        },
        beforeSend: function () {
          $("#insert_confirm").val("Inserting");
        },
        success: function (data) {
          $("#add_data_Modal").modal("hide");
          if (data == "success") {
            window.location.href = "/pythonlogin/home";
          }
        },
      });
    }
  });
// View record
  $(document).on("click", ".view_data", function () {
    var id = $(this).attr("id");
    $.ajax({
      url: "/select",
      method: "POST",
      data: { id: id },
      success: function (data) {
        $("#edit_data_Modal").modal("show");
        var data_rs = JSON.parse(data);
        $("#edit_id").val(data_rs["id"]);
        $("#edit_username").val(data_rs["username"]);
        $("#edit_email").val(data_rs["email"]);
        $("#edit_password").val(data_rs["password"]);
        $("#edit_role").val(data_rs["role"]);
      },
    });
  });
//   Save edit results
  $(document).on("click", ".save_edit", function () {
    var id = $("#edit_id").val();
    $.ajax({
      url: "/update",
      method: "POST",
      data: {
        username: $("#edit_username").val(),
        password: $("#edit_password").val(),
        email: $("#edit_email").val(),
        role: $("#edit_role").val(),
        id: id,
      },
      success: function (data) {
        $("#edit_data_Modal").modal("hide");
        if (data == "success") {
          window.location.href = "/pythonlogin/home";
        }
      },
    });
  });
  

  $(document).on("click", ".del_data", function () {
    var id = $(this).attr("id");
    $(".del_").attr("id", id);
  });
//   Del existed record
  $(document).on("click", ".del_", function () {
    var id = $(this).attr("id");
    $.ajax({
      url: "/delete",
      method: "POST",
      data: { id: id },
      success: function (data) {
        $("#del_confirm").modal("hide");
        if (data == "success") {
          window.location.href = "/pythonlogin/home";
        }
      },
    });
  });
});
