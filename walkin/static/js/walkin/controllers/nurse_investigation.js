// 
// This controller provides a custom interface for Walkin nurses to create many
// investigations at once.
//
controllers.controller(
    'WalkinNurseInvestigationsCtrl',
    function($scope, $modalInstance, $q, episode){
        
        $scope.investigations = {};
        $scope.episode        = episode;

        $scope.test_names = {
            blood_culture    : 'Blood Culture',
            urine_mcs        : 'Urine MC&S',
            wound_swab_mcs   : 'Wound swab MC&S',
            throat_swab_mcs  : 'Throat swab MC&S',
            stool_mcs        : 'Stool MC&S',
            stool_ocp        : 'Stool OCP',
            malaria_film     : 'Malaria Film',
            full_blood_count : 'Full Blood Count',
            biochemistry     : 'Biochemistry',
            serum_save       : 'Serum Save'
        }
        
        $scope.save = function(){
            var saves = [];
            _.each(_.keys($scope.investigations), function(key){
                if($scope.investigations[key] == true){
                    test = $scope.episode.newItem('microbiology_test');
                    saves.push(test.save({test: $scope.test_names[key]}));
                }
            });
            if(saves.length > 0){
                $q.all(saves).then(
                    function(){
                        $modalInstance.close();
                    }
                );
            }else{
                $modalInstance.close();
            }
        };
        
    }
);
