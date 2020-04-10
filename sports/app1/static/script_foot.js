const showDiv = () => {
    document.getElementById("disp").style.display = "block";
    document.getElementById("joinTeam").style.display = "none";
};

const showTeam = () => {
    document.getElementById("show-team").style.display = "block";

    document.getElementById("heading").innerHTML="team  ";
    const radio = document.getElementsByName("guy1");
    for(i=0;i<radio.length;i++){
        if(radio[i].checked){
            let val = radio[i].value;
            let text1 = document.getElementById("heading");
            let text2 = document.createTextNode(val);
            text1.appendChild(text2);
        }
    }

    // let ele = document.getElementById("popup");
    // ele.appendChild(text1);
};

var sel=[];
 $('#create').click(function() {
    sel = $('input[type=checkbox]:checked').map(function(_, el) {
        return $(el).val();
    }).get();

})

const showDiv2 = () => {
    document.getElementById("disp1").style.display = "none";
    document.getElementById("disp2").style.display = "block";
    var text = "";
    var i;
    for (i = 0; i < sel.length; i++) {
         text += sel[i] + "<br>";
    }
    document.getElementById("selected-players").innerHTML = text;
};

const closeTeam = () => {
    document.getElementById("disp1").style.display="none";
    document.getElementById("heading").innerHTML='';
};

const showDiv1 = () => {
    document.getElementById("disp1").style.display = "block";
}

var captain,date,time;
        $('a').click(function() {
            captain = $(this).attr('data-id');
            date = $(this).data('id1');
            time = $(this).data('id2');
        });

            $('#myModal').modal().on('show.bs.modal', function (e) {
            $(this).find('#captain').text(captain);
            $(this).find('#date').text(date);
            $(this).find('#time').text(time);
            });
