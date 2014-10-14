//
// This is the "Next stage" exit flow controller for OPAT patients.
//
controllers.controller(
    'WalkinDischargeCtrl',
    function($scope, $modalInstance, $rootScope,
             Item,
             options, episode, tags){

        $scope.episode = episode;
        $scope.episode.tagging[0] = $scope.episode.tagging[0].makeCopy();
        $scope.meta = {
            accepted: null
        };

        // Put all of our lookuplists in scope.
      for (var name in options) {
        if (name.indexOf('micro_test') != 0) {
          $scope[name + '_list'] = options[name];
        };
      };


        // Make sure that the episode's tagging item is an instance not an object
        $scope.ensure_tagging = function(episode){
            if(!$scope.episode.tagging[0].makeCopy){
                $scope.episode.tagging[0] = $scope.episode.newItem('tagging',{
                    column: $rootScope.fields.tagging }
                                                                  )
            }
            return
        };

        $scope.move_to_doctor = function(){
            $scope.ensure_tagging($scope.episode);
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.walkin_triage = false;
            tagging.walkin_doctor = true;

            $scope.episode.tagging[0].save(tagging).then(function(){
                $modalInstance.close('discharged');
            });
        }

        $scope.move_to_review = function(){
            $scope.ensure_tagging($scope.episode);
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.walkin_doctor = false;
            tagging.walkin_review = true;

            $scope.episode.tagging[0].save(tagging).then(function(){
                $modalInstance.close('discharged');
            });
        }

        $scope.remove_from_list = function(){
            $scope.ensure_tagging($scope.episode);
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.walkin_triage = false;
            tagging.walkin_doctor = false;

            $scope.episode.tagging[0].save(tagging).then(function(){
                $modalInstance.close('discharged');
            });
        }

        $scope.admit_to_ward = function(){
            $scope.ensure_tagging($scope.episode);
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.walkin = false;
            tagging.walkin_doctor = false;
            // what sort of inpatient should they be?
            // show modal with possible tags?
            tagging.mine = true;

            $scope.episode.tagging[0].save(tagging).then(function(){
                $modalInstance.close('discharged');
            });
        }

        // Let's have a nice way to kill the modal.
        $scope.cancel = function() {
          $modalInstance.close('cancel');
        };
    });
