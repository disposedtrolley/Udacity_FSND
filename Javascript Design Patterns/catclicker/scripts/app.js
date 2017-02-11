$(function() {

    var model = {

        init: function() {
            this.cats = [
                {
                    id: 1,
                    name: 'Bella',
                    clickCount: 0,
                    imgSrc: '/img/Bella.jpg'
                },
                {
                    id: 2,
                    name: 'Tigger',
                    clickCount: 0,
                    imgSrc: '/img/Tigger.jpg'
                },
                {
                    id: 3,
                    name: 'Oreo',
                    clickCount: 0,
                    imgSrc: '/img/Oreo.jpg'
                }];
            this.currentCat = this.cats[0];
        },

        setCurrentCat: function(catId) {
            for (var i = 0; i < this.cats.length; i++) {
                var thisCat = this.cats[i];
                if (thisCat.id === catId) {
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
                if (thisCat.id === this.currentCat.id) {
                    thisCat.clickCount += 1;
                }
            }
            catView.render();
        },

        updateCatDetails: function(cat) {
            for (var i = 0; i < this.cats.length; i++) {
                var thisCat = this.cats[i];
                if (thisCat.id === cat.id) {
                    this.cats[i] = cat;
                }
            }
        }
    };

    var controller = {
        init: function() {
            model.init();
            listView.init();
            catView.init();
            adminView.init();
        },

        getAllCats: function() {
            return model.cats;
        },

        getCurrentCat: function(catId) {
            return model.getCurrentCat(catId);
        },

        setCurrentCat: function(catId) {
            model.setCurrentCat(catId);
            catView.render();
            adminView.init();
        },

        incrementClickCount: function() {
            model.incrementClickCount();
            catView.render();
        },

        updateCatDetails: function(cat) {
            model.updateCatDetails(cat);
            catView.render();
            listView.render();
        }
    };

    var listView = {
        init: function() {
            // reference cat list
            this.$catList = $('.cat-names');
            // attach event listener to links
            this.$catList.on('click', '.cat-link', function(e) {
                var catId = parseInt($(this).attr('id'));
                controller.setCurrentCat(catId);
            });
            listView.render();
        },

        render: function() {
            var htmlStr = '';
            // populate cat list html into the container DOM node
            controller.getAllCats().forEach(function(cat) {
                var catName = cat.name;
                var catId = cat.id;
                htmlStr += '<button type="button" class="list-group-item cat-link" id=' + catId + '>' + catName + '</button>';
            });
            this.$catList.html(htmlStr);
        }
    };

    var catView = {
        init: function() {
            // reference cat details
            var $catDetails = $('.cat-container');
            // attach event listener to button
            $catDetails.on('click', 'img', function(e) {
                controller.incrementClickCount();
            });
            catView.render();

            var $adminButton = $('.show-admin');
            $adminButton.on('click', function(e) {
                adminView.render();
                $('.admin-container').show();
            });
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

    var adminView = {
        init: function() {
            this.cat = controller.getCurrentCat();

            var $adminContainer = $('.admin-container');
            $adminContainer.hide();

            this.$inputCatName = $adminContainer.find('form > .form-group > #inputCatName');
            this.$inputImageUrl = $adminContainer.find('form > .form-group > #inputImageUrl');
            this.$inputClickCount = $adminContainer.find('form > .form-group > #inputClickCount');

            var $saveButton = $adminContainer.find('.save-details');
            $saveButton.on('click', function(e) {
                e.preventDefault();
                adminView.cat.name = adminView.$inputCatName.val();
                adminView.cat.imgSrc = adminView.$inputImageUrl.val();
                adminView.cat.clickCount = adminView.$inputClickCount.val();
                controller.updateCatDetails(adminView.cat);
                controller.setCurrentCat(adminView.cat);
                $adminContainer.hide();
            });

            var $cancelButton = $adminContainer.find('.cancel');
            $cancelButton.on('click', function(e) {
                e.preventDefault();
                $adminContainer.hide();
            });
        },

        render: function() {
            // populate form with details of the current cat
            this.cat = controller.getCurrentCat();
            this.$inputCatName.val(this.cat.name);
            this.$inputImageUrl.val(this.cat.imgSrc);
            this.$inputClickCount.val(this.cat.clickCount);
        }
    };

    controller.init();
});