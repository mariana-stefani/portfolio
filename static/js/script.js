/**
 * Creates Progress Circle - Tutorial from https://bootstrapious.com/p/circular-progress-bar
 */
$(function () {
  $(".progress").each(function () {
    let value = $(this).attr("data-value");
    let left = $(this).find(".progress-left .progress-circle");
    let right = $(this).find(".progress-right .progress-circle");

    if (value > 0) {
      if (value <= 50) {
        right.css("transform", "rotate(" + percentageToDegrees(value) + "deg)");
      } else {
        right.css("transform", "rotate(180deg)");
        left.css(
          "transform",
          "rotate(" + percentageToDegrees(value - 50) + "deg)"
        );
      }
    }
  });

  /**
   * Transform the percentage to degrees
   * @param {number} percentage
   */
  function percentageToDegrees(percentage) {
    return (percentage / 100) * 360;
  }
});

/**
 * Sends email through the contact form
 * @param {object} contactForm
 */
function sendMail(contactForm) {
  emailjs
    .send("gmail", "mariana", {
      from_name: contactForm.name.value,
      from_email: contactForm.emailaddress.value,
      contact_request: contactForm.contactsummary.value,
    })
    .then(
      function (response) {
        console.log("SUCCESS", response);
      },
      function (error) {
        console.log("FAILED", error);
      }
    );
  // Show alert
  document.querySelector(".email-alert").style.display = "block";

  // Hide alert after 4 seconds
  setTimeout(function () {
    document.querySelector(".email-alert").style.display = "none";
  }, 4000);

  // Clear form
  document.getElementById("contact-form").reset();

  return false;
}

/**
 * When user scroll an ID is added to the nav to add background-color
 */

$(window).scroll(function () {
  let navbar = $(".navbar");
  if ($(window).scrollTop() > 0) {
    navbar.addClass("nav-show");
  } else {
    navbar.removeClass("nav-show");
  }
});

/**
 * Initializes emailjs
 */
(function () {
  emailjs.init("user_ihMVh8GieFlqswQcnywX0");
})();

/**
 * Sends email when button is clicked
 */
$("#contact-form").submit(function (e) {
  e.preventDefault();
  sendMail(this);
});

/**
 * Display toast message
 */
$(".toast").toast("show");

/**
 * Highlight nav link
 */
$(".menu a").each(function () {
  $(".menu a").on("click", function () {
    $(".menu a").removeClass("active");
    $(this).addClass("active");
  });
});
