var app = angular.module('app', ['ngTouch']);
 
app.controller('BDACtrl', ['$scope', 'factory', '$http', function ($scope, factory, $http) {
    
    $scope.submit = function() {
        //$scope.filepath = 'C:\\Users\\monu\\Desktop\\python\\data_file.csv'
        //$scope.index = 'bda1'
        //console.log($scope.index,$scope.filepath)
        api = 'pushData/'
        
        data = {
            filepath: $scope.filepath,
            index: $scope.index,
            }

        factory.getData(api,data);        
        //$scope.clear();   
    };

    $scope.clear = function() {
        $scope.filepath = '';
        $scope.index = '';        
    }

}]);

app.factory('factory', ['$http','$q', function($http, $q) {
    var factory = {}
    factory.getData = function(api,param) {
        var d = $q.defer();

        console.log(api)

        $http({
            method:'GET',
            url: api,
            params : param           
        }).success(function(result) {
            d.resolve(result)
            alert("Success" + result.data);
        }).error(function(result) {
            console.log("Error Occurred:")
            d.resolve(result)
            alert("Failure");
        });
        return d.promise;
    };

    
    return factory;
}]);