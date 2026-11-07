// Econ-ARK main.js v1.1

const nav = document.querySelector('.navigation');
const navToggle = document.getElementById('toggleNav');

navToggle.addEventListener('click', function (e) {
  e.preventDefault();
  if (window.getComputedStyle(nav).display === 'block') {
    nav.style.display = 'none';
  } else {
    nav.style.display = 'block';
  }
});

// If anchor "launch" open link of first launch button
function checkForLaunch() {
  var pathname = window.location.hash;
  if (pathname == '#launch') {
    var href = document.getElementsByClassName('launch-link')[0].href;
    window.location = href;
  }
}

// If anchor "dashboard" open link of first launch button
function checkForLaunchDashboard() {
  var pathname = window.location.hash;
  if (pathname == '#dashboard') {
    var href = document.getElementsByClassName('dashboard-link')[0].href;
    window.open(href, '_blank');
//     window.location = href;
  }
}
window.addEventListener(
  'hashchange',
  function () {
    checkForLaunch();
    checkForLaunchDashboard();
  },
  false
);
checkForLaunch();
checkForLaunchDashboard();

// Check for query string, launch notbooks accordingly
var urlParams = new URLSearchParams(window.location.search);
if ( urlParams.has('dashboard') ) {
  var href = document.getElementsByClassName('dashboard-link')[0].href;
  window.location = href;
} else if ( urlParams.has('launch') ) {
  var href = document.getElementsByClassName('launch-link')[0].href;
  window.location = href;  
}

// Actions accordion
if ( document.getElementsByClassName('actions')[0] ) {
  var actionDetails = $('.actions .action__details');
  var actionHeaders = $('.actions .action__header');
  $('.action__header').click(function(e){
    e.preventDefault();
    actionHeaders.removeClass('active');
    actionHeaders.find('i').removeClass('fa-chevron-down').addClass('fa-chevron-right');
    $(this).addClass('active');
    $(this).find('i').removeClass('fa-chevron-right').addClass('fa-chevron-down');
    actionDetails.slideUp('fast');
    $(this).next('.action__details').slideDown('fast');
  });
  $('.actions .action__header')[0].click();
}

// myBinder launch link animation
function delayLinkOpening(event) {
  event.preventDefault(); // Prevent the default link behavior

  var clickedLink = this;
  var overlay = document.querySelector('.mybinder-overlay');

  // Add a class to the clicked link
  overlay.classList.add('show');

  // Get the href attribute of the clicked link
  var linkHref = clickedLink.getAttribute('href');

  // Delay the link opening by 3 seconds
  setTimeout(function () {
    // Navigate to the link after the delay
    window.open(linkHref);

    // Remove the class after the link is opened
    overlay.classList.remove('show');
  }, 3000);
}

// Attach the delayLinkOpening function to all links with the class 'mybinder-overlay'
var delayedLinks = document.querySelectorAll('.animate-overlay');
delayedLinks.forEach(function (link) {
  link.addEventListener('click', delayLinkOpening);
});

