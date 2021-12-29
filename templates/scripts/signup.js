document.addEventListener("DOMContentLoaded", function() {
    // Avatar selection.
    document.addEventListener('click', function (e) {
        var avatar_list = document.querySelectorAll(".user-avatar");
        if(e.target.classList.contains('user-avatar')){
            const avatar = e.target;
            // CSS manipulation
            avatar_list.forEach(item => item.classList.remove('bg-pink-800'));

            if(avatar.classList.contains('bg-pink-800')){
                avatar.classList.remove('bg-pink-800');
                avatar.classList.add('bg-white');
            }else{
                avatar.classList.add('bg-pink-800');
                avatar.classList.remove('bg-white');
            }

            // Avatar value manipulation
            document.getElementById('id_avatar').value = avatar.id;
        }
    });
});