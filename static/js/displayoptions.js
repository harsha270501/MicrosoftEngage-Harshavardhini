// change the options to be displayed
function dispcontrol(){
    a1=document.getElementById('bestfirstsearch').checked;
    a2=document.getElementById('Asearch').checked;
    a3=document.getElementById('IDAsearch').checked;
    console.log(a1||a2||a3);

    if(a1||a2||a3)
    {
        document.getElementById("heuristic").style.display="block";
        document.getElementById("adddestpt").style.display="none";
        document.getElementById("adddestptbutton").style.display="none";
    }
    else
    {
        document.getElementById("heuristic").style.display="none";
        document.getElementById("adddestpt").style.display="block";
        document.getElementById("adddestptbutton").style.display="block";
  }
}



