
$(function(){

    var editor;
    function myFunction() {
        editor = ace.edit("editor");
        editor.setTheme("ace/theme/twilight");
        editor.session.setMode("ace/mode/javascript");
        editor.setOptions({
                 autoScrollEditorIntoView: true,
              });

    editor.renderer.setScrollMargin(10, 10, 10, 10);
    editor.session.setMode("ace/mode/c_cpp");
    editor.setAutoScrollEditorIntoView(true);
    editor.setOption("maxLines", 20);
    editor.setOption("minLines", 20);
    editor.resize();
}

myFunction();

$("#getdata").click(function(){


        $("#loader").attr("style","display:block");

        var code=editor.getValue();
        console.log("kutte1");


        $.ajax(
        {
             type: "POST",
             url: "/dashboard/CompileAndRun/submit",
             data:{
                 "code" : code,
                 "input1": $("#inputdata").val(),
                 "lang": $("#lang").val(),
                 "csrfmiddlewaretoken" : $('input[name="csrfmiddlewaretoken"]').val(),
             },
             success: function( data )
            {

              //   alert("animesh ullu1");
                 code_data(data);

            }
        })



    });

function code_data(data)
            {

            $("#loader").attr("style","display:none");

            //     alert("animesh ullu2");
                 console.log(data);


                console.log(data["cpuTime"]);



var x = data["output"];
var res = x.split("JDoodle").join("TriumphCode");
res = res.split("jdoodle").join("triumphcode");








                 //console.log(data.code_id);

                 //$("#inputdata").val(data.run_status.output);
                 //val(data.run_status.output_html);
                       $("#memory_used").text("Memory :  " + data["memory"]);
                       $("#time_used").text("CPU Time :  " +data["cpuTime"]);
                       $("#code_output").text("Output:  " +res);



            }



$("#submit").click(function(){
        var code=editor.getValue();
        console.log("kutte1");
        var pro = JSON.parse(document.getElementById("problem_data").innerHTML)
        $("#loader").attr("style","display:block");


        $.ajax(
        {
             type: "POST",
             url: "/dashboard/problems/viewproblems/submit",
             data:{
                 "pid" :pro["pid"],
                 "code" : code,
                 "lang": $("#lang").val(),
                 "csrfmiddlewaretoken" : $('input[name="csrfmiddlewaretoken"]').val(),
             },
             success: function( data )
            {
                        $("#loader").attr("style","display:none");

                 console.log(data);
                 console.log(data["compile_error"]);
                 if(data["compile_error"]=="YES"){

                        $("#status").text("Solved Sucessfully!!!");
                 }
                 else{
                        $("#status").text("Wrong answer");
                 }
            }
        })



    });







});



