$(function(){

     var p_status=JSON.parse(document.getElementById("p_status").innerHTML);
     var c_status=JSON.parse(document.getElementById("c_status").innerHTML)
     console.log(p_status);
     console.log(c_status);


var table = document.createElement("table");
table.setAttribute("id", "display_table");
document.getElementById("data1").appendChild(table);

var trh = document.createElement("tr");
trh.setAttribute("id", "table_head");
table.appendChild(trh);

var no = document.createElement("th");
var node = document.createTextNode("Problems Solved");
no.appendChild(node);
trh.appendChild(no);

for(var i = 0, size = p_status.length; i < size ; i++){

	var tr = document.createElement("tr");
	tr.setAttribute("id", "tr" + (i+1) );
    table.appendChild(tr);


	var td1 = document.createElement("td");
	td1.setAttribute("id", "td" + (i+1) + "1");
    tr.appendChild(td1);

}

for(var i = 0, size = p_status.length; i < size ; i++){


   var problem_index0 = document.createElement("label");
   node = document.createTextNode(p_status[i]["pid_id__pname"]);
   problem_index0.appendChild(node);

   element = document.getElementById("td" + (i+1) + "1");
   element.appendChild(problem_index0);





}







var table = document.createElement("table");
table.setAttribute("id", "display_table");
document.getElementById("data2").appendChild(table);

var trh = document.createElement("tr");
trh.setAttribute("id", "table_head");
table.appendChild(trh);

var no = document.createElement("th");
var node = document.createTextNode("Competition Participated");
no.appendChild(node);
trh.appendChild(no);

var problem_name = document.createElement("th");
node = document.createTextNode("Problem Solved");
problem_name.appendChild(node);
trh.appendChild(problem_name);


for(var i = 0, size = c_status.length; i < size ; i++){

	var tr = document.createElement("tr");
	tr.setAttribute("id", "tr" + (i+1) );
    table.appendChild(tr);


	var td1 = document.createElement("td");
	td1.setAttribute("id", "tda" + (i+1) + "1");
    tr.appendChild(td1);

	var td2 = document.createElement("td");
	td2.setAttribute("id", "td" + (i+1) + "2");
    tr.appendChild(td2);

}

for(var i = 0, size = c_status.length; i < size ; i++){


   var problem_index2 = document.createElement("label");
   node = document.createTextNode(c_status[i]["cid_id__cname"]);
   problem_index2.appendChild(node);

   element = document.getElementById("tda" + (i+1) + "1");
   element.appendChild(problem_index2);

   var problem_index1 = document.createElement("label");
   node = document.createTextNode(c_status[i]["pid_id__pname"]);
   problem_index1.appendChild(node);

   element = document.getElementById("td" + (i+1) + "2");
   element.appendChild(problem_index1);




}





});