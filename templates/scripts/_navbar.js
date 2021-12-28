
document.addEventListener("DOMContentLoaded", function() {
    document.addEventListener('click', function (e) {
        const dropdownMenu = document.getElementById('profile-menu');
        console.log(e.target.parentNode.id);
        if (e.target.parentNode.id === 'profile-menu-btn'){
            if (dropdownMenu.classList.contains("scale-0")){
                dropdownMenu.classList.remove("scale-0");
                dropdownMenu.classList.add("scale-1");
            }else{
                dropdownMenu.classList.remove("scale-1");
                dropdownMenu.classList.add("scale-0");
            }
            }else{      
                dropdownMenu.classList.remove("scale-1");
                dropdownMenu.classList.add("scale-0");
        }
    });

    document.getElementById("mobile-menu-btn").addEventListener("click", function() {
        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenu.classList.contains("scale-0")){
            mobileMenu.classList.remove("scale-0");
            mobileMenu.classList.add("scale-1");
        }else{
            mobileMenu.classList.remove("scale-1");
            mobileMenu.classList.add("scale-0");
        }
    });
});
