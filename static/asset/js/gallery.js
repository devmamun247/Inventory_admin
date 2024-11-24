

$(document).ready(function(){
  // Gallery Edit modal start
  //   modal open
  $(".admin_edit").click(function () {
    $(this).next().css({ transform: "scale(1)" });
  });

  //   Crose button click for close
  $(".AGMclose").click(function () {
    $(this).closest(".Agallery_modal").css({ transform: "scale(0)" });
  });

  //   Close by click on submit btn
  $(".AGMS").click(function (e) {
    e.preventDefault();
    $(this).closest(".Agallery_modal").css({ transform: "scale(0)" });
  });

  // Gallery Edit modal end

  //   Gallery delete start
  $(".admin_delete").click(function () {
    $(this).next().css({ transform: "scale(1)" });
  });

  //   Close by click on Close btn
  $(".AGMC").click(function (e) {
    e.preventDefault();
    $(this).closest(".Agallery_modal").css({ transform: "scale(0)" });
  });

  //   Close by click on Delete btn
  $(".AGMD").click(function (e) {
    e.preventDefault();
    $(this).closest(".Agallery_modal").css({ transform: "scale(0)" });
  });

  // Live search
  $("#searchInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#tableBody tr").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});