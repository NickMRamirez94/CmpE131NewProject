from flask import Blueprint
from my_app.source.models import cursor

my_view = Blueprint('my_view', __name__)


#-------------------- getBooks --------------------
def getBooks(data_results):
    ID = 0
    NAME = 1
    AUTHOR = 2
    PUBLISHER = 3
    CATEGORY = 4
    RELEASED = 5

    header = """
        <html>
        <head>
        <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        </style>
        </head>
        <body>

        <table>
            <table style="width:100%">
              <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Author</th>
                <th>Category</th>
                <th>Publisher</th>
                <th>Released</th>
              </tr>
                """

    footer = """
    </table></body>
        """
    message_out = ""

    for item in data_results:
        key = item[ID]
        message_out += '<tr>'+\
                       '<td>'+str(item[ID])+'</td>'+\
                       '<td><a style="text-decoration:none; color:#0000ff;" href="http://127.0.0.1:5000/books/'+str(key)+'">'+item[NAME]+'</td>'+\
                       '<td>'+item[AUTHOR]+'</td>'+\
                       '<td align="right">'+item[PUBLISHER]+'</td>'+\
                       '<td align="right">'+item[CATEGORY]+'</td>'+\
                       '<td align="right">'+item[RELEASED]+'</td>'+\
                       '</tr>'

    return header+message_out+footer

#-------------------- getStudios --------------------
def getPublisher(data_results):
    NAME = 1
    LOCATION = 2
    TITLES = 3
    RATING = 4

    header = """
            <html>
        <head>
        <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        </style>
        </head>
        <body>
        <table>
            <table style="width:100%">
              <tr>
                <th>ID</th>
                <th>Publisher Name</th>
                <th>Headquarters</th>
                <th>Total Books Released</th>
                <th>Average Book Rating</th>
              </tr>
                """

    footer = """
    </table></body>
        """
    message_out = ""


    key = 1
    for item in data_results:
        message_out += '<tr>'+\
                       '<td>'+str(key)+'</td>'+\
                       '<td><a style="text-decoration:none; color:#0000ff;" href="http://127.0.0.1:5000/publishers/'+str(key)+'">'+item[NAME]+'</td>'+\
                       '<td align="right">'+item[LOCATION]+'</td>'+\
                       '<td align="right">'+item[TITLES]+'</td>'+\
                       '<td align="right">'+item[RATING]+'</td>'+\
                       '</tr>'
        key += 1
    return header+message_out+footer

#-------Home Page---------
@my_view.route('/')
@my_view.route('/home')
def greeting():
    return '''

<html>
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>
</html>

<head>
<title> Home </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<style>
img {
    display: block;
    margin: 0 auto;
}
</style>

<img src=https://blog.spoongraphics.co.uk/wp-content/uploads/2014/illustration/1.jpg align="center" alt="Mountain View" style="width:500px;height:350px;">
<p align="center" style="font-family:'Arial'"> The Arena is built for gamers, by gamers </p>
<p align="center" style="font-family:'Arial'"> Here you can search for games on current or older systems </p>
<p align="center" style="font-family:'Arial'"> We also have information on consoles and other resources </p>
<hr>

<style>
.container {
  border: 2px solid #ccc;
  background-color: #eee;
  border-radius: 5px;
  padding: 16px;
  margin: 16px;
}

.container::after {
  content: "";
  clear: both;
  display: table;
}

.container img {
  float: left;
  margin-right: 20px;
  border-radius: 50%;
}

.container span {
  font-size: 20px;
  margin-right: 15px;
}

@media (max-width: 250px) {
  .container {
      text-align: center;
  }
  .container img {
      margin: auto;
      float: none;
      display: block;
  }
}
</style>
</head>
<body>

<h2 align="center">Testimonials</h2>

<div class="container">
  <img src="https://yt3.ggpht.com/-SLRdt5LKJic/AAAAAAAAAAI/AAAAAAAAAAA/mIeY5m_1ZdM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg" alt="Burnie" style="width:90px">
  <p><span>Burnie Burns</span> Rooster Teeth Productions</p>
  <p>I check The Arena all the time because they catalog the best of the best</p>
</div>

<div class="container">
  <img src="http://24.media.tumblr.com/c0ac782cf823042caea308b166c5e419/tumblr_n49qz73Z7F1rlqiixo7_500.jpg" alt="Gavin" style="width:90px">
  <p><span >Gavin Free</span> The Slow Mo Guys</p>
  <p>Whenever I want a game to play, I always come here to see the best options</p>
</div>

<div class="container">
  <img src="http://vignette1.wikia.nocookie.net/roosterteeth/images/2/2a/Gus-sorola.jpg/revision/latest?cb=20150331072512" alt="Gus" style="width:90px">
  <p><span >Gus Sorola</span> Rooster Teeth Productions</p>
  <p>I love the minimalistic UI and rich content this website provides</p>
</div>

</body>
</html>
'''

#-------------------- PC Page-------------
@my_view.route('/pc')
def pc():
    return '''
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/Catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>

<head>
<title> PC </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<style>
img {
    display: block;
    margin: 0 auto;
}
</style>

<img src=http://i.imgur.com/7dQXj4x.png align="center" alt="pc" style="width:400px;height:400px;">
<hr>

<html>
<style>
body {font-family: "Lato", sans-serif;}

/* Style the tab */
div.tab {
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
}

/* Style the buttons inside the tab */
div.tab button {
    background-color: inherit;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
}

/* Change background color of buttons on hover */
div.tab button:hover {
    background-color: #ddd;
}
/* Create an active/current tablink class */
div.tab button.active {
    background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
    display: none;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-top: none;
}
</style>
</head>
<body>

<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'Information')">Information</button>
  <button class="tablinks" onclick="openCity(event, 'Cost')">Cost</button>
  <button class="tablinks" onclick="openCity(event, 'Purchase')">Purchase</button>
  <button class="tablinks" onclick="openCity(event, 'Photos')">Photos</button>
</div>

<div id="Information" class="tabcontent">
  <h3 style="font-family:'Lucida Console'">Information</h3>
  <p style="font-family:'Courier New'">PC's are great for gamers who want longevity and amazing results from their builds. Often referred to as the master race, computers can either be simple or complex, with intricate water cooling systems. Even the cheapest computer can last a while playing current generation games at appropriate user settings. Parts over the years can be individually upgraded and at their own will unlike consoles. Steam, a game client, offers thousands of games to users on their marketplace, while consoles have a very limited selection of games published. One positive to gaming on a PC is that it dual functions as a computer, and offers much more user experience than a console. The cost of playing online with friends is none because the cost is what you pay for your internet connection.  </p>
</div>

<div id="Cost" class="tabcontent">
  <h3 style="font-family:'Lucida Console'">Cost</h3>
  <p style="color:green;"> PC Cost: $300.00 - $3,000.00 </p>
  <p style="color:blue;"> Online Cost: Varies </p>
  <p style="color:red;"> Storage: 128gb - 4TB </p>
</div>

<div id="Purchase" class="tabcontent">
  <h3 style="font-family:'Lucida Console'">Purchase</h3>
  <p style="font-family:'Courier New'">Here you can select to purchase some parts of a PC:</p>
  <p style="font-family:'Courier New'"> Processors: </p>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/Intel-Desktop-Processor-i7-7700K-BX80677I77700K/dp/B01MXSI216/ref=sr_1_3?s=pc&ie=UTF8&qid=1494010834&sr=1-3&keywords=intel+processor"> Intel i7-7700k </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/dp/B01MRRPPQS/ref=psdc_229189_t2_B01MXSI216"> Intel i5-7600k </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/Intel-Core-i7-4790-Processor-BX80646I74790/dp/B00J56YSLM/ref=sr_1_2?s=electronics&ie=UTF8&qid=1494010925&sr=1-2&keywords=intel+i7-4790k"> Intel i7-4790  </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/AMD-Ryzen-1800X-Processor-YD180XBCAEWOF/dp/B06W9JXK4G/ref=sr_1_5?s=pc&ie=UTF8&qid=1494012719&sr=1-5&keywords=amd+ryzen"> AMD Ryzen  </a><br/>
  <p style="font-family:'Courier New'"> Motherboards: </p>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/ROG-STRIX-Z270E-GAMING-Motherboard/dp/B01NGTJNSZ/ref=sr_1_6?s=pc&ie=UTF8&qid=1494010994&sr=1-6&keywords=motherboards"> Asus ROG z270 </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/ROG-STRIX-Z270E-GAMING-Motherboard/dp/B01MSWF8L9/ref=sr_1_6?s=pc&ie=UTF8&qid=1494010994&sr=1-6&keywords=motherboards&th=1"> Asus Maximus IX Formula </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/MSI-Z270-GAMING-PRO-CARBON/dp/B01MY58BS3/ref=sr_1_20?s=electronics&ie=UTF8&qid=1494011107&sr=1-20&keywords=motherboards+msi"> MSI Performance Gaming Intel z270 </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/dp/B01NBFZUUO/ref=psdc_1048424_t1_B01MY58BS3"> GIGABYTE Aorus GA-Z270X Gaming K7 </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/MSI-X370-GAMING-PRO-CARBON/dp/B06WGS4FJL/ref=sr_1_1?s=electronics&ie=UTF8&qid=1494012764&sr=1-1&keywords=motherboard+ryzen"> MSI X370 Gaming Pro Carbon </a><br/>
  <p style="font-family:'Courier New'"> Graphics Cards: </p>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/ASUS-GeForce-STRIX-Graphics-STRIX-GTX1080-A8G-GAMING/dp/B01K5F8MJK/ref=sr_1_2?s=electronics&ie=UTF8&qid=1494011572&sr=1-2&keywords=gtx+1080"> Asus GeForce GTX 1080 Strix </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/EVGA-GeForce-Support-Graphics-08G-P4-6286-KR/dp/B01GAI64GO/ref=sr_1_3?s=electronics&ie=UTF8&qid=1494011572&sr=1-3&keywords=gtx+1080"> EVGA GeForce GTX 1080 </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/Gigabyte-GeForce-GDDR5-Windforce-GV-N1070WF2OC-8GD/dp/B01HHCA1IO/ref=sr_1_4?s=electronics&ie=UTF8&qid=1494011632&sr=1-4&keywords=gtx%2B1070&th=1"> Gigabyte GeForce GTX 1070 Windforce OC </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/MSI-GTX-1070-GAMING-8G/dp/B01GXOX3SW/ref=sr_1_7?s=electronics&ie=UTF8&qid=1494011783&sr=1-7&keywords=gtx+1070"> MSI Gaming GeForce GTX 1070 </a><br/>
  <p style="font-family:'Courier New'"> Cases: </p>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/NZXT-Tower-Computer-White-CA-S340W-W1/dp/B01LZ3BJ5U/ref=sr_1_2?s=pc&ie=UTF8&qid=1494012574&sr=1-2&keywords=computer%2Bcase&th=1"> NZXT s340 </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/Phanteks-Enthoo-Evolv-Computer-Case/dp/B01F0KWTXA/ref=sr_1_1?ie=UTF8&qid=1494012681&sr=8-1&keywords=phanteks%2Bevo&th=1"> Phanteks Evolv  </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/quiet-BG001-Silent-Base-Orange/dp/B00PK3TW3I/ref=sr_1_8?ie=UTF8&qid=1494012744&sr=8-8&keywords=be%2Bquiet&th=1"> be quiet! BG001 </a><br/>
  <a style="text-decoration:none; color:#0000ff;" href="https://www.amazon.com/dp/B004ALI5KC/ref=psdc_572238_t3_B000I5JHB0"> Antec Nine Hundred Two V3 </a><br/>
</div>

<div id="Photos" class="tabcontent">
  <h3 style="font-family:'Lucida Console'">Photos</h3>
  <p style="font-family:'Courier New'"> Here are some examples of computer builds: </p>
  <img src="http://www.hex-gear.com/wp-content/uploads/2015/03/3-1024x754.jpg" alt="PC" style="width:400px;height:350px;">
  <p></p>
  <img src="https://i.imgur.com/pR7x89E.jpg" alt="PC1" style="width:400px;height:350px;">
  <p></p>
  <img src="http://i.imgur.com/5riTnQo.jpg" alt="PC2" style="width:400px;height:550px;">
  <p></p>
  <img src="https://mnpctech.com/images/companies/3/mnpctech_workshop_cooler_master_cm_storm_ghost_.jpg" alt="PC3" style="width:400px;height:400px;">
</div>

<script>
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
</script>
</body>
'''

#--------------------Catalog Page-------------
@my_view.route('/catalog')
@my_view.route('/Catalog')
def catalog():
    return '''
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>

<head>
<title> Catalog </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<style>
img {
    display: block;
    margin: 0 auto;
}
</style>

<img src=http://www.bahr.net.nz/wp-content/uploads/2013/07/Bookshelf-2.jpg align="center" alt="Mountain View" style="width:900px;height:300px;">
<hr>

<html>
<style>
body {font-family: "Lato", sans-serif;}

/* Style the tab */
div.tab {
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
}

/* Style the buttons inside the tab */
div.tab button {
    background-color: inherit;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
}

/* Change background color of buttons on hover */
div.tab button:hover {
    background-color: #ddd;
}
/* Create an active/current tablink class */
div.tab button.active {
    background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
    display: none;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-top: none;
}
</style>
</head>
<body>

<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'Books')">Books</button>
  <button class="tablinks" onclick="openCity(event, 'Publishers')">Publishers</button>
</div>

<div id="Books" class="tabcontent">
  <a style="text-decoration:none; color:#0000ff;" href="http://127.0.0.1:5000/books"> Books catalog</a>
</div>

<div id="Publishers" class="tabcontent">
  <a style="text-decoration:none; color:#0000ff;" href="http://127.0.0.1:5000/publishers"> Publishers catalog</a>
</div>

<script>
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
</script>
</body>

'''

#-------------------- Books Handler --------------------
@my_view.route('/books')
def books():

    header='''
    <html>
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>
</html>

<head>
<title> Games Table </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collections </h1>
<hr>
    '''
    command = """SELECT {b}.ID, {b}.Name, {b}.Author, {b}.Category, {p}.Name, {b}.Released
                      FROM {b} 
                      join {p} 
                      ON {b}.Publisher = {p}.ID
        """.format(b="Books", p='Publisher')

    cursor.execute(command)
    Catalog = cursor.fetchall()

    return header+(getBooks(Catalog))

#-------------------- Games Key Handler --------------------
#Parameters: Key, integer
@my_view.route('/books/<key>')
def book(key):

    header='''
    <html>
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>
</html>

<head>
<title> Book Titles </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<hr>
    '''
    NAME = 1
    AUTHOR = 2
    PUBLISHER = 3
    CATEGORY = 4
    RELEASED = 5
    COVER = 6

    command = """SELECT {b}.ID, {b}.Name, {b}.Author, {b}.Category, {p}.Name, {b}.Released, {b}.Cover
                      FROM {b} 
                      join {p} 
                      ON {b}.Publisher = {p}.ID
        """.format(b="Books", p='Publisher')
    cursor.execute(command)
    catalog_data = cursor.fetchall()

    if len(catalog_data) == 0:
        return """
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/Catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>

<head>
<title> Home </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<hr>
<style>
img {
    display: block;
    margin: 0 auto;
}
</style>

<img src=http://i.imgur.com/ARTIXTj.jpg align="center" alt="Mountain View" style="width:550px;height:300px;">
"""
    item = catalog_data[0]

    message = '<table>'
    message += '<center><h1>'+ item[NAME]+'</h1></center>'
    message += '<center><b>Author:  </b> ' + item[AUTHOR]+'</b><c/enter>'
    message += '<center><b>Category:  </b> ' + item[PUBLISHER]+'</b></center>'
    message += '<center><b>Publisher:  </b> ' + item[CATEGORY]+'</b></center>'
    message += '<center><b>Released in:  </b> ' + item[RELEASED]+'</b></center></td><br>'
    message += """<style>
img {
    display: block;
    margin: 0 auto;
}
</style>

<img src="""+item[COVER]+""" align="center" alt="Mountain View" style="width:800px;height:400px;">"""
    return header+message

#-------------------- Publishers Handler --------------------
@my_view.route('/publishers')
def publishers():

    header='''
    <html>
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>
</html>

<head>
<title> Studios </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<hr>
'''
    command = """SELECT *
                FROM {p}
        """.format(p='Publisher')

    cursor.execute(command)
    Catalog = cursor.fetchall()

    return header+(getPublisher(Catalog))



#-------------------- Developers Key Handler --------------------
#Parameters: Key, integer
@my_view.route('/publishers/<key>')
def publisher(key):

    header='''
    <html>
<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>
</html>

<head>
<title> Studio Title </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<hr>
    '''
    NAME = 1
    LOCATION = 2
    TITLES = 3
    RATING = 4

    command = """SELECT *
                      FROM {p}
        """.format(p='Publisher')
    cursor.execute(command)
    catalog_data = cursor.fetchall()

    if len(catalog_data) == 0:
        return """<head>
<style>
body {
    font-family: "Lato", sans-serif;
    transition: background-color .5s;
}

.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #2C3539;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}

.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #FFFFFF;
    display: block;
    transition: 0.3s;
}

.sidenav a:hover, .offcanvas a:focus{
    color: #F5F5F5;
}

.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}

#main {
    transition: margin-left .5s;
    padding: 16px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
</head>
<body>

<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="http://127.0.0.1:5000/">Home</a>
  <a href="http://127.0.0.1:5000/pc">PC</a>
  <a href="http://127.0.0.1:5000/playstation">Playstation</a>
  <a href="http://127.0.0.1:5000/xbox">Xbox</a>
  <a href="http://127.0.0.1:5000/nintendo">Nintendo</a>
  <a href="http://127.0.0.1:5000/news">News</a>
  <a href="http://127.0.0.1:5000/Catalog">Catalog</a>
</div>

<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

<script>
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "white";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}
</script>

</body>

<head>
<title> Home </title>
<head>

<body style="background-color:FEFEFE;">

<h1 style="font-size:300%;" align="center" style="font-family:'Times New Roman'"> The Collection </h1>
<hr>
<style>
img {
    display: block;
    margin: 0 auto;
}
</style>

<img src=http://i.imgur.com/ARTIXTj.jpg align="center" alt="Mountain View" style="width:550px;height:300px;">"""
    item = catalog_data[0]

    message = '<table>'
    message += '<center><h1>'+item[NAME]+'</h1></center>'
    message += '<center><b>Headquarters:  </b>'+item[LOCATION]+'</b></center>'
    message += '<center><b>Total Books Released:  </b>'+item[TITLES]+'</b></center>'
    message += '<center><b>Average Book Rating:  </b>'+item[RATING]+'</b></center><br>'

    return header+message
