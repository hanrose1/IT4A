from ..serializers import StudentSerializer
from rest_framework import mixins, generics
from students.models import Student

#extend ->  mixin to list data(GET requests), createmodel(POST requests) generic(queryset, serializer_class)-> para magamit ang variables ug methods
class Students(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #fetch data from databse - assign to queryset variable
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #When someone visits the endpoint with GET mu trigger dayon and return list
    #Example: call /employee/ -> mudagan ang get() -> tawagon dayon ang list() -> then si list() mu fetch ug employee, iconvert dayun using serializer to JSON -> return response
    def get(self, request):
        return self.list(request)
    
    #when naay mu send ug POST request
    #Example: Client send data -> post() run -> call create() -> i check dayon ni create() kung valid -> saves to database -> return saved data as JSON
    def post(self, request):
        return self.create(request)
    
class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #iretrieve niya from retrive model, pangitaon dayon niya ang ID number -> convert JSON ->return
    def get (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)