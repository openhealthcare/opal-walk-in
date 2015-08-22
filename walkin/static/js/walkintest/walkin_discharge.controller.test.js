describe('WalkinDischargeCtrl', function(){
    var $controller, $scope, $modalInstance, $httpBackend, $rootScope, $modal, $q;
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
        $q           = $injector.get('$q');

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
        var open_deferred;
        beforeEach(function(){
            $httpBackend.expectGET('/api/v0.1/userprofile/').respond({});

            open_deferred = $q.defer();
            spyOn($modal, 'open').and.callFake(function(){
                return {result: open_deferred.promise } 
            });
            spyOn($modalInstance, 'close');
            spyOn($scope, 'cancel').and.callThrough();
        });
        
        it('Should open Edit item with a management item', function () {
            $scope.move_to_management();
            modal_opts = $modal.open.calls.mostRecent().args[0];
            expect(modal_opts.templateUrl).toBe('/templates/modals/management.html');
            expect(modal_opts.controller).toBe('EditItemCtrl');
            expect(modal_opts.resolve.item().columnName).toBe('management');
            $httpBackend.flush();
        });

        it('Should close the modal', function () {
            $scope.move_to_management();
            expect($modalInstance.close).toHaveBeenCalled();
            $httpBackend.flush();
        });

        it('Should close the modal with a deferred', function () {
            $scope.move_to_management();
            expect($modalInstance.close.calls.mostRecent().args[0].then).toBeDefined();
            $httpBackend.flush()
        });

        it('Should resolve the deferred when edititem closes', function () {
            $scope.move_to_management();
            var returned_deferred = $modalInstance.close.calls.mostRecent().args[0];
            dummy = jasmine.createSpy('function()');
            
            returned_deferred.then(dummy);
            expect(dummy).not.toHaveBeenCalled();
            open_deferred.resolve();
            $scope.$digest(); // Fire actual resolving
            expect(dummy).toHaveBeenCalled();
            $httpBackend.flush();
        });
        
    });
    
});
