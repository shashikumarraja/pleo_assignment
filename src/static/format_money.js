$(document).ready(function(){
    $('.wrapper').on('click', '.get_result', function(){
       var number = $("#input_num").val();
       $.ajax({
        url: "/format_money",
        type: "get",
        data: {number: number},
        success: function(response) {
          $(".result").html('Formatted Number: '+response.formatted_number.toString());
          $(".result").attr("id", "success_message");
        },
        error: function(jqXHR, textStatus, errorThrown)  {
          const response = JSON.parse(jqXHR.responseText);
          const error_message = response.message;
          console.log(error_message)
          $(".result").html('Error Message: '+ error_message);
          $(".result").attr("id", "error_message");
        },
       });
    });
  });