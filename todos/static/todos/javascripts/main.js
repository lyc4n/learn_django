$(function(){
  $('.modal-submitter').on('click', function(e){
    e.preventDefault()
    $submitter = $(e.target)
    $form      = $('#' + $submitter.data('form-id'))
    $form.find('input[type=submit]').click()
  })
})
