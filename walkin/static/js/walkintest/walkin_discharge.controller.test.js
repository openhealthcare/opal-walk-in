describe('WalkinDischargeCtrl', function(){
    var $controller, $scope, $modalInstance, $httpBackend, $rootScope, $modal;
    var Episode;
    var options, episode, tags;

    beforeEach(module('opal.controllers'));

    beforeEach(inject(function($injector){
        today = moment();
        
        $rootScope   = $injector.get('$rootScope');
        $scope       = $rootScope.$new();
        $modal       = $injector.get('$modal');
        $controller  = $injector.get('$controller');
        Episode      = $injector.get('Episode');
        $httpBackend = $injector.get('$httpBackend');

        $modalInstance = $modal.open({template: 'Not a real template'});
        schema = {};
        tags = {};
        episode = new Episode({});
        
        $rootScope.fields = {
            'management': {
                name: 'management',
                single: false,
                fields : [
                    { name: 'date_of_appointment', type: 'date' }
                ]
            }
        }
        
        controller = $controller('WalkinDischargeCtrl', {
            $scope         : $scope,
            $modalInstance : $modalInstance,
            options        : options,
            tags           : tags,
            episode        : episode
        });
    }));

    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    
    describe('move_to_management()', function (){
        beforeEach(function(){
            $httpBackend.expectGET('/api/v0.1/userprofile/').respond({});
            spyOn($modal, 'open');
            spyOn($scope, 'cancel');
        });
        
        it('Should open Edit item with a management item', function () {
            $scope.move_to_management();
            modal_opts = $modal.open.mostRecentCall.args[0];
            expect(modal_opts.templateUrl).toBe('/templates/modals/management.html');
            expect(modal_opts.controller).toBe('EditItemCtrl');
            expect(modal_opts.resolve.item().columnName).toBe('management');
            $httpBackend.flush();
        });

        it('Should close the modal', function () {
            $scope.move_to_management();
            expect($scope.cancel).toHaveBeenCalledWith();
            $httpBackend.flush();
        });
    });
    
});
