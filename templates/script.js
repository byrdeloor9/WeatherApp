let weather = {
    'apikey':"8874533926928e550b8fef2e274a83f3",
    fetchWeather: function(){
        fetch(
            "http://api.openweathermap.org/data/2.5/weather?q=Denver&units=metric&appid=8874533926928e550b8fef2e274a83f3"
        ).then((Response) => Response.json())
        .then((data)=> console.log);
    },

}