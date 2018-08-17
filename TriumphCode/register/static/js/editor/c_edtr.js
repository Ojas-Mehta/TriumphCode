
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

        alert("hooioi");
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
                 //console.log(data.code_id);

                 //$("#inputdata").val(data.run_status.output);
                 //val(data.run_status.output_html);
                 var x;
                 if(data.compile_status == "OK" && data .run_status.status == "AC"){
                       x = "Code is sucessfully Compiled and executed."
                       $("#compile_and_run_status").text(x);
                       $("#memory_used").text("Memory Used:  " + data.run_status.memory_used);
                       $("#time_used").text("Time Used:  " +data.run_status.time_used);
                       $("#code_output").text("Output:  " +data.run_status.output);

                 }
                 else if(data.compile_status != "OK"){
                       x = "Code is not sucessfully compiled."
                       $("#compile_and_run_status").text(x);
                       $("#error_msg").text(data.compile_status);
                 }
                 else if(data.run_status.status != "AC"){
                       x = "Code is not executed."
                       $("#compile_and_run_status").text(x);
                       $("#error_msg").text(data.run_status.status);
                 }


            }



$("#submit").click(function(){
        var code=editor.getValue();
        console.log("c_kutte1");
        $("#loader").attr("style","display:block");

        var pro = JSON.parse(document.getElementById("contest").innerHTML)
        var cdata=JSON.parse(document.getElementById("cdata").innerHTML)
        //console.log(pro);

        $.ajax(
        {
             type: "POST",
             url: "/dashboard/Contest/problems/viewproblem/submit",
             data:{
                 "pid" :pro["pid"],
                 "cid":cdata[0]["cid"],
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



