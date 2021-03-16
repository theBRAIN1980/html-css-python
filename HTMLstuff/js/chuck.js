function showFact(joke) {
    document.querySelector("#fact").innerText = joke
}

axios.get("http://api.icndb.com/jokes/random")
    .then(response => showFact(response.data.value.joke))