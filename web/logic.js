window.addEventListener("DOMContentLoaded", function () {
    let settings_button = document.getElementById("settings_button");
    settings_button.addEventListener("click", function () {
       document.getElementsByClassName('settings')[0].style.display = "block";
    });
    let back_button = document.getElementById("back_button");
    back_button.addEventListener("click", function () {
        document.getElementsByClassName('settings')[0].style.display = "none";
    })
    let task_category_2 = document.getElementById("task_category_2_title");
    task_category_2.addEventListener("click", function () {
        document.getElementsByClassName('tasks_folder')[0].classList.toggle("active_task_folder");
        task_category_2.classList.toggle("active_task_category_title");
    });
    let g = 1;
    let t = 2;
    let gen_button = document.getElementById("gen_button");
    gen_button.addEventListener("click", function () {
        eel.makeVariants(g, t);
    });


});