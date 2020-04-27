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

function sendMail(contactForm) {
  emailjs.send("gmail", "mariana", {
      "from_name": contactForm.name.value,
      "from_email": contactForm.emailaddress.value,
      "contact_request": contactForm.contactsummary.value
  })
  .then(
      function(response) {
          console.log("SUCCESS", response);
      },
      function(error) {
          console.log("FAILED", error);
      }
  );
  // Show alert
  document.querySelector('.email-alert').style.display = 'block';

  // Hide alert after 3 seconds
  setTimeout(function(){
    document.querySelector('.email-alert').style.display = 'none';
  },5000);

  // Clear form
  document.getElementById('contact-form').reset();

  return false; 
}