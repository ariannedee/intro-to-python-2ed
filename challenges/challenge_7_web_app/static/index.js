$(document).ready(function(){  // When document loads
  console.log('index.js loaded')

  var onButtonClick = function () {
    var button_id = this.id;
    console.log(button_id + ' clicked')

    $.post(  // Make a POST request
      "/click/" + button_id,  // to this endpoint
      function (data) {       // on success, do this
        console.log(data)
        $("#" + button_id).text("I've been clicked " + data["num_clicks"] + " times");  // Update button text
      }
    );
  }

  $('button').click(onButtonClick);  // When any button is clicked, call function

});