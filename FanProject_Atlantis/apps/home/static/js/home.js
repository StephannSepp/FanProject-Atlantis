$(window).on('scroll', function () {
  if ($(window).scrollTop()) {
    $('nav').addClass('dark')
  } else {
    $('nav').removeClass('dark')
  }
})