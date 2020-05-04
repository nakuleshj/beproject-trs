$(document).ready(function(){
    $("#sub").click(function(){
        $("#sub").hide();
        var s=$('#s').val();
        var g=$('#g').val();
        var i=$('#i').val();
        var p=$('#p').val();

         $.ajax({
             type: "GET",
                    url: 'get_rec/',
                    data: {
                            'season': s,
                            'going_with':g,
                            'interest':i,
                            'pref':p
                    },
            dataType: 'json',
            success: function (data) {

                $('#p1').text(data.n1);
                $('#p2').text(data.n2);
                $('#p3').text(data.n3);
                $('#p4').text(data.n4);
                $('#p5').text(data.n5);
                $('#i1').attr("src",data.i1);
                $('#i2').attr("src",data.i2);
                $('#i3').attr("src",data.i3);
                $('#i4').attr("src",data.i4);
                $('#i5').attr("src",data.i5);
                $('#places').show();
                    }
                });

        });
    $("#n").click(function(){
        var s=$('#s').val();
        var g=$('#g').val();
        var i=$('#i').val();
        var p=$('#p').val();

         $.ajax({
             type: "GET",
                    url: 'get_rec/',
                    data: {
                            'season': s,
                            'going_with':g,
                            'interest':i,
                            'pref':p
                    },
            dataType: 'json',
            success: function (data) {

                $('#p1').text(data.n1);
                $('#p2').text(data.n2);
                $('#p3').text(data.n3);
                $('#p4').text(data.n4);
                $('#p5').text(data.n5);
                $('#i1').attr("src",data.i1);
                $('#i2').attr("src",data.i2);
                $('#i3').attr("src",data.i3);
                $('#i4').attr("src",data.i4);
                $('#i5').attr("src",data.i5);
                $('#places').show();
                    }
                });

        });
        $(".plcs").click(function(){
            var plc=$(this).children("span").text()
            var i=$('#i').val();
            var p=$('#p').val();
            $.ajax({
             type: "GET",
                    url: 'itnr/',
                    data: {
                            'place': plc,
                            'interest':i,
                            'pref':p
                    },
            dataType: 'json',
            success: function (data) {
            alert("Connected to itnr gen");
                    }
                });
        });
});