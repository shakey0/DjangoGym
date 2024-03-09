function adjustClassesForScreenWidth() {

    if (window.innerWidth <= 430) {

        var titleDiv = document.getElementById('title-div');
        if (titleDiv) {
            titleDiv.classList.remove('align-items-center');
        }
        var adminMainButtons = document.getElementById('admin-main-buttons');
        if (adminMainButtons) {
            adminMainButtons.classList.remove('ms-auto');
            adminMainButtons.classList.add('adjust-admin-main-buttons-vertical', 'mb-5');
        }
        var adminMainButtonsProfile = document.getElementById('admin-main-buttons-profile');
        if (adminMainButtonsProfile) {
            adminMainButtonsProfile.classList.remove('ms-auto');
        }

    } else {

        var titleDiv = document.getElementById('title-div');
        if (titleDiv) {
            titleDiv.classList.add('align-items-center');
        }
        var adminMainButtons = document.getElementById('admin-main-buttons');
        if (adminMainButtons) {
            adminMainButtons.classList.add('ms-auto');
            adminMainButtons.classList.remove('adjust-admin-main-buttons-vertical', 'mb-5');
        }
        var adminMainButtonsProfile = document.getElementById('admin-main-buttons-profile');
        if (adminMainButtonsProfile) {
            adminMainButtonsProfile.classList.add('ms-auto');
        }
    }

    if (window.innerWidth <= 630) {

        var titleDivHome = document.getElementById('title-div-home');
        if (titleDivHome) {
            titleDivHome.classList.remove('align-items-center');
        }
        var adminMainButtonsHome = document.getElementById('admin-main-buttons-home');
        if (adminMainButtonsHome) {
            adminMainButtonsHome.classList.remove('ms-auto');
            adminMainButtonsHome.classList.add('adjust-admin-main-buttons-vertical-630w', 'mb-5');
        }
    } else {

        var titleDivHome = document.getElementById('title-div-home');
        if (titleDivHome) {
            titleDivHome.classList.add('align-items-center');
        }
        var adminMainButtonsHome = document.getElementById('admin-main-buttons-home');
        if (adminMainButtonsHome) {
            adminMainButtonsHome.classList.add('ms-auto');
            adminMainButtonsHome.classList.remove('adjust-admin-main-buttons-vertical-630w', 'mb-5');
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
