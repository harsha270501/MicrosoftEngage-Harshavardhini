fixedcells=[]
var startgridno=0
var endgridno=0
blockobj={}
blocklist={}
for(var i=0;i<36;i++)
{
  for(var j=0;j<64;j++)
  {
    blocklist[[parseInt(i),parseInt(j)]]=false;
  }
}
var w = 1984, h = 1116;
var r;
var r1;
var sx,sy,ex,ey;
var pathpr;
pathpr=[]
window.onload = function () {
   
    r = Raphael("grid", w, h);
    
    --w;
    --h;
    r.rect(0, 0, w, h, 10).attr({stroke: "#666"});
    
    // grid
    var d = 31, i;
    for (i = d; i < h; i += d) {
      r.path([[ "M", 0, i], ["L", w, i]]).attr({stroke: "#666"});
    }
    
    for (i = 31; i < w; i += 31) {
      r.path([["M", i, 0], ["L", i, w]]).attr({stroke: "#666"});
    }
 

  
  
    var dragger = function () {
      this.ox = this.type == "rect" ? this.attr("x") : this.attr("cx");
      this.oy = this.type == "rect" ? this.attr("y") : this.attr("cy");
      this.animate({"fill-opacity": .5}, 500);
    },
    move = function (dx, dy) {
      var x1=(Math.floor((Math.floor(this.ox + dx))/31))*31;
      var y1=(Math.floor((Math.floor(this.oy + dy))/31))*31;
      
      var att = this.type == "rect"
        ? {x: x1, y:y1 }
        : {cx: x1, cy:y1};
      
      this.attr(att);
    
    },
    up = function () {
      this.animate({"fill-opacity": 1}, 500);
      this.click(function(){
        event.preventDefault();
      });
    }
  
    fixedcells = [
      r.rect(31,31,31,31).data("jid", "start"),
      r.rect(186,248,31,31).data("jid", "end")
    ];
  
    var n = fixedcells.length;
  
    
      fixedcells[0].attr({stroke: "green", fill:"green"})
        .drag(move, dragger, up);
      
      fixedcells[1].attr({stroke: "red", fill:"red"})
        .drag(move, dragger, up);

        
        
  };

  function drawblock(e){
    x3=e.clientX;
    y3=e.clientY;
    x3=(Math.floor((Math.floor(x3))/31))*31;
    y3=(Math.floor((Math.floor(y3))/31))*31;
    sx=fixedcells[0].attr("x");
    sy=fixedcells[0].attr("y");
    ex=fixedcells[1].attr("x");
    ey=fixedcells[1].attr("y");
    if((x3==sx)&&(y3==sy))
    return;
    if((x3==ex)&&(y3==ey))
    return;

    j=Math.floor(x3/31);
    i=Math.floor(y3/31);
    
    if(blocklist[[i,j]]==false)
    {  
      b=r.rect(x3,y3,31,31).data("jid","block"+i+j)
      b.attr({stroke:"gray",fill:"gray"});
      blocklist[[i,j]]=true;
      blockobj[[i,j]]=b;
    }
    else
    {  
      blocklist[[i,j]]=false;
      b=blockobj[[i,j]]
      b.attr({stroke:"#666",fill:"white"});
    }
  }
function search(){
  var searchtype;
  
  opt=[]
  var opt1=0;
  if(document.getElementById('allowdiagonals').checked)
  {
    if(document.getElementById('nocorner').checked)
    opt1=1;
    else
    opt1=2;
  }

  var opt2=0;
  opt.push(opt1);
  if(document.getElementById('euclidean').checked)
    opt2=0;
  else if(document.getElementById('manhattan').checked)
    opt2=1;
  opt.push(opt2);

  if(document.getElementById('bfs').checked)
    searchtype="bfs";
  else if(document.getElementById('dijkstra').checked)
    searchtype="dijkstra";
  else if(document.getElementById('bestfirstsearch').checked)
    searchtype="bestfirstsearch";
  else if(document.getElementById('Asearch').checked)
    searchtype="Asearch";
  else if(document.getElementById('IDAsearch').checked)
    searchtype="IDAsearch";

  for(var i=0;i<pathpr.length;i++)
    {
      pathpr[i].remove();
    }

  j=Math.floor(fixedcells[0].attr("x")/31);
  i=Math.floor(fixedcells[0].attr("y")/31);
  
  startgridno=i*64+j;
  console.log(startgridno);

  j=Math.floor(fixedcells[1].attr("x")/31);
  i=Math.floor(fixedcells[1].attr("y")/31);
  
  endgridno=i*64+j;
  console.log(endgridno);
  blockednodes=[]
  var key;
  for(key in blocklist){
    if(blocklist[key]==true)
    {
      i=parseInt(key[0]);
      j=parseInt(key[2]);
      console.log(i,j);
      b=i*64+j;
      console.log(b);
      blockednodes.push(b);
    }
  }
  console.log(blockednodes);
  const csrf_token=getCookie('csrftoken');
    searchparam={
        'start': startgridno,
        'end':endgridno,
        'blocked':blockednodes,
        'options':opt,
        'searchtype':searchtype,
        csrfmiddlewaretoken: csrf_token
    };
    $.post('searchpath',searchparam,function(data,status){
        console.log(searchtype);
        console.log(data['Result']['path']);
        console.log(data['Result']['dist']);
        drawpath(data);
    });

  }

  function drawpath(data)
  {
    p=data['Result']['path'];
    for(var i=0;i<p.length-1;i++)
    {
      i1=((Math.floor(p[i]/64))*31)+15.5;
      j1=((Math.floor(p[i]%64))*31)+15.5;
      i2=((Math.floor(p[i+1]/64))*31)+15.5;
      j2=((Math.floor(p[i+1]%64))*31)+15.5;
      
      pob=r.path([[ "M", j1, i1], ["L", j2, i2]]).data("jid", "path"+i);
      pathpr.push(pob);
      pob.attr({"stroke": "yellow","stroke-width": 3});
    }
    d=data['Result']['dist'];
  
    dist="Distance: "+d.toFixed(2);
    document.getElementById('resultd').innerHTML=dist;
  }

  function dispheuristic(){
    a1=document.getElementById('bestfirstsearch').checked;
    a2=document.getElementById('Asearch').checked;
    a3=document.getElementById('IDAsearch').checked;
    console.log(a1||a2||a3);

    if(a1||a2||a3)
    document.getElementById("heuristic").style.display="block";
    else
    document.getElementById("heuristic").style.display="none";
  }