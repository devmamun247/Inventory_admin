
// let sitebarmenu = document.querySelectorAll(".nav-link_aside");

// for (let i = 0; i < sitebarmenu.length; i++) {
//   sitebarmenu[i].addEventListener("click", function () {
//     let activeClas = document.querySelector(".active");
//     if (activeClas && activeClas.classList.contains("active")) {
//       activeClas.classList.remove("active");
//     }
//     this.classList.add("active");
//   });
// }


// Popup open for predict btn
let predic_btn = document.querySelectorAll(".popup_open");
for (let i = 0; i < predic_btn.length; i++) {
  predic_btn[i].addEventListener("click", function () {
    let popup = document.querySelector(".symtomp_popup");
    popup.classList.add("display_block");
  });
}

// Symtomp popup btn close
let popup_close = document.querySelectorAll(".dep_popup_close");
for (let i = 0; i < popup_close.length; i++) {
  popup_close[i].addEventListener("click", function () {
    let popup = this.parentElement.parentElement.parentElement;
    popup.classList.remove("display_block");
  });
}




// Bootstrap live search
 $(document).ready(function () {
   $(
     "#selectBox1, #selectBox2, #selectBox3, #selectBox4, #selectBox5, #selectBox6"
   ).select2();
   $(
     "#selectBox1, #selectBox2, #selectBox3, #selectBox4, #selectBox5, #selectBox6"
   ).select2({
     width: "100%",
   });

  //  Datepicker;
  //  $("#fullCalendar").fullCalendar({
  //    header: {
  //      left: "prev,next today",
  //      center: "title",
  //      right: "month,agendaWeek,agendaDay",
  //    },
  //    defaultView: "month",
  //    events: [
  //      {
  //        title: "Event 1",
  //        start: "2024-01-31",
  //      },
  //      {
  //        title: "Event 2",
  //        start: "2024-02-01",
  //        end: "2024-02-03",
  //      },
  //      // Add more events as needed
  //    ],
  //  });


// Sub menu toggle
  $(".sub_menu_head").click(function(){
    $(this).closest(".sub_manu_main").toggleClass("bordered");
    $(this).toggleClass("bg_whitw");
    $(this).next(".sub_menu_list").toggleClass("display_block");
  });


  $(".nav-link_aside").click(function(){
    $(".nav-link_aside").removeClass("active");
    $(this).addClass("active");
    $(this).find(".right_icon_sub").toggleClass("rotate_0");
  });

 });

 

$(document).ready(function(){
  // Location Search
  $(".location_select").selectpicker();
});



// user logout btn opne
$(document).ready(function(){
  $(".user_pannel").click(function () {
    $(".user_account").toggleClass("display_block");
  });
});



