$(document).ready(function() {

    var catClicks = {
        'Bella': 0,
        'Tigger': 0,
        'Oreo': 0
    };

    // Create list of links to each cat.
    for (var cat in catClicks) {
        $('.cat-names').append('<button type="button" class="list-group-item cat-link" id=' + cat + '>' + cat + '</button>');
    }

    // Attach click handler to cat links.
    $('.cat-link').click(function(e) {
        catName = $(this).text();
        showCat(catName);
    });

    // Display the details of a particular cat, including the increment button.
    function showCat(catName) {
        console.log(catName + " clicked");
        $('.cat-container').empty();
        $('.cat-container').append('<div class="cat-name"><h2 id="cat-name">' + catName + '</h2></div><div class="cat-image"><img id="cat-img" src="img/' + catName + '.jpg" alt="a picture of a cute cat"></div><div class="count-message"><p>You have clicked the cat <strong id="count-' + catName +  '">0</strong> times!</p></div><button class="btn btn-success button-increment" id="increment-count-' + catName +  '">Click Me!</button>');
        // Attach click handler to increment button.
        $('.button-increment').click(function(e) {
            var $elemCount = $(this).parent().find('strong');
            var incrementedCount = parseInt($elemCount.text(), 10) + 1;
            $elemCount.text(incrementedCount);
        });
    }

});