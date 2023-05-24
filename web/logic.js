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




    
    let g = 1;
    let t = 2;
    let gen_button = document.getElementById("gen_button");
    gen_button.addEventListener("click", function () {
        eel.makeVariants(g, t);
    });


});