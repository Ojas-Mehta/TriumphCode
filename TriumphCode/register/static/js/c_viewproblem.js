$(function(){

             var pro = JSON.parse(document.getElementById("contest").innerHTML)
             var cdata=JSON.parse(document.getElementById("cdata").innerHTML)
             console.log(pro);
             console.log(cdata);

var pname = document.createElement("h2");
pname.setAttribute("id", "pname");
var node = document.createTextNode(pro["pname"]);
pname.appendChild(node);
document.getElementById("view_problems_container").appendChild(pname);

var x = pro["pstatement"];
//var res = x.replace("&lt;","<");
var res = x.split("&lt;").join("<");
res = res.split("&gt;").join(">");


var pstatement = document.createElement("p");
pstatement.setAttribute("id", "pstatement");
node = document.createTextNode(res);
pstatement.appendChild(node);
document.getElementById("view_problems_container").appendChild(pstatement);

var l1 = document.createElement("label");
l1.setAttribute("id", "poutput");
node = document.createTextNode("Input  : ");
l1.appendChild(node);
document.getElementById("view_problems_container").appendChild(l1);

var pinput = document.createElement("p");
pinput.setAttribute("id", "pinput");
node = document.createTextNode(pro["pinput"]);
pinput.appendChild(node);
document.getElementById("view_problems_container").appendChild(pinput);

var l2 = document.createElement("label");
l2.setAttribute("id", "poutput");
node = document.createTextNode("Output  : ");
l2.appendChild(node);
document.getElementById("view_problems_container").appendChild(l2);

var poutput = document.createElement("p");
poutput.setAttribute("id", "poutput");
node = document.createTextNode(pro["poutput"]);
poutput.appendChild(node);
document.getElementById("view_problems_container").appendChild(poutput);



             timer("time",cdata[0]["cstarttime"].slice(0,19),cdata[0]["cduration"]);



});

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

          //  alert("ak6");
            document.getElementById(element).innerHTML = "Contest Over!!!";
            clearInterval(x);
            //$("#start_"+element).attr("style","display:block");
            //alert("Contest Over!!!");
            $("#lang").attr("style","display:none");
            $("#submit").attr("style","display:none");

           // alert("fff");



        }


        }, 1000);


}





