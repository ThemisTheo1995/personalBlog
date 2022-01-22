
document.addEventListener("DOMContentLoaded", function() {
    // Account , Notifications dropdown listener
    document.addEventListener('click', function (e) {
        const dropdownBtn = e.target.closest('button');
        const notifMenu = document.getElementById('notifications-menu');
        if ((dropdownBtn === null || !(dropdownBtn.classList.contains('dropdown-menu-btn'))) && !notifMenu.contains(e.target)){
            const dropdownMenus = document.querySelectorAll('.dropdown-menu');
            dropdownMenus.forEach(item =>{ 
                item.classList.remove('scale-1');
                item.classList.add('scale-0')});
        }
    });

    // Mobile menu view
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

// Account , Notifications dropdown function
function navDropdown(menu_id){
    // Minimise all the dropdowns but the clicked one.
    const dropdownMenus = document.querySelectorAll('.dropdown-menu');
    dropdownMenus.forEach(item =>{ 
        if(!(item.id == menu_id)){
            item.classList.remove('scale-1');
            item.classList.add('scale-0');
        }
    });
    // Minimise or Expand the clicked one based on its status.
    const dropdownMenu = document.getElementById(menu_id);
    if (dropdownMenu.classList.contains("scale-0")){
        dropdownMenu.classList.remove("scale-0");
        dropdownMenu.classList.add("scale-1");

        // Update the notification list status and remove animation.
        dropdownMenu.classList.add("scale-1");
    }else{
        dropdownMenu.classList.remove("scale-1");
        dropdownMenu.classList.add("scale-0");
    }
}

// Update the notification dropdown list status and remove animation.
function nav_notifications_handler(){
    // Update the status of the unread articles.
    fetch("{% url 'notification:nav_notifications_handler' %}").then(function(response){
        if (response.status == 200){
            // Remove animation
            document.getElementById("ntf_ping").classList.add("hidden");
            // Remove 'new notifications' effects
            notifications = document.querySelectorAll('.not-element');
            notifications.forEach(item =>{
                item.classList.remove("font-semibold");
            });
        }else{
        }
    });
}
