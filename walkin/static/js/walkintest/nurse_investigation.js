describe('WalkinNurseInvestigationsCtrl', function (){
    var $controller, $scope, $modalInstance, $httpBackend, $rootScope, episode;

    beforeEach(module('opal.controllers'));
    
    beforeEach(inject(function($injector){
        $rootScope   = $injector.get('$rootScope');
        $scope       = $rootScope.$new();
        $controller  = $injector.get('$controller');
        $modal       = $injector.get('$modal');
        Episode      = $injector.get('Episode');
        $httpBackend = $injector.get('$httpBackend');

        $modalInstance = $modal.open({template: 'Not a real template'})
        episode = new Episode({});
        $rootScope.fields = {
            'microbiology_test': {
                name: 'microbiology_test',
                single: false,
                fields: [
                    { name: 'test', type: 'string' }
                ]
            }
        }

        controller = $controller('WalkinNurseInvestigationsCtrl', {
            $scope         : $scope,
            $modalInstance : $modalInstance,
            episode        : episode
        });
    }));

    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    it('Should set up an investigations object', function () {
        expect($scope.investigations).toEqual({});
    });
    
    describe('with existing tests', function (){

        beforeEach(
            inject(function($injector){
                $scope       = $rootScope.$new();
                $modal       = $injector.get('$modal');

                $modalInstance = $modal.open({template: 'Not a real template'})

                episode = new Episode({});
                test = episode.newItem('microbiology_test');
                test.test = 'Serum Save';
                episode.addItem(test);
                
                controller = $controller('WalkinNurseInvestigationsCtrl', {
                    $scope         : $scope,
                    $modalInstance : $modalInstance,
                    episode        : episode
                });
            })

        );

        
        it('Should have positive investigations when they exist', function () {
            expect($scope.investigations.serum_save).toBe(true);
        });

        it('save() Should not add a second instance of the pre-existing test', function () {
            $scope.investigations.blood_culture = true;
            
            $httpBackend.expectPOST('/api/v0.1/microbiology_test/',
                                    {test: 'Blood Culture'}).respond('yes');
            $scope.save();
            
            $httpBackend.flush();
        });
        
    });

    describe('save()', function (){
        
        it('Should create an investigation', function () {
            $scope.investigations.blood_culture = true;

            $httpBackend.expectPOST('/api/v0.1/microbiology_test/',
                                  {test: 'Blood Culture'}).respond('yes');
            $scope.save();
            $httpBackend.flush();
        });

        it('Should create multiple investigations', function () {
            $scope.investigations.blood_culture = true;
            $scope.investigations.malaria_film  = true

            $httpBackend.expectPOST('/api/v0.1/microbiology_test/', {test: 'Blood Culture'})
                .respond('yes');
            $httpBackend.expectPOST('/api/v0.1/microbiology_test/', {test: 'Malaria Film'})
                .respond('yes');

            $scope.save();
            $httpBackend.flush();
        });

        it('Should close the modal', function () {
            spyOn($modalInstance, 'close').andReturn(true);
            $scope.save();
            expect($modalInstance.close).toHaveBeenCalled();
        });        
    });

    
    describe('cancel()', function (){
        it('Should close the modal', function () {
            spyOn($modalInstance, 'close').andReturn(true);
            $scope.cancel();
            expect($modalInstance.close).toHaveBeenCalledWith('cancel');
        });
    });
    
});
