from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,DeleteView,UpdateView
from django.views import View
from log.models import School
from django.urls import reverse_lazy
from log.forms import AddSchoolForm,EditSchoolForm



class HomeView(View):
    def get(self,request):
        m = School.objects.all()
        return render(request,'home.html',{'school':m})

class SchoolDetailView(DetailView):
    model = School
    template_name = 'school_detail.html'
    context_object_name = 'school'
    pk_url_kwarg = 'id'


class SchoolDelete(DeleteView):
    model = School
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('log:HomeView')
    template_name = 'movie_confirm_delete.html'

class SchoolEditView(UpdateView):
    model = School
    form_class = EditSchoolForm
    template_name = 'edit_school.html'
    success_url = reverse_lazy('log:HomeView')
    pk_url_kwarg = 'id'

class AddSchool(View):
    def get(self,request):
        form = AddSchoolForm()
        return render(request,'add_school.html',{'form':form})

    def post(self,request):
        if (request.method == 'POST'):
            name = request.POST.get('name')
            adrs = request.POST.get('address')
            pop = request.POST.get('population')
            fac = request.POST.get('faculty')
            det = request.POST.get('details')

            c = School.objects.create(name=name, address=adrs, population=pop, faculty=fac,details=det)
            c.save()
            return redirect('log:HomeView')
