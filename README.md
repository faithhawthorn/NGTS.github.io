# NGTS Webpage

To add new news items, follow this procedure.

1. Go to pages/news and create a new file called news_X.html, making sure X is incremented by 1.
2. Now put this in there
```html
<html>
<head>
<title></title>
<script
    src="https://code.jquery.com/jquery-3.3.1.js"
    integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
    crossorigin="anonymous">
</script>
<script> 
$(function(){
  $("#header").load("/pages/templates/header.html"); 
  $("#footer").load("/pages/templates/footer.html"); 
});
</script> 
</head>
<body>
<div id="header"></div>
<div>
    [YOUR NEWS TEXT GOES HERE]
</div>
<div id="footer"></div>
</body>
</html>
```
3. Now edit and put your news text in there. Images can go in images/news/ . Note that when you link them in the html, you will link them as /images/news/NGTS_wasp39.png as images is at the www root. 
4. Finally, pages/tabs/news_content.html needs linking to this new file so it can show the new news item. Just create a new dive like this
   ```html
       <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-card">
        <img src="/images/news/NGTS_wasp39.png" alt="John" style="width:100%">
        <div class="w3-container">
          <h3>  NGTS supports exoplanet atmosphere studies with the James Webb Space Telescope</h3>
          <p class="w3-opacity ws-xxsmall">2022-11-22 Peter Wheatley</p>
          <p><button onclick="location.href='/pages/news/news_17_page.html'" class="w3-button w3-light-grey w3-block"><i class="fa"></i> Find out more</button></p>
        </div>
      </div>
    </div>
   ```

5. You can also modify pages/templates/footer.html to put the latest news there. 

