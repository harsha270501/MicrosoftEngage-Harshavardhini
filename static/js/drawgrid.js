fixedcells=[]
var startgridno=0
var endgridno=0
blockobj={}
blocklist={}
endobj={}
endlist={}
txt=[]
b=[];
b.push(-1);
b.push(-1);
for(var i=0;i<36;i++)
{
  for(var j=0;j<64;j++)
  {
    b[0]=i;
    b[1]=j;
    blocklist[b]=false;
    endlist[b]=false;
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
      r.rect(186,279,31,31).data("jid", "start"),
      r.rect(465,403,31,31).data("jid", "end")
    ];
  
    var n = fixedcells.length;
  
    
      fixedcells[0].attr({stroke: "green", fill:"green",cursor:"move"})
        .drag(move, dragger, up).click(function(){
          event.preventDefault();
        });
      
      fixedcells[1].attr({stroke: "red", fill:"red",cursor:"move"})
        .drag(move, dragger, up).click(function(){
          event.preventDefault();
        });

        dispcontrol();
        
  };

  function drawblock(e){
    var clr="gray";
    if(document.getElementById("AddDestinationPoints").checked)
      clr="#c80815";
    else if(document.getElementById("Changestart").checked)
      clr="green";
    else if(document.getElementById("Changeend").checked)
      clr="red";
    
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

    j=parseInt(Math.floor(x3/31));
    i=parseInt(Math.floor(y3/31));
    if(clr=="gray")
    {
      if(blocklist[[i,j]]==false)
      {  
        b=r.rect(x3,y3,31,31).data("jid","block"+i+j)
        b.attr({stroke:clr,fill:clr});
        blocklist[[i,j]]=true;
        blockobj[[i,j]]=b;
      }
      else
      {  
        blocklist[[i,j]]=false;
        b=blockobj[[i,j]]
        b.remove();
      }
    }
    else if(clr=="green")
    {
      fixedcells[0].attr({"x":x3,"y":y3}).click(function(){
        event.preventDefault();
      });
    }
    else if(clr=="red")
    {
      fixedcells[1].attr({"x":x3,"y":y3}).click(function(){
        event.preventDefault();
      });
    }
    else 
    {
      if(endlist[[i,j]]==false)
      {  
        b=r.rect(x3,y3,31,31).data("jid","end"+i+j)
        b.attr({stroke:clr,fill:clr});
        endlist[[i,j]]=true;
        endobj[[i,j]]=b;
      }
      else
      {  
        endlist[[i,j]]=false;
        b=endobj[[i,j]]
        b.remove();
      }
    }
  }

function clearwalls(){
  for(var keys in blockobj){
  blocklist[keys]=false;
  b=blockobj[keys];
  b.remove();}

}

function clearpath(){
  for(var i=0;i<pathpr.length;i++)
    {
      pathpr[i].remove();
    }
    pathpr.length=0;

  for(var i=0;i<txt.length;i++)
  {
    txt[i].remove();
  }
  txt.length=0;
}

function cleardest(){
  for(var keys in endobj)
  {
    endlist[keys]=false;
    e=endobj[keys];
    e.remove();
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

  clearpath();

  j=Math.floor(fixedcells[0].attr("x")/31);
  i=Math.floor(fixedcells[0].attr("y")/31);
  
  startgridno=i*64+j;


  j=Math.floor(fixedcells[1].attr("x")/31);
  i=Math.floor(fixedcells[1].attr("y")/31);
  
  endgridno=i*64+j;
  var key;
  endnodes=[]
  endnodes.push(endgridno)

  for(key in endlist){
    if(endlist[key]==true)
    {
      k=key.split(',');
      i=parseInt(k[0]);
      j=parseInt(k[1]);
      console.log(i,j);
      b=i*64+j;
      console.log(b);
      endnodes.push(b);
    }
  }

  blockednodes=[]
 
  for(key in blocklist){
    if(blocklist[key]==true)
    {
      k=key.split(',');
      i=parseInt(k[0]);
      j=parseInt(k[1]);
      b=i*64+j;
      blockednodes.push(b);
    }
  }
  if((searchtype=="bestfirstsearch")||(searchtype=="Asearch")||(searchtype=="IDAsearch"))
  {  endnodes=endnodes[0];}
  
  
  const csrf_token=getCookie('csrftoken');
    searchparam={
        'start': startgridno,
        'end':endnodes,
        'blocked':blockednodes,
        'options':opt,
        'searchtype':searchtype,
        
    };
    console.log(searchparam);
    $.get('searchpath',searchparam,function(data,status){
        console.log(data,searchtype);
        drawpath(data,searchtype);
    });

  }

function drawpath(data,s)
  {
    if((s=="bfs")||(s=="dijkstra")){
      path=data['Result'];
      var i2,j2,dist;
      dist=0;
      var l=Object.keys(path).length;
      for(var pt in path)
      {
        p=path[pt][0];
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
        
        d=path[pt][1];
        console.log(path);
        if(l>1){
          console.log(1);
        t=r.text(j2,i2+31,d.toFixed(2)).attr({"font-size": 15});
        txt.push(t);
      }
        dist+=d;
      }
      document.getElementById('resultd').innerHTML="Distance: "+dist.toFixed(2);
    }
    else{
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
        console.log('Informed');
        d=data['Result']['dist'];
        dist="Distance: "+d.toFixed(2);
        document.getElementById('resultd').innerHTML=dist;
    }
}


  
