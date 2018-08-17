$(function(){



      var pro = JSON.parse(document.getElementById("contest").innerHTML)
      console.log(pro);

for(var i = 0, size = pro.length; i < size ; i++){

var divc = document.createElement("div");
divc.setAttribute("id", "divc" + (i+1));
divc.setAttribute("class", "w3-panel w3-border w3-round-xlarge");
document.getElementById("contest_des").appendChild(divc);

var head = document.createElement("section");
head.setAttribute("id", "head" + (i+1));
head.setAttribute("class", "special box");
divc.appendChild(head);



var pro_head = document.createElement("h2");
pro_head.setAttribute("id", "pro_head" + (i+1));
head.appendChild(pro_head);

var pd = document.createElement("label");
pd.setAttribute("id", "pro_des" + (i+1));
head.appendChild(pd);

var st = document.createElement("label");
st.setAttribute("id", "st" + (i+1));
head.appendChild(st);

var d = document.createElement("label");
d.setAttribute("id", "dur" + (i+1));
head.appendChild(d);

var time = document.createElement("label");
time.setAttribute("id", "timer" + (i+1));
head.appendChild(time);

var sn = document.createElement("label");
sn.setAttribute("id", "snb" + (i+1));
head.appendChild(sn);

var lb = document.createElement("label");
lb.setAttribute("id", "lb" + (i+1));
head.appendChild(lb);


}

for(var i = 0, size = pro.length; i < size ; i++){
   var item = pro[i];
   console.log(item["cid"] + " " + item["cname"]);

//   var problem_index0 = document.createElement("label");
  // var node = document.createTextNode((i+1) + "         ");
   //problem_index0.appendChild(node);



   var problem_index = document.createElement("label");
   node = document.createTextNode(pro[i]["cname"] + "          ");
   problem_index.setAttribute("style", "font-family: Comic Sans MS, cursive, sans-serif;");
   problem_index.appendChild(node);

   element = document.getElementById("pro_head" + (i+1));
   element.appendChild(problem_index);


   var problem_index2 = document.createElement("label");
   node = document.createTextNode(pro[i]["cdescription"] + "          ");
   problem_index2.appendChild(node);

   element = document.getElementById("pro_des" + (i+1));
   element.appendChild(problem_index2);

   var temp = document.createElement("br");
   element.appendChild(temp);


   var problem_index3 = document.createElement("label");
   node = document.createTextNode("Starts on : " + pro[i]["cstarttime"].slice(0,19));
   problem_index3.appendChild(node);

   element = document.getElementById("st" + (i+1));
   element.appendChild(problem_index3);

   var problem_index4 = document.createElement("label");
   node = document.createTextNode(pro[i]["cduration"] + "          ");
   problem_index4.appendChild(node);

   element = document.getElementById("dur" + (i+1));
   element.appendChild(problem_index4);

   var problem_index5 = document.createElement("p");
   node = document.createTextNode(" ");
   problem_index5.setAttribute("id", pro[i]["cid"]);
   problem_index5.appendChild(node);

   element = document.getElementById("timer" + (i+1));
   element.appendChild(problem_index5);


   var startnow = document.createElement("a");
   node = document.createTextNode("Start Now    ");
   startnow.setAttribute("id", "start_" + pro[i]["cid"]);
   startnow.setAttribute("class", "button_a");
   startnow.setAttribute("href", "problems/?cid=" + pro[i]["cid"]);
   startnow.setAttribute("style", "display:none");
   startnow.setAttribute("value", "Start Now");
   startnow.appendChild(node);

   element = document.getElementById("snb" + (i+1));
   element.appendChild(startnow);

   var leaderboard = document.createElement("a");
   node = document.createTextNode("Leaderboard");
   leaderboard.setAttribute("id", "rank_" + pro[i]["cid"]);
   leaderboard.setAttribute("href", "http://localhost:8000/dashboard/Contest/getRankList/?cid=" + pro[i]["cid"]);
   leaderboard.setAttribute("class", "button_a");
   leaderboard.setAttribute("style", "display:none");
   leaderboard.setAttribute("value", "Leaderboard");
   leaderboard.appendChild(node);

   element = document.getElementById("lb" + (i+1));
   element.appendChild(leaderboard);




}


    //alert();



    //timer(2,"2018-03-14 20:21:25");
for(var i = 0, size = pro.length; i < size ; i++){

       timer(pro[i]["cid"],pro[i]["cstarttime"].slice(0,19),pro[i]["cduration"]);

}


    function timer(element,time,duration)
    {
         var countDownDate = new Date(time).getTime();

// Update the count down every 1 second
         var x = setInterval(function() {

    // Get todays date and time
         var now = new Date().getTime();

    // Find the distance between now an the count down date
         var distance = countDownDate - now;
         //console.log(distance);

    // Time calculations for days, hours, minutes and seconds
         var days = Math.floor(distance / (1000 * 60 * 60 * 24));
         var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
         var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
         var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
        document.getElementById(element).innerHTML = days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";

    // If the count down is over, write some text
        if (distance < 0) {

            document.getElementById(element).innerHTML = "Started";
            $("#start_"+element).attr("style","display:block");

           // alert("fff");

           if (-distance > duration*60*60*1000) {
                clearInterval(x);
                document.getElementById(element).innerHTML = "Ended";
                $("#start_"+element).attr("style","display:none");
                $("#rank_"+element).attr("style","display:block");
           // alert("fff");

           // ranklist;

            $.ajax(
            {
                 type: "GET",
                 url: "/dashboard/Contest/prepareRankList",
                 data:{
                    "cid":element,
                 },
                 success: function( data )
                {

                     //alert("animesh ullu");
                     console.log(data);
                     console.log("cool");
                }
            })


            }


        }



        }, 1000);


    }




});