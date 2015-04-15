//
// This is our "Enter Walk-in" flow controller
//
controllers.controller(
    'WalkinHospitalNumberCtrl',
    function($scope, $modalInstance, $modal, $rootScope, $q,
             schema, options,
             Episode){

        $scope.model = {
            hospitalNumber : null
        }
        $scope.patient = null;

        //
        // When we've created an episode with this flow, tag it to the correct
        // teams and then kill the modal.
        //
        $scope.tag_and_close = function(episode){
            if(!episode.newItem){
                episode = new Episode(episode, schema);
            };
            var ep = episode.makeCopy();
            var location = episode.location[0].makeCopy();
            ep.category = 'Walkin';

            //
            // Pre fill some tests:
            //
            var hiv = episode.newItem('microbiology_test',
                                      {column: $rootScope.fields.microbiology_test});

            $q.all([
                episode.save(ep),
                episode.location[0].save(location),
                hiv.save({test: 'Hiv Point of Care'}),
            ]).then(function(){
                episode.active = true;
                $modalInstance.close(episode);
            })

        };

        //
        // We have an initial hospital number - we can now figure out whether to
        // Add or pull over.
        //
        $scope.findByHospitalNumber = function(){
            Episode.findByHospitalNumber(
                $scope.model.hospitalNumber,
                {
                    newPatient: $scope.new_patient,
                    newForPatient: $scope.new_for_patient,
                    error: function(){
                        // This shouldn't happen, but we should probably handle it better
                        alert('ERROR: More than one patient found with hospital number');
                        $modalInstance.close(null)
                    }
                }
            );
        };

        //
        // Create a new patient
        //
        $scope.new_patient = function(result){
            // There is no patient with this hospital number
            // Show user the form for creating a new episode,
            // with the hospital number pre-populated
            modal = $modal.open({
                templateUrl: '/templates/modals/add_walkin_episode.html/',
                controller: 'AddEpisodeCtrl',
                resolve: {
                    schema: function() { return schema; },
                    options: function() { return options; },
                    demographics: function() {
                        return { hospital_number: $scope.model.hospitalNumber }
                    }
                }
            }).result.then(function(result) {
                // The user has created the episode, or cancelled
                if(result){ // We made an episode!
                    $scope.tag_and_close(result);
                }else{
                    $modalInstance.close(result);
                }
            });
        };

        //
        // Create a new episode for an existing patient
        //
        $scope.new_for_patient = function(patient){
            if(patient.active_episode_id && _.keys(patient.episodes).length > 0){
                alert('This walkin patient is a current inpatient!');
            }else{
                $scope.add_for_patient(patient);
            };
        };

        //
        // Add a new episode for an existing patient. Pre-fill the relevant demographics
        //
        $scope.add_for_patient = function(patient){
            var demographics = patient.demographics[0];
            if(demographics.date_of_birth){
                var dob = moment(demographics.date_of_birth, 'YYYY-MM-DD')
                    .format('DD/MM/YYYY');
                demographics.date_of_birth = dob;
            }
            modal = $modal.open({
                templateUrl: '/templates/modals/add_walkin_episode.html/',
                controller: 'AddEpisodeCtrl',
                resolve: {
                    schema: function() { return schema; },
                    options: function() { return options; },
                    demographics: function() { return demographics; }
                }
            }).result.then(function(result) {
                // The user has created the episode, or cancelled
                if(result){ // We made an episode!
                    $scope.tag_and_close(result);
                }else{
                    $modalInstance.close(result);
                }
            });
        };

        // Let's have a nice way to kill the modal.
        $scope.cancel = function() {
            $modalInstance.close('cancel');
        };
    }
);
