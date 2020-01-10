const nav = document.querySelector('.navigation');
const navToggle = document.getElementById('toggleNav');

navToggle.addEventListener('click', function(e) {
  e.preventDefault();
  if (window.getComputedStyle(nav).display === 'block') {
    nav.style.display = 'none';
  } else {
    nav.style.display = 'block';
  }
});

function filterMaterials() {
  var materials = document.querySelectorAll('#materialsList>li');
  var tabChoice = document.querySelector('.tabs-toggles li a.active').id;
  var tagChoice = document.getElementById('tagSelect').value;

  for (var i = 0; i < materials.length; i++) {
    if (tagChoice == 'All' && tabChoice == 'All') {
      materials[i].classList.remove('hideMaterial');
    } else {
      var hasTag = false;
      var hasTab = false;

      if (tagChoice == 'All') {
        hasTag = true;
      } else {
        var materialTags = materials[i].querySelectorAll('.tags li');
        for (var j = 0; j < materialTags.length; j++) {
          if (materialTags[j].textContent == tagChoice) {
            hasTag = true;
          }
        }
      }

      if (
        materials[i].classList.contains(tabChoice) ||
        tabChoice == 'allMaterial'
      ) {
        var hasTab = true;
      }

      if (hasTag && hasTab) {
        materials[i].classList.remove('hideMaterial');
      } else {
        materials[i].classList.add('hideMaterial');
      }
    }
  }
}

// Setup tab event listener and populate tag dropdown
if (document.getElementById('materialsList')) {
  const tabLinks = document.querySelectorAll('.tabs-toggles li a');
  for (var i = 0; i < tabLinks.length; i++) {
    tabLinks[i].addEventListener('click', function(e) {
      e.preventDefault();
      for (var j = 0; j < tabLinks.length; j++) {
        tabLinks[j].classList.remove('active');
      }
      this.classList.add('active');
      filterMaterials();
    });
  }

  var materialTags = document.querySelectorAll('#materialsList .tags li');
  var tags = [];
  for (var i = 0; i < materialTags.length; i++) {
    tags.push(materialTags[i].textContent);
  }
  let uniqueTags = [...new Set(tags)];
  var tagSelect = document.getElementById('tagSelect');
  for (var i = 0; i < uniqueTags.length; i++) {
    option = document.createElement('option');
    option.value = option.text = uniqueTags[i];
    tagSelect.add(option);
  }

  document.getElementById('tagSelect').addEventListener('change', event => {
    filterMaterials();
  });

  const choices = new Choices('#tagSelect', {
    itemSelectText: ''
  });
}
