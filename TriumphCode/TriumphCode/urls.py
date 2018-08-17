"""TriumphCode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from register import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('register.urls')),
    path(r'register/', include('register.urls')),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/problems/$', views.getproblems, name='problems'),
    url(r'^dashboard/problems/viewproblems/$', views.viewproblems, name='viewproblems'),
    url(r'^dashboard/profile/editprofile', views.editprofile, name='editprofile'),
    url(r'^dashboard/status', views.user_status, name='user_status'),
    url(r'^dashboard/profile/change_password', views.change_password, name='change_password'),
    url(r'^dashboard/profile', views.profile, name='profile'),
    url(r'^dashboard/problems/viewproblems/submit', views.submit_problem, name='submit_problem'),
    url(r'^dashboard/Contest/$', views.getContests, name='contests'),
    url(r'^dashboard/Contest/problems/$', views.getContestProblems, name='contests_problem'),
    url(r'^dashboard/Contest/problems/viewproblem/$', views.contestProblem_ViewProblem, name='contests_prob_viewprob'),
    url(r'^dashboard/Contest/problems/viewproblem/submit', views.c_submit_problem, name='c_submit_problem'),
    url(r'^dashboard/Contest/prepareRankList/$', views.prepareRankList, name='prepareRankList'),
    # replace with dynamic calling
    url(r'^dashboard/Contest/getRankList/$', views.getRankList, name='getRankList'),


















    # tutorial
    url(r'^dashboard/Tutorials/$', views.tutorials, name='tutorial'),
    url(r'^dashboard/Tutorials/Sorting/$', views.sorting, name='sorting'),
    url(r'^dashboard/Tutorials/Sorting/bubblesort/$', views.bubble, name='bubble'),
    url(r'^dashboard/Tutorials/Sorting/selectionsort/$', views.selection, name='selection'),
    url(r'^dashboard/Tutorials/Sorting/insertionsort/$', views.insertion, name='insertion'),
    url(r'^dashboard/Tutorials/Sorting/mergesort/$', views.merge, name='merge'),
    url(r'^dashboard/Tutorials/Sorting/quicksort/$', views.quick, name='quick'),
    url(r'^dashboard/Tutorials/Sorting/heapsort/$', views.heap, name='heap'),
    url(r'^dashboard/Tutorials/searching/$', views.searching, name='searching'),
    url(r'^dashboard/Tutorials/searching/linearsearch/$', views.linear, name='linear'),
    url(r'^dashboard/Tutorials/searching/binarysearch/$', views.binary, name='binary'),
    url(r'^dashboard/Tutorials/searching/ternarysearch/$', views.ternary, name='ternary'),
    url(r'^dashboard/Tutorials/GreedyAlgorithm/$', views.greedy, name='greedy'),
    url(r'^dashboard/Tutorials/Graphs/$', views.graphs, name='graphs'),
    url(r'^dashboard/Tutorials/Graphs/GraphRepresentation/$', views.gr, name='gr'),
    url(r'^dashboard/Tutorials/Graphs/BFS/$', views.bfs, name='bfs'),
    url(r'^dashboard/Tutorials/Graphs/DFS/$', views.dfs, name='dfs'),
    url(r'^dashboard/Tutorials/Graphs/MinimumSpanningTree$', views.mst, name='mst'),
    url(r'^dashboard/Tutorials/DataStructures/$', views.ds, name='ds'),
    url(r'^dashboard/Tutorials/DataStructures/Arrays/$', views.arr, name='arr'),
    url(r'^dashboard/Tutorials/DataStructures/Arrays/Array/$', views.ar, name='ar'),
    url(r'^dashboard/Tutorials/DataStructures/Arrays/Multiarray/$', views.multi, name='multi'),
    url(r'^dashboard/Tutorials/DataStructures/linklist/$', views.linklist, name='linklist'),
    url(r'^dashboard/Tutorials/DataStructures/Stacks/$', views.stacks, name='stacks'),
    url(r'^dashboard/Tutorials/DataStructures/queues/$', views.queues, name='queues'),
    url(r'^dashboard/Tutorials/stacksandqueues/$', views.sq, name='sq'),
    url(r'^dashboard/Tutorials/stacksandqueues/Stacks/$', views.stack, name='stack'),
    url(r'^dashboard/Tutorials/stacksandqueues/queues/$', views.queue, name='queue'),
    url(r'^dashboard/Tutorials/Bitmanipulation/$', views.bm, name='bm'),
    url(r'^dashboard/Tutorials/Bitmanipulation/Basics/$', views.basics, name='basics'),
    url(r'^dashboard/Tutorials/Bitmanipulation/DPANDBP/$', views.dpbp, name='dpbp'),
    url(r'^dashboard/Tutorials/dynamicprogramming/$', views.dynamic, name='dynamic'),
    url(r'^dashboard/Tutorials/dynamicprogramming/Introdynamicprogramming/$', views.indynamic, name='indynamic'),
    url(r'^dashboard/Tutorials/dynamicprogramming/Dimensional/$', views.dimension, name='dimension'),







]
