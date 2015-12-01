describe('WalkinHospitalNumberCtrl', function (){
    "use strict";
    var $controller, $scope, $modalInstance, $httpBackend, $rootScope;
    var schema, options, tags, Episode;

    beforeEach(module('opal.controllers'));

    beforeEach(inject(function($injector){
        var $modal   = $injector.get('$modal');
        $rootScope   = $injector.get('$rootScope');
        $scope       = $rootScope.$new();
        $controller  = $injector.get('$controller');
        Episode      = $injector.get('Episode');
        $httpBackend = $injector.get('$httpBackend');

        $modalInstance = $modal.open({template: 'Not a real template'})
        schema = {}
        options = {}

        $rootScope.fields = {
            'microbiology_test': {
                name: 'microbiology_test',
                single: false,
                fields: [
                    { name: 'test', type: 'string' },
                    { name: 'date_ordered', type: 'date' }
                ]
            },
            'management': {
                name: 'management',
                single: false,
                fields : [
                    { name: 'date_of_appointment', type: 'date' }
                ]
            }
        }

        var controller = $controller('WalkinHospitalNumberCtrl', {
            $scope         : $scope,
            $modalInstance : $modalInstance,
            schema         : schema,
            options        : options,
            tags           : tags
        });
    }));

    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });


    describe('tag_and_close()', function (){

        it('Should save and close', function () {
            var episode  = {
                id: '3',
                date_of_episode: moment().format('DD/MM/YYYY'),
                category: 'Walkin'
            };
            $httpBackend.expectPUT('/episode/3/', episode).respond(episode);

            var test = {test: 'HIV Point of Care', episode_id: "3"};
            $httpBackend.expectPOST('/api/v0.1/microbiology_test/', test).respond(test);
            var episode = {id: '3'};

            spyOn($modalInstance, 'close');

            $scope.tag_and_close(episode);
            $httpBackend.flush();

            expect($modalInstance.close).toHaveBeenCalled();
        });

    });


});
