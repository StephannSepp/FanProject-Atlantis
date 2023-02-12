window.onscroll = function () {
  let winScroll = document.body.scrollTop || document.documentElement.scrollTop
  let height = document.documentElement.scrollHeight - document.documentElement.clientHeight
  let vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
  if (height > vh) {
    let scrolled = (winScroll / height) * 100
    $("#scrollProgressBar").css("width", scrolled + "%")
  }
}
