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
    let gen_button = document.getElementById("gen_button");
    gen_button.addEventListener("click", function () {
        let mass_practice = [
            document.getElementById('count').value,
            document.getElementById("practice1").value,
            document.getElementById("practice2").value,
            document.getElementById("practice3").value,
            document.getElementById("practice4").value,
            document.getElementById("practice5").value,
            document.getElementById("practice6").value,
            document.getElementById("practice7").value,
            document.getElementById("practice8").value,
            document.getElementById("practice9").value,
            document.getElementById("practice10").value
        ];
        // eel.makeVariants(mass_practice);
        // eel.check();
        eel.build(mass_practice);
    });


});