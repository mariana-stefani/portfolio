/**
 * Creates Progress Circle - Tutorial from https://bootstrapious.com/p/circular-progress-bar
 */
$(function () {
  $(".progress").each(function () {
    let value = $(this).attr("data-value");
    let left = $(this).find(".progress-left .progress-bar");
    let right = $(this).find(".progress-right .progress-bar");

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
let navbar = $(".navbar");

$(window).scroll(function () {
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
 * Display toast message when login fails
 */
$(".toast").toast("show");
