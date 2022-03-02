const $form = $('form[name=signup_form]');

$form.submit(function(e){
  e.preventDefault();

  const $data = $form.serialize();

  $.ajax({
    url : "/createuser/",
    type: "POST",
    data: $data,
    dataType: "json",
    success: function(resp){
      console.log("success",resp)
    },
    error: function(resp){
      console.log("error",resp)
    }
  });
});