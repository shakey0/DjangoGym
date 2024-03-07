function adjustClassesForScreenWidth() {

    if (window.innerWidth <= 430) {

        var classesTitleDiv = document.getElementById('classes-title-div');
        if (classesTitleDiv) {
            classesTitleDiv.classList.remove('align-items-center');
        }
        var classesAdminMainButtons = document.getElementById('classes-admin-main-buttons');
        if (classesAdminMainButtons) {
            classesAdminMainButtons.classList.remove('ms-auto');
            classesAdminMainButtons.classList.add('adjust-admin-main-buttons-vertical', 'mb-5');
        }

    } else {

        var classesTitleDiv = document.getElementById('classes-title-div');
        if (classesTitleDiv) {
            classesTitleDiv.classList.add('align-items-center');
        }
        var classesAdminMainButtons = document.getElementById('classes-admin-main-buttons');
        if (classesAdminMainButtons) {
            classesAdminMainButtons.classList.add('ms-auto');
            classesAdminMainButtons.classList.remove('adjust-admin-main-buttons-vertical', 'mb-5');
        }
    }
}

window.addEventListener('resize', adjustClassesForScreenWidth);

adjustClassesForScreenWidth();


function adjustScheduledForScreenWidth() {

    var titleDivs = document.querySelectorAll('.scheduled-title-div');
    var adminMainButtons = document.querySelectorAll('.scheduled-top-buttons');

    if (window.innerWidth <= 430) {
        titleDivs.forEach(function(div) {
            div.classList.remove('d-flex');
        });
        adminMainButtons.forEach(function(btn) {
            btn.classList.add('mt-2');
        });
    } else {
        titleDivs.forEach(function(div) {
            div.classList.add('d-flex');
        });
        adminMainButtons.forEach(function(btn) {
            btn.classList.remove('mt-2');
        });
    }
}

window.addEventListener('resize', adjustScheduledForScreenWidth);

adjustScheduledForScreenWidth();
