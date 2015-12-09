
    angular.module('sortApp', [])

    .controller('mainController', function ($scope)
    $scope.sortType = 'name'; // set the default sort type
    $scope.sortReverse = false;  // set the default sort order
    $scope.searchFish = '';     // set the default search/filter term

    $scope.sushi = ['test']


    );
    