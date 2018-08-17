from django.shortcuts import render, redirect
from register.forms import SignUpForm, EditProfileForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import problems, users_problem, competitions, competition_problems, user_competition_problems,score_user
from django.contrib.auth.decorators import login_required
import json, requests
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signuppage(request):
    return render(request, 'register/signup.html')

@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/')
def editor(request):
    return render(request, 'editor.html')

@login_required(login_url='/')
def getproblems(request):

    data2 = request.GET
    print(data2)

    print("####")
    print(data2['level'])
    #data1 = data2.dict()
    #print(data2)
    #a = list(data1.values())
    data23 = problems.objects.filter(plevel=data2['level']).values("pid", "pkey","pname", "ptag");
    data24= list(data23)
    data2=json.dumps(data24)
    print(data2)
    #jsondata=json.dumps(data1)
    #print(len(a))
    #print(a[0])

    context={
        "name":"problemset",
        "data":data2,
    }
    return render(request,'problems.html', context)


#    render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register/signup.html', {'form': form})

@login_required(login_url='/')
def submit(request):

    print("**********\n")
    data1 = request.POST
    code = data1['code']
    print(code)
    input1 = data1['input1']
    print(input1)
    print(data1)
    RUN_URL = "https://api.jdoodle.com/v1/execute"
    CLIENT_ID = 'f9b593e45b8113057f5cee59c48960e4'

    CLIENT_SECRET = 'd381c91b1469a0cfe8abdc3dbf9ecc9833b9dff6350afe2e9006821f0069badb'
    #source = open('c:/users/KD/Desktop/abcd.c', 'r')
    #input = open('c:/users/KD/Desktop/input.txt', 'r')
    data = {
        "clientId" : "f9b593e45b8113057f5cee59c48960e4",
        "clientSecret": "d381c91b1469a0cfe8abdc3dbf9ecc9833b9dff6350afe2e9006821f0069badb",
        "script": code,
        "stdin" : input1,
        "language": data1['lang'],


    }
    print(type(data))
    data=json.dumps(data)
    print(type(data))
    headers = {'Content-type': 'application/json'}
    data = requests.post(url=RUN_URL, data=data, headers=headers).json()
    print(data)
    return JsonResponse(data)

@login_required(login_url='/')
def viewproblems(request):
    data1=request.GET
    data2=data1.dict()
    requestedproblem1 = problems.objects.filter(pk=data2['pid']).values()[0]
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #print(type(requestedproblem))
    requestedproblem=json.dumps(requestedproblem1)
    context = {
        "name": "problemset",
        "data": requestedproblem,
    }
    print(context)
    return render(request, 'viewproblems.html', context)


@login_required
def profile(request):
    args = { 'user': request.user}
    return render(request, 'register/profile.html', args)

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'register/editprofile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('profile'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'register/change_password.html', args)

@login_required
def user_status(request):
    args = {
        'data':'hello',
    }
    if request.user.is_authenticated:
        username = request.user.id #default filed for id
        request1=request.user
        print(username)
    return render(request, 'user_status.html', args)


def submit_problem(request):
    #code updating db after poblem is subm
    print("**********\n")
    data = request.POST
    print(data)
    problem_id=data['pid']
    user_id = request.user.id
    value=problems.objects.filter(pid=problem_id).values("pinput", "poutput");
    print(value[0])

    code = data['code']

    input = value[0]['pinput'].replace('\r', '') #database se fetch
    output= value[0]['poutput']
    print(output)
    output=output.replace('\r', '')
    output = output.replace('\n', '')
    print(input)
    print(output)

    lang=data['lang']
    print(lang)

    RUN_URL = "https://api.jdoodle.com/v1/execute"
    CLIENT_SECRET = 'f1a22b13834ca4da7574a335438d3cf3247d9956'

    data = {
        "clientId" : "f9b593e45b8113057f5cee59c48960e4",
        "clientSecret": "d381c91b1469a0cfe8abdc3dbf9ecc9833b9dff6350afe2e9006821f0069badb",
        "script": code,
        "stdin" : input,
        "language": lang,


    }

    data=json.dumps(data)

    headers = {'Content-type': 'application/json'}

    data = requests.post(RUN_URL, data=data, headers=headers).json()
    c_output=data['output']
    print("cdvcdfgbhdbcdshicfgbsdhdsbgfhjdgfhdf")

    c_output = c_output.replace('\n', '')
    print(c_output)
    status = output == c_output
    print(status)
    if status:
        user = User.objects.get(id=user_id)
        problem = problems.objects.get(pid=problem_id)

        record = users_problem(uid=user, pid=problem)
        record.save()
        return JsonResponse({"compile_error": "YES"})
    else :
        return JsonResponse({"status": c_output,"compile_error": "NO"})


    """
    if data['compile_status'] == 'OK':
        print(data)
        c_output_dict=data['run_status']
        c_output=c_output_dict['output']
        c_output = c_output.replace('\n', '')
        # print(c_output)
        # print(type(c_output))
        # print(type(output))

        d={
            'a': output,
            'b': c_output,
        }
        print (d)
        #print(output==c_output['output'])
        status=output==c_output
        if status:
            user = User.objects.get(id = user_id)
            problem = problems.objects.get(pid=problem_id)

            record = users_problem(uid=user, pid=problem)
            record.save()


        return JsonResponse({"status": status, "compile_error":"NO"})

    else:
        print("error")
        return JsonResponse({"compile_error":"YES"})
    """

def getContests(request):

    #data23 = competitions.objects.all().values()

    #data2 = json.dumps(data23, default=str)  # need to remember the datetime format while deserializing
    #print(data2)
    #data23 = competitions.objects.filter(cid=1).values("cid", "cname", "cdescription","cduration","cstarttime");
    data23 = competitions.objects.all().values()
    data24 = list(data23)
    data2 = json.dumps(data24,default=str)

    context = {
        "name": "contest",
        "data":data2,
    }

    return render(request, 'contest.html', context)


def getContestProblems(request):

    #var=problems.objects.filter(cid=1)
    #print(var)
    #print("*************")
    #requestedcontestproblems = competition_problems.objects.filter(cid=1).values()
    data = request.GET
    print(data)
    requestedcontestproblems = competition_problems.objects.filter(cid=data['cid']).values("pid_id__pid","pid_id__pname","pid_id__pkey", "cpscore","cid")
    #print(requestedcontestproblems)
    # replace by pk=data11['cid']

    data2 = json.dumps(list(requestedcontestproblems), default=str)
    data4 = competitions.objects.filter(cid=data['cid']).values("cid","cstarttime","cduration")
    data4 = json.dumps(list(data4), default=str)

    context = {
        "name": "problemset",
        "data": data2,
        "cdata":data4,
    }

    return render(request, 'contest_problems.html', context)



def contestProblem_ViewProblem(request):

    data = request.GET
    print(data)
    print("*********")
    print(problems.objects.filter(pk=data['pid']).values())

    requestedproblem1 = problems.objects.filter(pk=data['pid']).values()[0]
    # to be replaced by pk=data2['pid']
    requestedproblem = json.dumps(requestedproblem1)
    data4 = competitions.objects.filter(cid=data['cid']).values("cid", "cstarttime", "cduration")
    data4 = json.dumps(list(data4), default=str)

    context = {
        "name": "problemset",
        "data": requestedproblem,
        "cdata": data4,
    }

    return render(request, 'c_problem_viewproblem.html', context)


def c_submit_problem(request):
    #code updating db after poblem is subm
    print("**********\n")
    data = request.POST
    print(data)
    cid=data['cid']
    problem_id=data['pid']
    user_id = request.user.id
    value=problems.objects.filter(pid=problem_id).values("pinput", "poutput");
    print(value[0])

    code = data['code']

    input = value[0]['pinput'].replace('\r', '') #database se fetch
    output= value[0]['poutput']
    output=output.replace('\r', '')
    output = output.replace('\n', '')
    print(input)
    print(output)

    lang=data['lang']
    print(lang)

    RUN_URL = "https://api.jdoodle.com/v1/execute"
    CLIENT_SECRET = 'f1a22b13834ca4da7574a335438d3cf3247d9956'

    data = {
        "clientId": "f9b593e45b8113057f5cee59c48960e4",
        "clientSecret": "d381c91b1469a0cfe8abdc3dbf9ecc9833b9dff6350afe2e9006821f0069badb",
        "script": code,
        "stdin": input,
        "language": lang,

    }

    data = json.dumps(data)

    headers = {'Content-type': 'application/json'}

    data = requests.post(RUN_URL, data=data, headers=headers).json()
    c_output = data['output']
    print(c_output)
    c_output = c_output.replace('\n', '')

    status = output == c_output
    print(status)
    if status:

        user = User.objects.get(id=user_id)

        problem = problems.objects.get(pid=problem_id)
        competition = competitions.objects.get(cid=cid)
        record = user_competition_problems(uid=user, pid=problem, cid=competition)
        print("cxcx")
        print(user)
        record.save()
        return JsonResponse({"compile_error": "YES"})
    else :
        return JsonResponse({"status": c_output, "compile_error": "NO"})

"""
    if data['compile_status'] == 'OK':
        print(data)
        c_output_dict=data['run_status']
        c_output=c_output_dict['output']
        c_output = c_output.replace('\n', '')
        # print(c_output)
        # print(type(c_output))
        # print(type(output))

        d={
            'a': output,
            'b': c_output,
        }
        print (d)
        #print(output==c_output['output'])
        status=output==c_output
        if status:
            user = User.objects.get(id = user_id)
            problem = problems.objects.get(pid=problem_id)
            competition= competitions.objects.get(competition_id=cid)

            record = user_competition_problems(uid=user, pid=problem,cid=competition)
            record.save()


        return JsonResponse({"status": status, "compile_error":"NO"})

    else:
        print("error")
        return JsonResponse({"compile_error":"YES"})

"""

@login_required
def user_status(request):

    if request.user.is_authenticated:
        userid = request.user.id #default filed for id
        request1=request.user
        print(request1.username)
        print(request1)

        #fetchUserProblems1 = problems.objects.filter(pid=users_problem.objects.filter(uid=userid).values()[0]['uid_id'])
        fetchUserProblems1 = users_problem.objects.filter(uid=userid).values('uid', 'pid_id__pname')
        # fetchUserProblems1 = users_problem.objects.all).select_related("pid")
        # print(fetchUserProblems1.pname)
        #fetchUserCompetitions1 = user_competition_problems.objects.filter(uid=userid).values()[0]
        fetchUserCompetitions1 = user_competition_problems.objects.filter(uid=userid).values('uid', 'cid_id__cname', 'pid_id__pname')
        fetchUserProblems = json.dumps(list(fetchUserProblems1), default=str)
        fetchUserCompetitions = json.dumps(list(fetchUserCompetitions1), default=str)

        args = {
            'problemStatus': fetchUserProblems,
            'competitionStatus': fetchUserCompetitions,
        }
    return render(request, 'user_status.html', args)



def prepareRankList(request):
    i=1
    rdata = request.GET

    competitionidd = rdata['cid']#this is hardcoded. has to be replaced
    problems_by_user1 = user_competition_problems.objects.filter(cid=competitionidd).values()
    #print(problems_by_user1)
    checkuserscorerecord = score_user.objects.filter(competitionid_id=competitionidd).exists()
    if checkuserscorerecord:
        print('hao')

        return JsonResponse({"prepared":"YES"})
    problems_by_user = list(problems_by_user1)
    print(problems_by_user)


    for eachproblem in problems_by_user:
        #eachproblem is a dictionary
        print("issues")

        addscore1 = competition_problems.objects.filter(cid_id = competitionidd).filter(pid_id=eachproblem['pid_id']).values('cpscore')[0]
        addscore = int(addscore1['cpscore'])
        # createuserscorerecord = score_user_temp()
        # createuserscorerecord.competitionid = 2
        #
        # createuserscorerecord.userid = 2
        # createuserscorerecord.score = 50
        # print(createuserscorerecord)
        # createuserscorerecord.save()
        # createuserscorerecord = score_user()
        # createuserscorerecord.competitionid_id = competitionidd
        # createuserscorerecord.userid_id = 4
        # '''eachproblem['uid_id']'''
        # createuserscorerecord.score = addscore
        # print(createuserscorerecord)
        # createuserscorerecord.save()
        # print(addscore )
        #
        # createuserscorerecord = score_user_temp()
        # createuserscorerecord.competitionid = competitionidd
        #
        # createuserscorerecord.userid = eachproblem['uid_id']
        # createuserscorerecord.score = 50
        # print(createuserscorerecord)
        # createuserscorerecord.save()
        check =  score_user.objects.filter(competitionid_id=competitionidd).filter(userid_id=eachproblem['uid_id']).exists()
        print(check)
        if check:
            print('whaaaaaaaaaaaat')
            scorevar1 =score_user.objects.filter(competitionid_id=competitionidd).filter(userid_id=eachproblem['uid_id']).values('score')[0]
            print(scorevar1)
            scorevar = int(scorevar1['score'])
            #print(scorevar+addscore)
            getuserrecord = score_user.objects.filter(competitionid_id=competitionidd).filter(userid_id=eachproblem['uid_id']).update(score=(scorevar + addscore))
            # getuserrecord.score=scorevar + addscore
            # getuserrecord.save()
            print(getuserrecord)
        else:
            # referencetocompetition = competitions(cid =competitionidd )
            # referencetouser = User(pk=eachproblem['uid_id'])
            print('whyyyyyyyyyyyy')
            createuserscorerecord = score_user()
            #createuserscorerecord.id = i
            #i=i+1
            createuserscorerecord.competitionid_id = competitionidd

            createuserscorerecord.userid_id = eachproblem['uid_id']
            createuserscorerecord.score = addscore
            print(createuserscorerecord)
            createuserscorerecord.save()
        #
        #     createuserscorerecord = score_user()
        #     createuserscorerecord.competitionid = competitionidd
        #     createuserscorerecord.userid_id = 4
        #     '''eachproblem['uid_id']'''
        #     createuserscorerecord.score = addscore
        #     print(createuserscorerecord)
        #     createuserscorerecord.save()


    return JsonResponse({"prepared":"YES"})


def getRankList(request):
    rdata = request.GET

    competitionidd=rdata['cid']
    print('prepare')
    currentRankList1 = score_user.objects.filter(competitionid = competitionidd).values('competitionid_id__cname', 'userid_id__username','score').order_by('-score')
    currentRankList = list(currentRankList1)
    currentRankList = json.dumps(currentRankList)
    print(type(currentRankList))
    args = {
        'rankList': currentRankList,
    }
    #args={}
    return render(request, 'RankList.html', args)









































#tutorials

@login_required(login_url='/')
def tutorials(request):
    return render(request, 'tutorial/Tutorials.html')


@login_required(login_url='/')
def sorting(request):
    return render(request, 'tutorial/Sorting.html')

@login_required(login_url='/')
def bubble(request):
    return render(request, 'tutorial/bubblesort.html')

@login_required(login_url='/')
def selection(request):
    return render(request, 'tutorial/selectionsort.html')

@login_required(login_url='/')
def insertion(request):
    return render(request, 'tutorial/insertionsort.html')

@login_required(login_url='/')
def merge(request):
    return render(request, 'tutorial/mergesort.html')

@login_required(login_url='/')
def quick(request):
    return render(request, 'tutorial/quicksort.html')

@login_required(login_url='/')
def heap(request):
    return render(request, 'tutorial/heapsort.html')

@login_required(login_url='/')
def searching(request):
    return render(request, 'tutorial/searching.html')

@login_required(login_url='/')
def linear(request):
    return render(request, 'tutorial/linearsearch.html')

@login_required(login_url='/')
def binary(request):
    return render(request, 'tutorial/binarysearch.html')

@login_required(login_url='/')
def ternary(request):
    return render(request, 'tutorial/ternarysearch.html')

@login_required(login_url='/')
def greedy(request):
    return render(request, 'tutorial/GreedyAlgorithm.html')

@login_required(login_url='/')
def graphs(request):
    return render(request, 'tutorial/Graphs.html')

@login_required(login_url='/')
def gr(request):
    return render(request, 'tutorial/GraphRepresentation.html')

@login_required(login_url='/')
def bfs(request):
    return render(request, 'tutorial/BFS.html')

@login_required(login_url='/')
def dfs(request):
    return render(request, 'tutorial/DFS.html')

@login_required(login_url='/')
def mst(request):
    return render(request, 'tutorial/MinimumSpanningTree.html')

@login_required(login_url='/')
def ds(request):
    return render(request, 'tutorial/DataStructures.html')

@login_required(login_url='/')
def arr(request):
    return render(request, 'tutorial/Arrays.html')

@login_required(login_url='/')
def ar(request):
    return render(request, 'tutorial/Array.html')

@login_required(login_url='/')
def multi(request):
    return render(request, 'tutorial/Multiarray.html')

@login_required(login_url='/')
def linklist(request):
    return render(request, 'tutorial/linklist.html')

@login_required(login_url='/')
def stacks(request):
    return render(request, 'tutorial/Stacks.html')

@login_required(login_url='/')
def queues(request):
    return render(request, 'tutorial/queues.html')

@login_required(login_url='/')
def sq(request):
    return render(request, 'tutorial/stacksandqueues.html')

@login_required(login_url='/')
def stack(request):
    return render(request, 'tutorial/Stacks.html')

@login_required(login_url='/')
def queue(request):
    return render(request, 'tutorial/queues.html')

@login_required(login_url='/')
def bm(request):
    return render(request, 'tutorial/Bitmanipulation.html')

@login_required(login_url='/')
def basics(request):
    return render(request, 'tutorial/Basics.html')

@login_required(login_url='/')
def dpbp(request):
    return render(request, 'tutorial/DPANDBP.html')

@login_required(login_url='/')
def dynamic(request):
    return render(request, 'tutorial/dynamicprogramming.html')

@login_required(login_url='/')
def indynamic(request):
    return render(request, 'tutorial/Introdynamicprogramming.html')

@login_required(login_url='/')
def dimension(request):
    return render(request, 'tutorial/Dimensional.html')