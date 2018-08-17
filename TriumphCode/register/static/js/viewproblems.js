$(function(){


      var pro = JSON.parse(document.getElementById("problem_data").innerHTML)
             console.log(pro);

            console.log(pro["pname"]);




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



});