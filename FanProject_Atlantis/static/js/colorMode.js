var toggle = document.getElementById("theme-toggle")

var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")
if (storedTheme) {
  document.documentElement.setAttribute('data-theme', storedTheme)
  if (storedTheme === "light") {
    $("#theme-icon").removeClass("bi-moon-stars-fill")
    $("#theme-icon").addClass("bi-sun-fill")
  } else {
    $("#theme-icon").removeClass("bi-sun-fill")
    $("#theme-icon").addClass("bi-moon-stars-fill")
  }
}

toggle.onclick = function () {
  var currentTheme = document.documentElement.getAttribute("data-theme")
  var targetTheme = "light"

  if (currentTheme === "light") {
    targetTheme = "dark"
    $("#theme-icon").removeClass("bi-sun-fill")
    $("#theme-icon").addClass("bi-moon-stars-fill")
  } else {
    $("#theme-icon").removeClass("bi-moon-stars-fill")
    $("#theme-icon").addClass("bi-sun-fill")
  }

  document.documentElement.setAttribute('data-theme', targetTheme)
  localStorage.setItem('theme', targetTheme)
};