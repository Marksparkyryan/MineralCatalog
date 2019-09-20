// make back-to-top button appear/dissappear 

arrow = document.getElementById("back_to_top");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 375 || document.documentElement.scrollTop > 375) {
    arrow.style.display = "block";
  } else {
    arrow.style.display = "none";
  }
}
