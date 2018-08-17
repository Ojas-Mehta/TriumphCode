
$(function(){


             var pro = JSON.parse(document.getElementById("kutta").innerHTML)
             console.log(pro);
            //$("#abc").text("title:  " + x[0]);
            console.log(pro[0]["pname"]);
//var txt = "";
var x;
for (x in pro) {
    console.log(pro[x]["pid"]);
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
node = document.createTextNode("Category");
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
   console.log(item["pid"] + " " + item["pname"]);

   var problem_index0 = document.createElement("label");
   node = document.createTextNode((i+1));
   problem_index0.appendChild(node);

   element = document.getElementById("td" + (i+1) + "1");
   element.appendChild(problem_index0);



   var problem_index = document.createElement("a");
   node = document.createTextNode(pro[i]["pname"] + "          ");
   problem_index.setAttribute("href", "viewproblems/?pid=" + pro[i]["pid"]);
   problem_index.setAttribute("id", pro[i]["pid"]);
   problem_index.setAttribute("value", pro[i]["pname"]);
   problem_index.appendChild(node);

   element = document.getElementById("td" + (i+1) + "2");
   element.appendChild(problem_index);


   var problem_index2 = document.createElement("label");
   var node = document.createTextNode(pro[i]["ptag"] + "          ");
   problem_index2.appendChild(node);

   element = document.getElementById("td" + (i+1) + "3");
   element.appendChild(problem_index2);




}




//document.getElementById("demo").innerHTML = txt;



});



