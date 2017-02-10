$(function() {

    var model = {
        init: function() {
            this.cats = [
            {
                name: 'Bella',
                clickCount: 0
            },
            {
                name: 'Tigger',
                clickCount: 0
            },
            {
                name: 'Oreo',
                clickCount: 0
            }];
            this.currentCat = this.cats[0];
        },

        setCurrentCat: function(catName) {
            for (var cat in this.cats) {
                var thisCat = this.cats[cat];
                if (thisCat.name === catName) {
                    this.currentCat = thisCat;
                }
            }
            catView.render();
        },

        getCurrentCat: function() {
            return this.currentCat;
        },

        incrementClickCount: function() {
            for (var cat in this.cats) {
                var thisCat = this.cats[cat];
                if (thisCat.name === this.currentCat.name) {
                    thisCat.clickCount += 1;
                }
            }
            catView.render();
        }
    };

    var controller = {
        init: function() {
            model.init();
            listView.init();
            catView.init();
        },

        getAllCats: function() {
            return model.cats;
        },

        getCurrentCat: function(catName) {
            return model.getCurrentCat(catName);
        },

        setCurrentCat: function(catName) {
            model.setCurrentCat(catName);
            catView.render();
        },

        incrementClickCount: function() {
            model.incrementClickCount();
            catView.render();
        }
    };

    var listView = {
        init: function() {
            // reference cat list
            this.$catList = $('.cat-names');
            // attach event listener to links
            this.$catList.on('click', '.cat-link', function(e) {
                var catName = $(this).text();
                controller.setCurrentCat(catName);
            });
            listView.render();
        },

        render: function() {
            var htmlStr = '';
            // populate cat list html into the container DOM node
            controller.getAllCats().forEach(function(cat) {
                var catName = cat.name;
                htmlStr += '<button type="button" class="list-group-item cat-link" id=' + catName + '>' + catName + '</button>';
            });
            this.$catList.html(htmlStr);
        }
    };

    var catView = {
        init: function() {
            // reference cat details
            this.$catDetails = $('.cat-container');
            // attach event listener to button
            this.$catDetails.on('click', 'button', function(e) {
                controller.incrementClickCount();
            });
            catView.render();
        },

        render: function() {
            // populate cat details html into the container DOM node
            var htmlStr = '';
            var currentCat = controller.getCurrentCat();
            var catName = currentCat.name;
            var clickCount = currentCat.clickCount;
            htmlStr += '<div class="cat-name"><h2 id="cat-name">' + catName + '</h2></div><div class="cat-image"><img id="cat-img" src="img/' + catName + '.jpg" alt="a picture of a cute cat"></div><div class="count-message"><p>You have clicked the cat <strong id="count-' + catName +  '">' + clickCount + '</strong> times!</p></div><button class="btn btn-success button-increment" id="increment-count-' + catName +  '">Click Me!</button>';
            this.$catDetails.html(htmlStr);
        }
    };

    controller.init();
});