
var imageArray = [
"https://i.ytimg.com/vi/1CQ1NzP0zhU/maxresdefault.jpg",
"http://cdn.soccerbible.com/media/36507/adidas-stellar-ace-img9.jpg",
"https://4.bp.blogspot.com/-4KkgQjTGpj0/V6TfeTbzA5I/AAAAAAAA-Us/CcN7Y-dARqI9zLBBUO8Qa3CbkGnreui0gCLcB/s1600/adidas-dark-space-ace-16-purecontrol.jpg",
"http://www.sportskicksstore.com/wp/wp-content/uploads/2016/09/adidas-ace-16-purecontrol-viper-pack-boots-400x225.jpg",       
"https://2.bp.blogspot.com/-ZLQVEi1t08g/WCe-H479cDI/AAAAAAABDPM/2-lpndhWd44Aaz5EWi_Q2aVS7BHJVTXGgCLcB/s738/nike-2016-2017-tech-craft-pack-4.jpg",
"https://3.bp.blogspot.com/-pt2FrWEt1o4/V5YW6mk4TgI/AAAAAAAA-X8/gIES-bJhm_IVA6NFT0C52jM_o-w5qkwhQCLcB/s1600/nike-magista-obra-2016-2017-lite-pack-boots%2B%25282%2529.jpg",                
"http://www.sil.lt/media/images/Prekes/Prekiu-foto/Nike-Mercurial/nike-mercurial-superfly-v-cr7-fg-852511-376-mens-soccer-cleats-3.jpg"
];
    
    var slideIndex = 1;
        showDivs(slideIndex);

        function plusDivs(n) {
          showDivs(slideIndex += n);
        }

        function showDivs(n) {
          var i;
          var x = document.getElementsByClassName("mySlides");
          if (n > x.length) {slideIndex = 1}    
          if (n < 1) {slideIndex = x.length}
          for (i = 0; i < x.length; i++) {
             x[i].style.display = "none";  
          }
          x[slideIndex-1].style.display = "block";  
        };

    $('#forwardBtn').on('click', function() {
        currentIndex++;
        renderImage();

    });

    $('#backBtn').on('click', function() {
        currentIndex--;
        renderImage();
    });      

    
    var name = prompt("What is your name?");
    var outputString ="Happy Birthday  " + name + "!!!";
    $("h1").html(outputString);

    var outputString ="Dear " + name ;
    $("h2").html(outputString);

    var age =prompt("How old are you?")
    var outputString ="Have a nice " + age + "th Birthday"  ;
    $("h3").html(outputString);

    google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawStuff);

      function drawStuff() {
        var data = new google.visualization.arrayToDataTable([
         ['Present', 'Rate'],
              ['Adidas Pure Control +16 Gold', 25,  ], 
              ['Adidas Pure Control +16 Black',30  ],
              ['Adidas Pure Control +16 Viper',25   ],
              ['Nike Hypervenom Techcraft Black', 20],
              ['Nike Obra 2 Pure Platinum', 30      ],
              ['CR7 Mercurial V Green', 10          ]
              ]);

        var options = {
          title: 'Rate',
          legend: { position: 'none' },
          chart: { title: 'Cleats rating ',
                   subtitle: 'popularity by percentage' },
          bars: 'horizontal', // Required for Material Bar Charts.
          axes: {
            x: {
              0: { side: 'top', label: 'Percentage'} // Top x-axis.
            }
          },
          bar: { groupWidth: "90%" }
        };

        var chart = new google.charts.Bar(document.getElementById('top_x_div'));
        chart.draw(data, options);
      };    

    

