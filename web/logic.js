window.addEventListener("DOMContentLoaded", function () {
    let settings_button = document.getElementById("settings_button");
    settings_button.addEventListener("click", function () {
        document.getElementsByClassName('main_menu')[0].style.display = "none";
       document.getElementsByClassName('settings')[0].style.display = "flex";
    });
    let back_button = document.getElementById("back_button");
    back_button.addEventListener("click", function () {
        document.getElementsByClassName('main_menu')[0].style.display = "block";
        document.getElementsByClassName('settings')[0].style.display = "none";
    })

    let categoryCheckbox = document.querySelectorAll('.category_checkbox');
    categoryCheckbox.forEach(function (checkbox) {
       checkbox.addEventListener('change', function () {
           let category = this.closest('.category');

           // Находим все элементы sub_category внутри текущего category
           let subCategories = category.querySelectorAll('.sub_category');

           // Переключаем видимость элементов sub_category
           subCategories.forEach(function(subCategory) {
               subCategory.style.display = subCategory.style.display === 'flex' ? 'none' : 'flex';
           });
       });
    });

    let subCategoryCheckbox = document.querySelectorAll('.sub_category_checkbox');
    subCategoryCheckbox.forEach(function (checkbox) {
       checkbox.addEventListener('change', function () {
           let subCategory = this.closest('.sub_category');

           // Находим все элементы sub_category_task внутри текущего subCategory
           let tasks = subCategory.querySelectorAll('.sub_category_task');

           // Переключаем видимость элементов sub_category_task
           tasks.forEach(function(task) {
               task.style.display = task.style.display === 'flex' ? 'none' : 'flex';
           });
       });
    });

    let gen_button = document.getElementById("gen_button");
    gen_button.addEventListener("click", function () {
        let mass_practice = [
            document.getElementById("variant_count").value,
            document.getElementById("practice1").checked,
            document.getElementById("practice2").checked,
            document.getElementById("practice3").checked,
            document.getElementById("practice4").checked,
            document.getElementById("practice5").checked,
            document.getElementById("practice6").checked,
            document.getElementById("practice7").checked,
            document.getElementById("practice8").checked,
            document.getElementById("practice9").checked,
            document.getElementById("practice10").checked,
            document.getElementById("practice11").checked,
            document.getElementById("practice12").checked,
            document.getElementById("theory").value
        ];
        // eel.makeVariants(mass_practice);
        // eel.check();
        eel.build(mass_practice);
        // eel.p(mass_practice);
    });


});