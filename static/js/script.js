//Progress Circle
// Tutorial from https://bootstrapious.com/p/circular-progress-bar

$(function () {
  $(".progress").each(function () {
    var value = $(this).attr("data-value");
    var left = $(this).find(".progress-left .progress-bar");
    var right = $(this).find(".progress-right .progress-bar");
    var bar = $(this).find(".progress");

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

  function percentageToDegrees(percentage) {
    return (percentage / 100) * 360;
  }
});

//Email JS

$(function () {
  emailjs.init("user_ihMVh8GieFlqswQcnywX0");
})();

function sendMail(contactForm) {
  email
    .send("gmail", "mariana", {
      "from _name": contactForm.name.value,
      from_email: contactForm.emailaddress.value,
      contact_request: contactForm.contactsummary.value,
    })
    .then(
      function (response) {
        console.log("success", response);
      },
      function (error) {
        console.log("failed", error);
      }
    );
  return false;
}
