$(document).ready(function () {

  var tmp = [];
  
  //batsman
 $('input:radio[name="batsman"]').change(function(){
    var checked = $("input[name='batsman']:checked").val();
    if(tmp.length == 10){
      tmp.splice(0,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }

});
//runMate
 $('input:radio[name="runMate"]').change(function(){
    var checked = $("input[name='runMate']:checked").val();
    if(tmp.length == 10){
      tmp.splice(1,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }
});
//bowler
 $('input:radio[name="bowler"]').change(function(){
    var checked = $("input[name='bowler']:checked").val();
    if(tmp.length == 10){
      tmp.splice(2,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }
});
//fielder
 $('input:radio[name="fielder"]').change(function(){
    var checked = $("input[name='fielder']:checked").val();
    if(tmp.length == 10){
      tmp.splice(3,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }
});
//run
 $('input:radio[name="run"]').change(function(){
    var checked = $("input[name='run']:checked").val();
    if(tmp.length == 10){
      tmp.splice(4,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }
});
//Out
 $('input:radio[name="out"]').change(function(){
    var checked = $("input[name='out']:checked").val();
    if(tmp.length == 10){
      tmp.splice(5,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }
});
//Out Batsman Name
 $('input:radio[value="run_Out"]').change(function(){
            $('.menu').slideToggle("slide");
});


//BowlerType
 $('input:radio[name="bowlerType"]').change(function(){
    var checked = $("input[name='bowlerType']:checked").val();
    if(tmp.length == 10){
      tmp.splice(6,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }
});
//extraRun Types
 $('input:radio[name="extraRunType"]').change(function(){
    var checked = $("input[name='extraRunType']:checked").val();
    if(tmp.length == 10){
      tmp.splice(7,1,checked);
    }else{
      if($(this).is(":checked")){
          //alert(checked);
          tmp.push(checked);
      }
    }
});


//Extra Run
    $('.minus').click(function () {
				var $input = $(this).parent().find('input');
				var count = parseInt($input.val()) - 1;
				count = count < 1 ? 1 : count;
				$input.val(count);
				$input.change();
				return false;
			});
			$('.plus').click(function () {
				var $input = $(this).parent().find('input');
				$input.val(parseInt($input.val()) + 1);
				$input.change();
				return false;
			});
		
    
 







//##### Submit Button #####
   
  $('#button').on('click', function () {
		
    //Add Extra Run
    var extraRun = $('#extraRun').val();
    var  extraRun= parseFloat(extraRun);
    if(tmp.length == 10){
      tmp.splice(8,1,extraRun);
    }else{
          tmp.push(extraRun);
    
    }

    //Over count
    var over = $('#over').val();
    var  over= parseFloat(over)               
    over += 0.1 ;
    
    if (over % 10 == 0.6){
      over += 0.5;
    }
    over = over.toFixed(1);
    $('#over').val(over);
    over -= 0.1;
    over = over.toFixed(1);
    
    //add ball no. to tmp 
    if(tmp.length == 10){
      tmp.splice(9,1,over);
    }else{  
          tmp.push(over);
    }

    
    


    //***********************************
    //ajax
    $.ajax({           
            type: 'POST',
            url: "{% url 'match_view' %}",
            data: {'tmp': tmp,'matchId': 1},
            dataType: 'json',
            success: function (response) {
                  console.log(response);
                  if (response.status == 200){
                    var text = tmp.join('>'); 
                    document.getElementById("demo").innerHTML = text;
                  }else{
                    document.getElementById("demo").innerHTML = tmp;
                  }
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response.error);
            }
          });

    //text= tmp.toString()
    
  });
  
});
