$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
});

$(document).on('submit','#comment_form',function(e){
  e.preventDefault();
  $.ajax({
      type:'post',
      url:'savecomment/',
      data:{
          objID:$('#objID').val(),
          comment:$('#comment').val(),
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function()
      {
          location.reload();
           
      }

  });
}); 







