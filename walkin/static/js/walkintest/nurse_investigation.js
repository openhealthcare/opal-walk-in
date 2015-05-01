describe('WalkinNurseInvestigationsCtrl', function (){
    var $controller, $scope, $modalInstance, $httpBackend, episode;

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

    describe('save()', function (){
        
        it('Should create an investigation', function () {
            $scope.investigations.blood_culture = true;

            $httpBackend.whenPOST('/api/v0.1/microbiology_test/',
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
});
