
// Onclick of the button


function main() {  
  
  var img = new Image(25, 25);//document.createElement("img");
  img.src = "https://media.tenor.com/On7kvXhzml4AAAAj/loading-gif.gif";
  var src = document.getElementById("picture");
  //document.querySelector(".picture") = img;
  const est = document.createElement("p")
  const node = document.createTextNode('Estimated Time 40 secs')
  src.appendChild(img);
  src.appendChild(node);
  document.querySelector(".intro").innerHTML = '';
  document.querySelector(".info").innerHTML = '';
  document.querySelector(".info1").innerHTML = '';
  document.querySelector(".info2").innerHTML = '';
  document.querySelector(".info3").innerHTML = '';
  document.querySelector(".info4").innerHTML = '';
  document.querySelector(".info5").innerHTML = '';
  document.querySelector(".info6").innerHTML = '';
  document.querySelector(".info7").innerHTML = '';
  //src.appendChild(img);
  if (document.getElementById("lon") == '[object HTMLParagraphElement]'){
    var z = document.getElementById("lat").textContent
    var y = document.getElementById("lon").textContent
    } else {
      var z = document.getElementById("lat").value
      var y = document.getElementById("lon").value
    }
  var t1 = document.getElementById("measurmentSystem").value  
  var t2 = document.getElementById("excludeFreq").value

  eel.random_python(t2, t1, z, y)(function(number){                      
    // Update the div with a random number returned by python
    // picture
    src.removeChild(img)
    src.removeChild(node)
    src.removeChild(img)
    src.removeChild(node)
    document.querySelector(".intro").innerHTML = number[0];
    document.querySelector(".info").innerHTML = number[1];
    document.querySelector(".info1").innerHTML = number[2];
    document.querySelector(".info2").innerHTML = number[3];;
    document.querySelector(".info3").innerHTML = number[4];
    document.querySelector(".info4").innerHTML = number[5];
    document.querySelector(".info5").innerHTML = number[6];
    document.querySelector(".info6").innerHTML = number[7];
    document.querySelector(".info7").innerHTML = number[8];
    })
}



var x = document.getElementById("demo")
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(showPosition)
  } else {
    x.innerHTML = "Geolocation is not supported by this browser."
  }
}
function showPosition(position) {
  const autoCoord = document.createElement("div")
  autoCoord.setAttribute("id", "typeOfCoord")
  const lat = document.createElement("p")
  lat.setAttribute("id", "lat")
  const node = document.createTextNode(position.coords.latitude)
  const lon = document.createElement("p")
  lon.setAttribute("id", "lon")
  const node2 = document.createTextNode(position.coords.longitude)
  autoCoord.appendChild(lat)
  autoCoord.appendChild(lon)
  lat.appendChild(node)
  lon.appendChild(node2)
  x.innerHTML = "AutoCoords"
  const parent = document.getElementById("div1")
  const child = document.getElementById("typeOfCoord")
  parent.replaceChild(autoCoord, child)
  //uhuuhuhuh.setAttribute("id", "uhuuhuhuh")
}

// type="text" id="stateInput" value="Some text..."


function accessDenied() {
  const manual_input_coords = document.createElement("div")
  manual_input_coords.setAttribute("id", "typeOfCoord")
  const lat_input = document.createElement("input")
  lat_input.setAttribute("type", "text")
  lat_input.setAttribute("id", "lat")
  lat_input.setAttribute("value", "Type your Latitude...")
  const lon_input = document.createElement("input")
  lon_input.setAttribute("type", "text")
  lon_input.setAttribute("id", "lon")
  lon_input.setAttribute("value", "Type your Longitude...")
  manual_input_coords.appendChild(lat_input)
  manual_input_coords.appendChild(lon_input)
  x.innerHTML = "Go ahead, type your coords"
  const parent = document.getElementById("div1")
  const child = document.getElementById("typeOfCoord")
  parent.replaceChild(manual_input_coords, child)

}

function myFunction() {
  if (document.getElementById("lon") == '[object HTMLParagraphElement]'){
  var z = document.getElementById("lat").textContent
  var y = document.getElementById("lon").textContent
  } else {
    var z = document.getElementById("lat").value
    var y = document.getElementById("lon").value
  }
  //var y = document.getElementById("lon").toString().value
  document.getElementById("latOut").innerHTML = z
  document.getElementById("lonOut").innerHTML = y
  
  var t1 = document.getElementById("measurmentSystem").value
  document.getElementById("test1").innerHTML = t1
  
  var t2 = document.getElementById("excludeFreq").value
  document.getElementById("test2").innerHTML = t2
  
  var t3 = document.getElementById("measurmentSystem").value
  document.getElementById("test3").innerHTML = t3


}

function myFunctions(){
  var z = document.getElementById("lat")
  document.getElementById("latOut").innerHTML = z
}

