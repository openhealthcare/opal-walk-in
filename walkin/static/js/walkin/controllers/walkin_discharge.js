//
// This is the "Next stage" exit flow controller for OPAT patients.
//
controllers.controller(
    'WalkinDischargeCtrl',
    function($scope, $modalInstance, $modal, $rootScope, $q,
             $modal,
             growl,
             Item, CopyToCategory, UserProfile,
             options, episode, tags){

        $scope.episode = episode;
        $scope.meta = {
            accepted        : null,
            target_team     : null,
            results_actioned: null
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
                growl.success('Moved to Doctor list')
                $modalInstance.close('discharged');
            });
        }

        $scope.move_to_review = function(){
            $scope.ensure_tagging($scope.episode);
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.walkin_doctor = false;
            tagging.walkin_review = true;

            $scope.episode.tagging[0].save(tagging).then(function(){
                growl.success('Moved to Review list')
                $modalInstance.close('discharged');
            });
        }

        $scope.nurse_led_care = function(){
            var nursing = $scope.episode.newItem('walkin_nurse_led_care');
            to_save = [
                nursing.save({
                    reason:    $scope.meta.nurse_reason,
                    treatment: $scope.meta.treatment
                }),
            ]
            if($scope.meta.diagnosis){
                var diagnosis = $scope.episode.newItem('diagnosis');
                to_save.push(diagnosis.save({condition: $scope.meta.diagnosis}));
            }
            
            $scope.ensure_tagging($scope.episode);

            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.walkin_triage = false;
            tagging.walkin_doctor = false;
            tagging.walkin_review = false;

            if($scope.episode.management.length == 0 || !$scope.episode.management[0].makeCopy){
                $scope.episode.management[0] = $scope.episode.newItem('management',{
                    column: $rootScope.fields.management }
                                                                  )
            }
            var management = $scope.episode.management[0].makeCopy();
            management.results_actioned = $scope.meta.results_actioned;
            to_save.push($scope.episode.management[0].save(management));
            to_save.push($scope.episode.tagging[0].save(tagging));
            
            $q.all(to_save).then(function(){
                growl.success('Removed from Walk-in lists')
                var deferred = $q.defer();
                'discharged'

                $rootScope.open_modal(
                    'ModalDischargeSummaryCtrl',
                    '/dischargesummary/modals/walkinnurse/',
                    'lg',
                    {episode: episode}
                ).result.then(
                    function(r){ deferred.resolve('discharged') },
                    function(r){ deferred.reject('discharged') }                    
                );
                
                $modalInstance.close(deferred.promise);
            });
        }

        // 
        // Copy this episode to a new inpatient episode.
        //
        // Untag this episode.
        // Tag the new episode to the selected team
        // 
        $scope.admit_to_ward = function(){
            $scope.ensure_tagging($scope.episode);
            var tagging = $scope.episode.tagging[0].makeCopy();
            tagging.walkin = false;
            tagging.walkin_doctor = false;

            CopyToCategory($scope.episode.id, 'inpatient').then(
                function(episode){
                    var newtagging = episode.tagging[0];
                    var newtags = {};
                    newtags[$scope.meta.target_team] = true;
                    
                    $q.all([
                        $scope.episode.tagging[0].save(tagging),
                        newtagging.save(newtags)
                    ]).then(function(){
                        var msg = 'Admitted to ' + $scope.meta.target_team + ' ward';
                        growl.success(msg);
                        $modalInstance.close('discharged');                        
                    })
                });
        }

        $scope.move_to_management = function(){
            var deferred = $q.defer();
            var item = $scope.episode.newItem('management');
            
            $scope.episode.addItem(item);
            
            $modal.open({
                templateUrl: '/templates/modals/management.html',
                controller: 'EditItemCtrl',
                resolve: {
                    item: function() { return item; },
                    options: function() { return options; },
                    profile: function() { return UserProfile; },
                    episode: function() { return episode; }
                }
            }).result.then(
                function(r){ deferred.resolve(r) },
                function(r){ deferred.reject(r) }
            );
            $modalInstance.close(deferred.promise);
        }

        // Let's have a nice way to kill the modal.
        $scope.cancel = function() {
            $modalInstance.close('cancel');
        };
    });
