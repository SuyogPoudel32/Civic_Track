
const menuBtn = document.getElementById("menuBtn");
const menuIcon = document.getElementById("menuIcon");
const mobileMenu = document.getElementById("mobileMenu");

menuBtn.addEventListener("click", () => {

    mobileMenu.classList.toggle("hidden");

    if (mobileMenu.classList.contains("hidden")) {
        menuIcon.classList.remove("fa-xmark");
        menuIcon.classList.add("fa-bars");
    } else {
        menuIcon.classList.remove("fa-bars");
        menuIcon.classList.add("fa-xmark");
    }

});
window.addEventListener("resize",() => {
  if (window.innerWidth >768) {
    mobileMenu.classList.add("hidden");
            menuIcon.classList.remove("fa-xmark");
        menuIcon.classList.add("fa-bars");
  }
}
)


