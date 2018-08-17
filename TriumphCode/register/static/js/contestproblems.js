$(function(){


      var cdata=JSON.parse(document.getElementById("cdata").innerHTML)
      var pro = JSON.parse(document.getElementById("contest").innerHTML)
   //            var pro = JSON.parse(document.getElementById("kutta").innerHTML)
             console.log(pro);

            //$("#abc").text("title:  " + x[0]);
            console.log(pro[0]["pid_id__pname"]);

//var txt = "";
var x;
for (x in pro) {
    console.log(pro[x]["pid_id__pid"]);
}



var table = document.createElement("table");
table.setAttribute("id", "display_table");
document.getElementById("problems_container").appendChild(table);

var trh = document.createElement("tr");
trh.setAttribute("id", "table_head");
table.appendChild(trh);

var no = document.createElement("th");
var node = document.createTextNode("S.No.");
no.appendChild(node);
trh.appendChild(no);

var problem_name = document.createElement("th");
node = document.createTextNode("Problem");
problem_name.appendChild(node);
trh.appendChild(problem_name);

var problem_key = document.createElement("th");
node = document.createTextNode("Problem Key");
problem_key.appendChild(node);
trh.appendChild(problem_key);

for(var i = 0, size = pro.length; i < size ; i++){

	var tr = document.createElement("tr");
	tr.setAttribute("id", "tr" + (i+1) );
    table.appendChild(tr);


	var td1 = document.createElement("td");
	td1.setAttribute("id", "td" + (i+1) + "1");
    tr.appendChild(td1);

	var td2 = document.createElement("td");
	td2.setAttribute("id", "td" + (i+1) + "2");
    tr.appendChild(td2);

	var td3 = document.createElement("td");
	td3.setAttribute("id", "td" + (i+1) + "3");
    tr.appendChild(td3);




}







for(var i = 0, size = pro.length; i < size ; i++){
   var item = pro[i];
   console.log(item["pid_id__pid"] + " " + item["pid_id__pname"]);

   var problem_index0 = document.createElement("label");
   var node = document.createTextNode((i+1));
   problem_index0.appendChild(node);

   element = document.getElementById("td" + (i+1) + "1");
   element.appendChild(problem_index0);


   var problem_index = document.createElement("a");
   node = document.createTextNode(pro[i]["pid_id__pname"] + "          ");
   problem_index.setAttribute("href", "viewproblem/?pid=" + pro[i]["pid_id__pid"]+"&cid="+cdata[0]["cid"]);
   problem_index.setAttribute("id", pro[i]["pid_id__pid"]);
   problem_index.setAttribute("value", pro[i]["pid_id__pname"]);
   problem_index.appendChild(node);

   element = document.getElementById("td" + (i+1) + "2");
   element.appendChild(problem_index);

   var problem_index2 = document.createElement("label");
   var node = document.createTextNode(pro[i]["pid_id__pkey"] + "          ");
   problem_index2.appendChild(node);

   element = document.getElementById("td" + (i+1) + "3");
   element.appendChild(problem_index2);




}


    timer("time",cdata[0]["cstarttime"].slice(0,19),cdata[0]["cduration"]);




    function timer(element,time,duration)
    {

         var countDownDate = new Date(time).getTime();
         countDownDate=countDownDate+duration*3600*1000;
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

            document.getElementById(element).innerHTML = "";
            clearInterval(x);
//            $("#start_"+element).attr("style","display:block");
            alert("Contest Over!!!");
           // alert("fff");



        }



        }, 1000);


    }





});