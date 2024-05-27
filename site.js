function clearTable(table)
{
    
    let rowsLeft = true;
    
    while(rowsLeft === true)
    {
        let table_len = table.rows.length;
        if(table_len > 0)
        {
            table.deleteRow(0);
        }
        else
        {
            rowsLeft = false;
        }
    }
}


function loadNews()
{
    let articles = [];
    $.ajaxSetup({
        async: false
    });
    $.getJSON("news.json", function(json) {
        
        json.forEach(element => {
            articles.push(element);
        });
    });

    $.ajaxSetup({
        async: true
    });
    let table = document.getElementById("newsDisplay");
    clearTable(table);
    let table_len = articles.length;

    for(var i = 0; i < table_len + 1; i++)
    {
        if(i != 0)
        {
            let content = articles[i - 1].content;
            let title = articles[i - 1].title;

            var row = table.insertRow(i).outerHTML="<tr><td> <div class='news-article'> <h2>" + title + "</h2><br><h4>" + content + "</h4></div></td></tr>";
        }
        else
        {
            var row = table.insertRow(i).outerHTML="<tr><td><h2>News</h2></td></tr>";
        }
    }
        
}


function loadVideos()
{
    let videos = [];
    $.ajaxSetup({
        async: false
    });
    $.getJSON("videos.json", function(json) {
        
        json.forEach(element => {
            videos.push(element);
        });
    });

    $.ajaxSetup({
        async: true
    });
    let table = document.getElementById("videosDisplay");
    clearTable(table);
    let table_len = videos.length;

    for(var i = 0; i < table_len + 1; i++)
    {
        if(i != 0)
        {
            let videoId = videos[i - 1].videoId;
            let title = videos[i - 1].title;
            let summary = videos[i - 1].summary;

            let video = '<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/' + videoId + '?si=ONWrAHGsYhjC9TWk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>';

            var row = table.insertRow(i).outerHTML="<tr><td> <div class='news-article'> <h2>" + title + "</h2></br>" + video + "</br><h4>" + summary + "</h4></div></td></tr>";
        }
        else
        {
            var row = table.insertRow(i).outerHTML="<tr><td><h2>Videos</h2></td></tr>";
        }
    }
        
}

function displayIndividualGame(selected)
{
    let games = [];
    $.ajaxSetup({
        async: false
    });
    $.getJSON("games.json", function(json) {
        
        json.forEach(element => {
            games.push(element);
        });
    });

    $.ajaxSetup({
        async: true
    });

    let table = document.getElementById("individualDisplay");
    document.getElementById("individualDiv").style.opacity = 100;
    clearTable(table);

    
    let title = games[selected].title;
    let description = games[selected].description;
    let link = games[selected].link;
    let linkText = games[selected].linkText;
    
    table.insertRow(0).outerHTML = "<tr><td><h2>" + title + "</h2></td></tr>";

    const descriptionElement = "<h4>" + description + "</h4>";
    const button = "<a href='" + link + "' download=''><input type='button' value='" + linkText + "'/></a>";


    var row = table.insertRow(1).outerHTML="<tr><td> <div class='news-article'>" + descriptionElement + "</br>" + button + "</div></td></tr>";

    
}

function loadGames()
{
    let games = [];
    $.ajaxSetup({
        async: false
    });
    $.getJSON("games.json", function(json) {
        
        json.forEach(element => {
            games.push(element);
        });
    });

    $.ajaxSetup({
        async: true
    });
    let table = document.getElementById("gamesDisplay");
    clearTable(table);
    let table_len = games.length;

    clearTable(document.getElementById("individualDisplay"));

    document.getElementById("individualDiv").style.opacity = 0;

    for(var i = 0; i < table_len + 1; i++)
    {
        if(i != 0)
        {
            let title = games[i - 1].title;

            const button = "<a onclick='displayIndividualGame(" + (i - 1) + ")'><h2> " + title + "</h2></a>";


            var row = table.insertRow(i).outerHTML="<tr><td> <div class='news-article'>" + button + "</div></td></tr>";
        }
        else
        {
            var row = table.insertRow(i).outerHTML="<tr><td><h2>Games</h2></td></tr>";
        }
    }
        
}