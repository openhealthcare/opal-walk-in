//
// This controller provides a custom interface for managing Zika patients
//
controllers.controller(
    'ZikaCtrl',
    function( $scope, $modalInstance, $q, episode ){
        "use strict";

        $scope.episode = episode;

        $scope.editing = {};

        $scope.save = function(){
        };

        // Let's have a nice way to kill the modal.
        $scope.cancel = function() {
            $scope.saving = false;
            $modalInstance.close('cancel');
        };

    }
);
