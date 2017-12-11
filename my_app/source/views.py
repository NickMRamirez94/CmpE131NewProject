from flask import Blueprint
from my_app.source.models import cursor

my_view = Blueprint('my_view', __name__)

#-------Home Page---------
@my_view.route('/')
@my_view.route('/home')
def greeting():
    return '''
 <html lang="en">
   <head>
    <title>Gustoso</title>
     <!-- Required meta tags -->
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

     <style>

     .container {
      width: 100%;
      padding-right: 15px;
      padding-left: 15px;
      margin-right: auto;
      margin-left: auto;
    }

    @media (min-width: 576px) {
      .container {
        max-width: 540px;
      }
    }

    @media (min-width: 768px) {
      .container {
        max-width: 720px;
      }
    }

    @media (min-width: 992px) {
      .container {
        max-width: 960px;
      }
    }

    @media (min-width: 1200px) {
      .container {
        max-width: 1140px;
      }
    }
     .banner {
     	width: 100%;
     	display: block;

     }

     .banner > .banner-image{
     	width: 100%;
     	display: block;
     }

     ul {
         list-style-type: none;
         margin: 0;
         padding: 0;
         overflow: hidden;
         background-color: white;
     }

     li {
         float: left;
     }

     li a {
         display: block;
         color: black;
         text-align: center;
         padding: 14px 16px;
         text-decoration: none;
     }

     li a:hover {
         border: 1px solid #D2D4D5;
         color: #7F7F7F
     }

    .col-sm-6 {
    -ms-flex: 0 0 50%;
        flex: 0 0 50%;
    max-width: 50%;
    }

    .col-6 {
      -ms-flex: 0 0 50%;
          flex: 0 0 50%;
      max-width: 50%;
    }

    .col-sm-4 {
        -ms-flex: 0 0 33.333333%;
            flex: 0 0 33.333333%;
        max-width: 33.333333%;
      }

    .col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col,
    .col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm,
    .col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md,
    .col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg,
    .col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl,
    .col-xl-auto {
      position: relative;
      width: 100%;
      min-height: 1px;
      padding-right: 15px;
      padding-left: 15px;
    }

    .col {
      -ms-flex-preferred-size: 0;
          flex-basis: 0;
      -ms-flex-positive: 1;
          flex-grow: 1;
      max-width: 100%;
    }

    .row {
      display: -ms-flexbox;
      display: flex;
      -ms-flex-wrap: wrap;
          flex-wrap: wrap;
      margin-right: -15px;
      margin-left: -15px;
    }

    .text-center {
      text-align: center !important;
    }

    h1{
        font-family: "proxima-nova";
        text-transform: uppercase;
        font-weight: 600;
        font-size: 2.5em;
    }

    h3{
        font-weight: 100;
    }

    .top-buffer{
        margin-top: 20px;
    }

    .top-buffer-large{
        margin-top: 35px;
    }

    .top-buffer-xlarge{
        margin-top: 100px;
    }

    .img-thumbnail {
      padding: 0.25rem;
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 0.25rem;
      transition: all 0.2s ease-in-out;
      max-width: 100%;
      height: 200px;
    }

    .img-thumbnail2 {
      padding: 0.25rem;
      background-color: #fff;
      border: 1px solid #ddd;
      border-radius: 0.25rem;
      transition: all 0.2s ease-in-out;
      max-width: 100%;
      height: 300px;
    }

    .button {
        background-color: #4e5156; /* DarkGrey */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: block;
        margin: 0 auto;
        width: 20%
        font-size: 16px;
    }

    .pt-5,
    .py-5 {
      padding-top: 3rem !important;
    }

    .pb-5,
    .py-5 {
      padding-bottom: 3rem !important;
    }


     </style>
   </head>

   <body style="background-color:white">

    <!--Navigation Bar-->
     <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark navbar-static-top">
        <ul>
          <li><a href="http://127.0.0.1:5000/">Menus</a></li>
          <li><a href="http://127.0.0.1:5000/reservations">Reservations</a></li>
          <li><a href="#">Order Online</a></li>
          <li><a href="#">More</a></li>
        </ul>
    </nav>

    <!--Main Image-->
      <div class="banner">
        <img class="banner-image" src="https://wallpaperscraft.com/image/national_day_of_pizza_2015_pizza_cheese_pastries_100087_3840x2160.jpg">
      </div>

      <div class="container">
          <div class="row top-buffer">
            <div class="col text-center">
                <h1>gustoso menus</h1>
            </div>
          </div> <!--End First row-->

          <div class="row">
            <div class="col text-center">
            <p>Gustoso Restaurant is a family owned Restaurant that first opened in 1990. It is one of </br>San Francisco's premiere locations for food and
            excellent service.</p>
            </div>
          </div> <!--End Second Row-->

          <div class="row">

            <!--Beer Menu-->
            <div class="col text-center">
                <div class="row">
                    <img src="https://wallpaperscraft.com/image/beer_glasses_two_1391_1920x1080.jpg" alt="beer" class="img-thumbnail">
                </div>
                <div class="row text-center">
                    <h3 style="width:100%">BEER + WINE + COCKTAILS</h3>
                </div>
                <div class="row top-buffer-large text-center">
                    <a href="#" class="button">View Drink Menu</a>
                </div>
            </div>

            <!--Lunch and Dinner Menu-->
            <div class="col">
                <div class="row">
                    <img src="https://i.pinimg.com/originals/36/41/2d/36412d255dcd53a3523dcc1afb5612d2.jpg" alt="pizza" class="img-thumbnail">
                </div>
                <div class="row text-center">
                    <h3 style="width:100%">LUNCH + DINNER MENU</h3>
                </div>
                <div class="row top-buffer-large">
                    <a href="#" class="button">View Dinner Menu</a>
                </div>
            </div>

            <!--Brunch Menu-->
            <div class="col">
                <div class="row">
                    <img src="https://wallpaperscraft.com/image/tea_camomiles_breakfast_croissants_berry_21654_1920x1080.jpg" alt="breakfast" class="img-thumbnail">
                </div>
                <div class="row text-center">
                    <h3 style="width:100%">BRUNCH MENU</h3>
                </div>
                <div class="row top-buffer-large">
                    <a href="#" class="button">View Brunch Menu</a>
                </div>
            </div>

          </div> <!--End Third Row-->

          <div class="row top-buffer-xlarge">

            <!--Steak Specials-->
            <div class="col">
                <div class="row">
                    <img src="https://wallpaperscraft.com/image/steak_meat_vegetables_dinner_110386_1920x1080.jpg" alt="steak" class="img-thumbnail2">
                </div>
                <div class="row text-center">
                    <h3 style="width:100%">FRIDAY STEAKS</h3>
                </div>
                <div class="row top-buffer-large">
                    <a href="#" class="button">View Steak Specials</a>
                </div>
            </div>

            <!--Happy Hour Menu-->
                <div class="col">
                    <div class="row">
                        <img src="https://wallpaperscraft.com/image/mojito_drink_mint_ice_113611_1920x1080.jpg" alt="happyhour" class="img-thumbnail2">
                    </div>
                    <div class="row text-center">
                        <h3 style="width:100%">HAPPY HOUR MENU</h3>
                    </div>
                    <div class="row top-buffer-large">
                        <a href="#" class="button">View Happy Hour Menu</a>
                    </div>
                </div>

          </div> <!--End Fourth Row-->

      </div> <!--End Container-->

    <div class="row top-buffer-xlarge">
        <div class="banner">
          <img class="banner-image" src="https://images8.alphacoders.com/358/358841.jpg">
        </div>
    </div> <!--End Last Row Bottom Banner-->

        <!-- Footer -->
        <div>
          <div class="container">
            <p style="float:left"><b>We Are Located At</b></br>
            1234 Diablo Lane</br>
            San Francisco, CA 94121</p>
            <p style="float:right"><b>Hours</b></br>
            Monday to Thursday 11am-10pm</br>
            Friday and Saturday 11am-12pm</br>
            Closed Sundays</p>
          </div>
        </div>


    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
   </body>
 </html>


'''

#-------------------- Reseravtions Page-------------
@my_view.route('/reservations')
def reservations():
    return '''
<html lang="en">
  <head>
   <title>Gustoso</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <style>

    .container {
     width: 100%;
     padding-right: 15px;
     padding-left: 15px;
     margin-right: auto;
     margin-left: auto;
   }

   @media (min-width: 576px) {
     .container {
       max-width: 540px;
     }
   }

   @media (min-width: 768px) {
     .container {
       max-width: 720px;
     }
   }

   @media (min-width: 992px) {
     .container {
       max-width: 960px;
     }
   }

   @media (min-width: 1200px) {
     .container {
       max-width: 1140px;
     }
   }
    .banner {
       width: 100%;
       display: block;

    }

    .banner > .banner-image{
       width: 100%;
       display: block;
    }

    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: white;
    }

    li {
        float: left;
    }

    li a {
        display: block;
        color: black;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }

    li a:hover {
        border: 1px solid #D2D4D5;
        color: #7F7F7F
    }

   .col-sm-6 {
   -ms-flex: 0 0 50%;
       flex: 0 0 50%;
   max-width: 50%;
   }

   .col-6 {
     -ms-flex: 0 0 50%;
         flex: 0 0 50%;
     max-width: 50%;
   }

   .col-sm-4 {
       -ms-flex: 0 0 33.333333%;
           flex: 0 0 33.333333%;
       max-width: 33.333333%;
     }

   .col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col,
   .col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm,
   .col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md,
   .col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg,
   .col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl,
   .col-xl-auto {
     position: relative;
     width: 100%;
     min-height: 1px;
     padding-right: 15px;
     padding-left: 15px;
   }

   .col {
     -ms-flex-preferred-size: 0;
         flex-basis: 0;
     -ms-flex-positive: 1;
         flex-grow: 1;
     max-width: 100%;
   }

   .row {
     display: -ms-flexbox;
     display: flex;
     -ms-flex-wrap: wrap;
         flex-wrap: wrap;
     margin-right: -15px;
     margin-left: -15px;
   }

   .text-center {
     text-align: center !important;
   }

   h1{
       font-family: "proxima-nova";
       text-transform: uppercase;
       font-weight: 600;
       font-size: 2.5em;
   }

   h3{
       font-weight: 100;
   }

   .top-buffer{
       margin-top: 20px;
   }

   .top-buffer-large{
       margin-top: 35px;
   }

   .top-buffer-xlarge{
       margin-top: 100px;
   }

   .img-thumbnail {
     padding: 0.25rem;
     background-color: #fff;
     border: 1px solid #ddd;
     border-radius: 0.25rem;
     transition: all 0.2s ease-in-out;
     max-width: 100%;
     height: 200px;
   }

   .img-thumbnail2 {
     padding: 0.25rem;
     background-color: #fff;
     border: 1px solid #ddd;
     border-radius: 0.25rem;
     transition: all 0.2s ease-in-out;
     max-width: 100%;
     height: 300px;
   }

   .button {
       background-color: #4e5156; /* DarkGrey */
       border: none;
       color: white;
       padding: 15px 32px;
       text-align: center;
       text-decoration: none;
       display: block;
       margin: 0 auto;
       width: 20%
       font-size: 16px;
   }

   .pt-5,
   .py-5 {
     padding-top: 3rem !important;
   }

   .pb-5,
   .py-5 {
     padding-bottom: 3rem !important;
   }

   .reserv-text{
        font-size: 125%;
        font-family: arial;
       }

   .img-center {
        display: block;
        margin: 0 auto;
    }


    </style>
  </head>

  <body style="background-color:white">

   <!--Navigation Bar-->
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark navbar-static-top">
       <ul>
         <li><a href="http://127.0.0.1:5000/">Menus</a></li>
         <li><a href="http://127.0.0.1:5000/Reservations">Reservations</a></li>
         <li><a href="#">Order Online</a></li>
         <li><a href="#">More</a></li>
       </ul>
   </nav>

   <!--Main Image-->
     <div class="banner">
       <img class="banner-image" src="https://wallpaperscraft.com/image/spaghetti_italian_food_seafood_dish_107740_1920x1080.jpg">
     </div>

     <div class="container">

        <div class="row top-buffer-xlarge">
            <a href="#" class="button">PLACE A RESERVATION</a>
        </div> <!--End First Row-->

        <div class="col">

            <div class ="row top-buffer">
                <p class="reserv-text text-center" style="width:100%">QUALITY INGREDIENTS. FRESH FOOD. ALL ITALIAN.</p>
            </div> <!--End Second Row-->

            <div class = "row top-buffer">
                <p class="reserv-text text-center" style="width:100%"><b>RESERVATIONS: </b>(123) 456-7890</p>
            </div> <!--End Third Row-->

            <div class ="row top-buffer">
                <p class="reserv-text text-center" style="width:100%">PLEASE NOTE: STARTING OCTOBER 24TH WE WILL BE CLOSING EVERYDAY</br>
                BETWEEN THE HOURS OF 3-4.</p>
            </div> <!--End Fourth Row-->

            <div class="row top-buffer">
                <img style="height:250px" class="img-center" src="https://i.pinimg.com/236x/f0/7f/f2/f07ff281777046de02aa8a297a8c657d--pasta-shells-coffee-cafe.jpg">
            </div> <!--End Fifth Row-->

        </div> <!--End First Col-->


        <!--Here's the 3x2 pictures-->
        <div class="row">
            <div class="col">
                <img style="height:300px" class="img-center img-thumbnail" src="https://wallpaperscraft.com/image/buildings_night_lights_110960_1280x1024.jpg">
            </div> <!--End First Col-->
            <div class="col">
                <img style="height:300px" class="img-center img-thumbnail" src="https://wallpaperscraft.com/image/cafe_restaurant_wine_wine_racks_design_39247_1280x1024.jpg">
            </div> <!--End Second Col-->
            <div class="col">
                <img style="height:300px" class="img-center img-thumbnail" src="https://wallpaperscraft.com/image/desk_restaurant_wine_glasses_plates_flowers_roses_80713_1280x1024.jpg">
            </div> <!--End Third Col-->
        </div> <!--End First Row-->

        <div class="row">
            <div class="col">
                <img style="height:300px" class="img-center img-thumbnail" src="https://wallpaperscraft.com/image/evening_table_dinner_restaurant_coast_look_fires_garland_48367_1280x1024.jpg">
            </div> <!--End First Col-->
            <div class="col">
                <img style="height:300px" class="img-center img-thumbnail" src="https://wallpaperscraft.com/image/waiter_tray_food_restaurant_77445_1280x1024.jpg">
            </div> <!--End Second Col-->
            <div class="col">
                <img style="height:300px" class="img-center img-thumbnail" src="https://wallpaperscraft.com/image/design_locking_interior_house_carpet_bathroom_brown_box_style_table_31493_1280x1024.jpg">
            </div> <!--End Third Col-->
        </div> <!--End Second Row-->

     </div> <!--End Container-->

     <div class="row top-buffer-xlarge">
         <div class="banner">
           <img class="banner-image" src="https://wallpaperscraft.com/image/restaurant_table_interior_modern_style_39288_1920x1080.jpg">
         </div>
     </div> <!--End Last Row Bottom Banner-->

       <!-- Footer -->
       <div>
         <div class="container">
           <p style="float:left"><b>We Are Located At</b></br>
           1234 Diablo Lane</br>
           San Francisco, CA 94121</p>
           <p style="float:right"><b>Hours</b></br>
           Monday to Thursday 11am-10pm</br>
           Friday and Saturday 11am-12pm</br>
           Closed Sundays</p>
         </div>
       </div>


   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
  </body>
</html>
'''

#--------------------Order Page-------------
@my_view.route('/catalog')
@my_view.route('/Catalog')
def catalog():
    return '''


'''
