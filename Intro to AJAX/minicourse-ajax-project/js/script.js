
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var inputStreet = $('#street').val();
    var inputCity = $('#city').val();
    var address = inputStreet + ", " + inputCity;

    $greeting.text("So, you want to live at " + address + "?");
    $body.append('<img class="bgimg" src="http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address + '">');

    // NY Times
    var nyTimesUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    nyTimesUrl += '?' + $.param({
        'api-key': "73f7a9f472f84d5390964f05262a356d",
        'q': inputCity,
        'fl': "web_url,headline,lead_paragraph"
    });

    $.getJSON(nyTimesUrl, function(data) {
        articles = [];
        $.each(data.response.docs, function(key, val) {
            articles.push('<li class="article"><a href="' + val["web_url"] + '">' + val["headline"]["main"] + '</a><p>'+ val["lead_paragraph"] + '</p></li>');
        });
        $( "<ul/>", {
            "class": "article-list",
            "id": "nytimes-articles",
            html: articles.join( "" )
        }).appendTo( ".nytimes-container" );
    }).error(function(e) {
        $nytHeaderElem.text("New York Times Articles Could Not Be Loaded");
    });

    return false;
}

$('#form-container').submit(loadData);
