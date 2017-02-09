$(document).ready(function() {

    var cats = {
        'Bella': 0,
        'Tigger': 0,
        'Oreo': 0
    };

    // Create list of links to each cat.
    for (var cat in cats) {
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
        $catContainer = $('.cat-container');
        $catContainer.empty();
        $catContainer.append('<div class="cat-name"><h2 id="cat-name">' + catName + '</h2></div><div class="cat-image"><img id="cat-img" src="img/' + catName + '.jpg" alt="a picture of a cute cat"></div><div class="count-message"><p>You have clicked the cat <strong id="count-' + catName +  '">' + cats[catName] + '</strong> times!</p></div><button class="btn btn-success button-increment" id="increment-count-' + catName +  '">Click Me!</button>');
        // Attach click handler to increment button.
        $('.button-increment').click(function(e) {
            // Update clicks in cats object.
            cats[catName] += 1;
            // Update count message.
            var $countMessage = $('.count-message');
            $countMessage.empty();
            $countMessage.append('<p>You have clicked the cat <strong id="count-' + catName +  '">' + cats[catName] + '</strong> times!</p>');
        });
    }

});