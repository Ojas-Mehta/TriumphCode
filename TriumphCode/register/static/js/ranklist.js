$(function(){


     //alert("ranking");
     var pro=JSON.parse(document.getElementById("ranklist").innerHTML);
     console.log(pro);
     document.getElementById("cname").innerHTML=pro[0]["competitionid_id__cname"];


var table = document.createElement("table");
table.setAttribute("id", "display_table");
document.getElementById("problems_container").appendChild(table);

var trh = document.createElement("tr");
trh.setAttribute("id", "table_head");
table.appendChild(trh);

var Rank = document.createElement("th");
var node = document.createTextNode("Rank");
Rank.appendChild(node);
trh.appendChild(Rank);
/*
var c_name = document.createElement("th");
node = document.createTextNode("Competition");
c_name.appendChild(node);
trh.appendChild(c_name);
*/
var u_name = document.createElement("th");
node = document.createTextNode("User");
u_name.appendChild(node);
trh.appendChild(u_name);

var score = document.createElement("th");
node = document.createTextNode("Score");
score.appendChild(node);
trh.appendChild(score);


for(var i = 0, size = pro.length; i < size ; i++){

	var tr = document.createElement("tr");
	tr.setAttribute("id", "tr" + (i+1) );
    table.appendChild(tr);


	var td1 = document.createElement("td");
	td1.setAttribute("id", "td" + (i+1) + "1");
    tr.appendChild(td1);
/*
	var td2 = document.createElement("td");
	td2.setAttribute("id", "td" + (i+1) + "2");
    tr.appendChild(td2);
*/
	var td3 = document.createElement("td");
	td3.setAttribute("id", "td" + (i+1) + "2");
    tr.appendChild(td3);

    var td4 = document.createElement("td");
	td4.setAttribute("id", "td" + (i+1) + "3");
    tr.appendChild(td4);



}







for(var i = 0, size = pro.length; i < size ; i++){
   var item = pro[i];
//   console.log(item["pid_id__pid"] + " " + item["pid_id__pname"]);

   var problem_index0 = document.createElement("label");
   var node = document.createTextNode((i+1));
   problem_index0.appendChild(node);

   element = document.getElementById("td" + (i+1) + "1");
   element.appendChild(problem_index0);

/*
   var problem_index = document.createElement("a");
   node = document.createTextNode(pro[i]["competitionid_id__cname"] + "          ");
   problem_index.setAttribute("href", "viewproblem/?pid=" + pro[i]["competitionid_id__cname"]);
   problem_index.setAttribute("id", pro[i]["competitionid_id__cname"]);
   problem_index.setAttribute("value", pro[i]["competitionid_id__cname"]);
   problem_index.appendChild(node);

   element = document.getElementById("td" + (i+1) + "2");
   element.appendChild(problem_index);
*/
   var problem_index2 = document.createElement("label");
   var node = document.createTextNode(pro[i]["userid_id__username"] + "          ");
   problem_index2.appendChild(node);

   element = document.getElementById("td" + (i+1) + "2");
   element.appendChild(problem_index2);

   var problem_index3 = document.createElement("label");
   var node = document.createTextNode(pro[i]["score"] + "          ");
   problem_index3.appendChild(node);

   element = document.getElementById("td" + (i+1) + "3");
   element.appendChild(problem_index3);



}











});