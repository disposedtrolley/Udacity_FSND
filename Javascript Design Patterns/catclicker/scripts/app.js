$(function() {

    var model = {

        init: function() {
            this.cats = [
                {
                    name: 'Bella',
                    clickCount: 0,
                    imgSrc: '/img/Bella.jpg'
                },
                {
                    name: 'Tigger',
                    clickCount: 0,
                    imgSrc: '/img/Tigger.jpg'
                },
                {
                    name: 'Oreo',
                    clickCount: 0,
                    imgSrc: '/img/Oreo.jpg'
                }];
            this.currentCat = this.cats[0];
        },

        setCurrentCat: function(catName) {
            for (var i = 0; i < this.cats.length; i++) {
                var thisCat = this.cats[i];
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
            for (var i = 0; i < this.cats.length; i++) {
                var thisCat = this.cats[i];
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
            var currentCat = controller.getCurrentCat();

            var catName = currentCat.name;
            var clickCount = currentCat.clickCount;
            var imgSrc = currentCat.imgSrc;

            // update cat name
            $('.cat-name > h2').text(catName);
            // update cat image
            $('.cat-img').attr('src', imgSrc);
            // update click count
            $('.count').text(clickCount);
        }
    };

    controller.init();
});